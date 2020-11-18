import binascii
import hashlib
import io
import logging
import os
from collections import defaultdict
from concurrent.futures import wait
from concurrent.futures.thread import ThreadPoolExecutor
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from struct import pack, unpack

import zstandard as zstd
from PIL import Image

from .chacha import Key, chacha, filename_hash
from .known_assets import IMAGES_DONT_CONVERT, KNOWN_ASSETS

EXTRACTED_DIR = Path("Extracted")
OVERRIDES_DIR = Path("Overrides")
DEFAULT_COMPRESSION_LEVEL = 20
BANK_ALIGNMENT = 32


class MissingAsset(Exception):
    """Returned when an expected asset is missing."""


class Asset(object):
    def __init__(
        self, name_hash, name_len, filename, asset_data,
        asset_len, encrypted, offset, data_offset, data_size
    ):
        self.name_hash = name_hash
        self.name_len = name_len
        self.filename = filename
        self.asset_data = asset_data
        self.asset_len = asset_len
        self.encrypted = encrypted
        self.offset = offset
        self.data_offset = data_offset
        self.data_size = data_size
        self.asset_data = asset_data
        self.data = None

    @property
    def total_size(self):
        return 8 + self.name_len + self.asset_len

    def __repr__(self):
        return (
            "Asset("
            "name_hash={!r}, name_len={!r}, filename={!r}, asset_len={!r}, encrypted={!r}, "
            "offset={}, data_offset={}, data_size={!r}"
            ")"
        ).format(
            binascii.hexlify(self.name_hash or b""),
            self.name_len,
            self.filename,
            self.asset_len,
            self.encrypted,
            hex(self.offset),
            hex(self.data_offset),
            self.data_size,
        )

    def match_hash(self, hash_):
        min_len = min(len(hash_), self.name_len)
        return hash_[:min_len] == self.name_hash[:min_len]

    def load_data(self, handle):
        """ Cache data on the asset. Must be called before extraction."""
        handle.seek(self.data_offset)
        self.data = handle.read(self.data_size)

    def extract(self, mods_dir, dest_path, key, compression_level=DEFAULT_COMPRESSION_LEVEL):
        if self.data is None:
            raise RuntimeError("load_data hasn't been called.")

        path = mods_dir / dest_path
        compressed_path = mods_dir / ".compressed" / dest_path
        filepath = path / self.filename.decode()
        compressed_filepath = compressed_path / f"{self.filename.decode()}.zst"
        md5sum_filepath = compressed_path / f"{self.filename.decode()}.md5sum"


        if self.encrypted:
            try:
                # Decrypt
                self.data = chacha(self.filename, self.data, key)

                # Decompress
                cctx = zstd.ZstdDecompressor()
                self.data = cctx.decompress(self.data)

                # Recompress at higher compression level to give
                # better chance of assets fitting in binary
                logging.info("Storing compressed asset %s...", compressed_filepath)
                with compressed_filepath.open("wb") as compressed_file:
                    cctx = zstd.ZstdCompressor(level=compression_level)
                    compressed_data = cctx.compress(self.data)
                    compressed_file.write(compressed_data)

            except Exception:  # pylint: disable=broad-except
                logging.exception("Failed compression")
                return None


        if filepath.suffix == ".DDS" and self.filename not in IMAGES_DONT_CONVERT:
            image = Image.open(io.BytesIO(self.data))
            # Swap byte order to read correct endianness
            image.tile[0] = image.tile[0][:-1] + ((image.tile[0][-1][0][::-1], 0, 1),)
            new_data = io.BytesIO()
            image.save(new_data, format="PNG")
            self.data = new_data.getvalue()

        # Get a hash of the the uncompressed file to be used
        # to detect if the source file changed
        md5sum = hashlib.md5(self.data).hexdigest()
        with md5sum_filepath.open("w") as md5sum_file:
            md5sum_file.write(md5sum)

        logging.info("Storing asset %s...", filepath)
        if filepath.suffix == ".DDS" and self.filename not in IMAGES_DONT_CONVERT:
            filepath = filepath.with_suffix(".png")

        with filepath.open("wb") as asset_file:
            asset_file.write(self.data)


class AssetStore(object):

    DATA_OFFSET = 0x400

    def __init__(self, exe_handle):
        self.assets = []
        self.exe_handle = exe_handle
        self.total_size = 0
        self._key = Key()

    @property
    def key(self):
        return self._key.key

    def update_key(self, size):
        self._key.update(size)

    def recalculate_key(self):
        new_key = Key()
        for asset in self.assets:
            if asset.filename is None:
                continue
            new_key.update(asset.asset_len)
        self._key = new_key

    def rehash_all_files(self):
        for asset in self.assets:
            if asset.filename is None:
                continue
            asset.name_hash = self.filename_hash(asset.filename).ljust(asset.name_len, b"\x00")

    def find_asset(self, filename):
        if filename is None:
            return None
        name_hash = filename_hash(filename, self.key)
        for asset in self.assets:
            if asset.match_hash(name_hash):
                return asset
        return None

    def filename_hash(self, filename):
        if filename is None:
            return None
        return filename_hash(filename, self.key)

    def pack_assets(self):
        self.exe_handle.seek(self.DATA_OFFSET)

        for asset in self.assets:
            if asset.filename is None:
                continue

            assert asset.data_size == asset.asset_data.get_data_size()
            data = asset.asset_data.get_data()

            if asset.encrypted:
                logging.info("Encrypting file %s", asset.asset_data.filename)
                data = chacha(asset.filename, data, self.key)

            logging.info("Packing file %s", asset.asset_data.filename)
            self.exe_handle.write(pack("<II", asset.asset_len, asset.name_len))
            self.exe_handle.write(asset.name_hash)
            self.exe_handle.write(pack("<b", asset.encrypted))
            self.exe_handle.write(data)

        self.exe_handle.write(pack("<II", 0, 0))

    @classmethod
    def load_from_file(cls, exe_handle):
        asset_store = cls(exe_handle)
        asset_store.exe_handle.seek(cls.DATA_OFFSET)

        while True:
            offset = asset_store.exe_handle.tell()
            asset_len, name_len = unpack(b"<II", asset_store.exe_handle.read(8))
            if (asset_len, name_len) == (0, 0):
                break
            assert asset_len > 0

            name_hash = asset_store.exe_handle.read(name_len)
            encrypted = asset_store.exe_handle.read(1) == b"\x01"
            data_offset = asset_store.exe_handle.tell()
            data_size = asset_len - 1

            asset_store.exe_handle.seek(data_size, 1)
            asset_store.update_key(asset_len)

            asset = Asset(
                name_hash=name_hash,
                name_len=name_len,
                filename=None,
                asset_data=None,
                asset_len=asset_len,
                encrypted=encrypted,
                offset=offset,
                data_offset=data_offset,
                data_size=data_size,
            )
            asset_store.assets.append(asset)
            asset_store.total_size += asset.total_size

        return asset_store

    def populate_asset_names(self):
        for filename in KNOWN_ASSETS:
            asset = self.find_asset(filename)
            if asset is None:
                continue
            asset.filename = filename

    def repackage(
        self, mods_dir, search_dirs, extracted_dir,
        compression_level=DEFAULT_COMPRESSION_LEVEL
    ):
        self.populate_asset_names()
        asset_bundle = AssetBundle.from_dirs(self, Path(mods_dir), search_dirs, extracted_dir)
        asset_bundle.compress(compression_level=compression_level)

        offset = self.DATA_OFFSET
        for asset in self.assets:
            if asset.filename is None:
                continue
            asset_data = asset_bundle.get(str(Path(asset.filename.decode()).name))
            if asset_data is None:
                raise MissingAsset(f"FAIL {asset.filename.decode()}")

            asset.asset_data = asset_data

            asset.offset = offset
            asset.data_size = asset_data.get_data_size()
            asset.data_offset = asset.offset + 8 + asset.name_len + 1

            # The name hash of soundbank files is padded such that the data_offset
            # is divisible by 32.
            #
            # Padding is between 1 and 32 bytes
            if asset_data.file_path.suffix == ".bank":
                padding = BANK_ALIGNMENT - asset.data_offset % BANK_ALIGNMENT
                asset.name_len += padding
                asset.data_offset += padding

            asset.asset_len = asset.data_size + 1
            offset += asset.total_size

        self.recalculate_key()
        self.rehash_all_files()
        self.pack_assets()


class ResolutionPolicy(Enum):
    RaiseError = 1
    FirstWins = 2
    LastWins = 3


class FileConflict(Exception):
    pass


class MultipleMatchingAssets(Exception):
    pass


KNOWN_ASSET_NAMES = {
    Path(path.decode()).name: path.decode()
    for path in KNOWN_ASSETS
}


def get_files_from_search_dir(mods_dir, search_dir):
    out_files = {}

    search_dir = mods_dir / search_dir
    if not search_dir.exists():
        return out_files

    for root, dirs, files in os.walk(search_dir, topdown=True):
        dirs[:] = [d for d in dirs if d not in [".compressed"]]

        for file_ in files:
            real_name = file_
            if Path(file_).suffix == ".png":
                real_name = str(Path(file_).with_suffix(".DDS"))

            if real_name not in KNOWN_ASSET_NAMES:
                continue

            if file_ in out_files:
                MultipleMatchingAssets(f"Found {file_} multiple times in {search_dir}")
            out_files[file_] = (
                search_dir.relative_to(mods_dir),
                (Path(root) / file_).relative_to(search_dir)
            )

    return out_files


def to_dds(img):
    img = img.convert("RGBA")

    # https://docs.microsoft.com/en-us/windows/win32/direct3ddds/dds-header
    header_size = 124  # always the same
    flags = 0x0002100F  # required flags + pitch + mipmapped

    height = img.height
    width = img.width

    pitch = width * 4  # bytes per line
    depth = 1
    mipmaps = 1

    # pixel format sub structure
    pfsize = 32  # size of pixel format structure, constant
    pfflags = 0x41  # uncompressed RGB with alpha channel
    fourcc = 0  # compression mode (not used for uncompressed data)
    bitcount = 32
    # bit masks for each channel, here for RGBA
    rmask = 0xFF000000
    gmask = 0x00FF0000
    bmask = 0x0000FF00
    amask = 0x000000FF

    caps = 0x1000  # simple texture with only one surface and no mipmaps
    caps2 = 0  # additional surface data, unused
    caps3 = 0  # unused
    caps4 = 0  # unused

    data = b"DDS "  # magic bytes
    data += pack("<II", header_size, flags)
    data += pack("<5I", height, width, pitch, depth, mipmaps)
    data += pack("<11I", *((0,)*11))  # reserved
    data += pack("<4I", pfsize, pfflags, fourcc, bitcount)
    data += pack(">4I", rmask, gmask, bmask, amask)  # masks are stored in big endian
    data += pack("<4I", caps, caps2, caps3, caps4)
    data += pack("<I", 0)  # reserved

    data += bytes(
        (
            byte if rgba[3] != 0 else 0
        )  # Hack to force all transparent pixels to be (0, 0, 0, 0)
           # instead of (255, 255, 255, 0)
        for rgba in img.getdata()
        for byte in rgba
    )

    return data


@dataclass
class AssetBundle:
    def __init__(self, asset_datas):
        self.asset_datas = asset_datas

    def get(self, key, default=None):
        return self.asset_datas.get(key, default)

    @classmethod
    def from_dirs(
        cls, asset_store, mods_dir, search_dirs, fallback_dir,
        resolution_policy=ResolutionPolicy.RaiseError
    ):

        pack_assets = defaultdict(list)
        asset_datas = {}

        for search_dir in search_dirs:
            for (file_, file_paths) in get_files_from_search_dir(mods_dir, search_dir).items():
                pack_assets[file_].append(file_paths)

        for asset in asset_store.assets:
            if asset.filename is None:
                continue
            filename = Path(asset.filename.decode())
            if filename.suffix == ".DDS" and asset.filename not in IMAGES_DONT_CONVERT:
                filename = filename.with_suffix(".png")
            assets = pack_assets.get(filename.name)

            if not assets:
                file_path = mods_dir / fallback_dir / filename
                if not file_path.exists():
                    raise MissingAsset(f"Didn't find an asset for {file_path}")

                asset_datas[str(Path(asset.filename.decode()).name)] = AssetData(
                    mods_dir, fallback_dir, filename, asset
                )
                continue

            if resolution_policy == ResolutionPolicy.RaiseError and len(assets) >= 2:
                raise FileConflict(
                    f"{filename} found in multiple packs: {', '.join(assets)}"
                )

            idx = 0
            if resolution_policy == ResolutionPolicy.FirstWins:
                idx = 0
            elif resolution_policy == ResolutionPolicy.LastWins:
                idx = -1

            search_dir, filename_ = assets[idx]
            asset_datas[str(Path(asset.filename.decode()).name)] = AssetData(
                mods_dir, search_dir, filename_, asset
            )

        return cls(asset_datas)

    def compress(self, compression_level=DEFAULT_COMPRESSION_LEVEL):
        pool = ThreadPoolExecutor()
        futures = [
            pool.submit(asset_data.compress, compression_level)
            for asset_data in self.asset_datas.values()
            if asset_data.needs_compression()
        ]
        wait(futures, timeout=300)

@dataclass
class AssetData:
    mods_dir: Path
    path: Path
    filename: str
    asset: Asset

    def md5sum_of_file(self):
        with self.file_path.open("rb") as file_:
            md5sum = hashlib.md5()
            chunk = file_.read(8192)
            while chunk:
                md5sum.update(chunk)
                chunk = file_.read(8192)
            return md5sum.hexdigest().encode()

    @property
    def real_suffix(self):
        if self.filename.suffix == ".png" and self.asset.filename not in IMAGES_DONT_CONVERT:
            return ".DDS"
        return self.filename.suffix

    @property
    def file_path(self):
        return self.mods_dir /self.path / self.filename

    @property
    def compressed_name(self):
        return f"{self.filename.with_suffix(self.real_suffix)}.zst"

    @property
    def compressed_path(self):
        return self.mods_dir / ".compressed" / self.path / self.compressed_name

    @property
    def md5sum_name(self):
        return f"{self.filename.with_suffix(self.real_suffix)}.md5sum"

    @property
    def md5sum_path(self):
        return self.mods_dir / ".compressed" / self.path / self.md5sum_name

    def needs_compression(self):
        if not self.asset.encrypted:
            return False

        if not self.md5sum_path.exists():
            return True

        if not self.compressed_path.exists():
            return True

        md5sum = self.md5sum_of_file()
        with self.md5sum_path.open("rb") as md5sum_file:
            stored_md5sum = md5sum_file.read().strip()
        if md5sum != stored_md5sum:
            return True

        return False

    def compress(self, compression_level=DEFAULT_COMPRESSION_LEVEL):
        if not self.asset.encrypted:
            return

        self.compressed_path.parent.mkdir(parents=True, exist_ok=True)
        self.md5sum_path.parent.mkdir(parents=True, exist_ok=True)

        if self.file_path.suffix == ".png":
            logging.info('Converting image "%s" to DDS', self.filename)
            with Image.open(self.file_path) as img:
                data = to_dds(img)
        else:
            with open(self.file_path, "rb") as asset_file:
                data = asset_file.read()

        md5sum = self.md5sum_of_file()
        with self.md5sum_path.open("wb") as md5sum_file:
            md5sum_file.write(md5sum)

        logging.info("Compressing %s...", self.filename)
        cctx = zstd.ZstdCompressor(level=compression_level)
        data = cctx.compress(data)
        with open(self.compressed_path, "wb") as compressed_file:
            compressed_file.write(data)

    def get_data_size(self):
        if self.asset.encrypted:
            path = self.compressed_path
        else:
            path = self.file_path
        return path.stat().st_size

    def get_data(self):
        if self.asset.encrypted:
            path = self.compressed_path
        else:
            path = self.file_path

        with path.open("rb") as file_:
            return file_.read()
