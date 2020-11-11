from struct import pack, unpack
from PIL import Image
import binascii
import io
import os
import hashlib
import logging
from pathlib import Path
import zstandard as zstd
from dataclasses import dataclass

from .chacha import Key, filename_hash, chacha
from .known_assets import KNOWN_ASSETS

EXTRACTED_DIR = Path("Extracted")
OVERRIDES_DIR = Path("Overrides")
DEFAULT_COMPRESSION_LEVEL = 20
BANK_ALIGNMENT = 32

class MissingAsset(Exception):
    """Returned when an expected asset is missing."""


class Asset(object):
    def __init__(
        self, name_hash, name_len, filename, asset_data, asset_len, encrypted, offset, data_offset, data_size
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

    def match_hash(self, hash):
        l = min(len(hash), self.name_len)
        return hash[:l] == self.name_hash[:l]

    def load_data(self, handle):
        """ Cache data on the asset. Must be called before extraction."""
        handle.seek(self.data_offset)
        self.data = handle.read(self.data_size)

    def extract(self, dest_path, key, compression_level=DEFAULT_COMPRESSION_LEVEL):
        if self.data is None:
            raise RuntimeError("load_data hasn't been called.")

        self.path = dest_path
        compressed_path = dest_path / ".compressed"
        filepath = self.path / self.filename.decode()
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
                logging.info(f"Storing compressed asset {compressed_filepath}...")
                with compressed_filepath.open("wb") as compressed_file:
                    cctx = zstd.ZstdCompressor(level=compression_level)
                    compressed_data = cctx.compress(self.data)
                    compressed_file.write(compressed_data)

            except Exception as exc:
                logging.error(exc)
                return None


        if filepath.suffix == ".png":
            width, height = unpack(b"<II", self.data[:8])
            image = Image.frombytes("RGBA", (width, height), self.data[8:], "raw")
            new_data = io.BytesIO()
            image.save(new_data, format="PNG")
            self.data = new_data.getvalue()

        # Get a hash of the the uncompressed file to be used
        # to detect if the source file changed
        md5sum = hashlib.md5(self.data).hexdigest()
        with md5sum_filepath.open("w") as md5sum_file:
            md5sum_file.write(md5sum)

        logging.info(f"Storing asset {filepath}...")
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
                logging.info(f"Encrypting file {asset.asset_data.filename}")
                data = chacha(asset.filename, data, self.key)

            logging.info(f"Packing file {asset.asset_data.filename}")
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
            asset_store._key.update(asset_len)

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

    def repackage(self, mods_dir, compression_level=DEFAULT_COMPRESSION_LEVEL):
        self.populate_asset_names()

        offset = self.DATA_OFFSET
        for asset in self.assets:
            if asset.filename is None:
                continue
            asset_data = AssetData.from_filename(mods_dir, asset.filename.decode(), asset.encrypted)
            if asset_data is None:
                raise MissingAsset(asset.filename.decode())
            if asset_data.needs_compression():
                asset_data.compress(compression_level)
            asset.asset_data = asset_data

            asset.offset = offset
            asset.data_size = asset_data.get_data_size()
            asset.data_offset = asset.offset + 8 + asset.name_len + 1

            # The name hash of soundbank files is padded such that the data_offset is divisible by 32
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


@dataclass
class AssetData:
    path: Path
    filename: str
    encrypted: bool

    def md5sum_of_file(self):
        with self.file_path.open("rb") as file_:
            md5sum = hashlib.md5()
            chunk = file_.read(8192)
            while chunk:
                md5sum.update(chunk)
                chunk = file_.read(8192)
            return md5sum.hexdigest().encode()

    @classmethod
    def from_filename(cls, mods_dir, filename, encrypted):
        for path in [OVERRIDES_DIR, EXTRACTED_DIR]:
            path = mods_dir / path
            file_path = path / filename
            if not file_path.exists():
                continue
            return cls(path, filename, encrypted)

    @property
    def file_path(self):
        return self.path / self.filename

    @property
    def compressed_name(self):
        return f"{self.filename}.zst"

    @property
    def compressed_path(self):
        return self.path / ".compressed" / self.compressed_name

    @property
    def md5sum_name(self):
        return f"{self.filename}.md5sum"

    @property
    def md5sum_path(self):
        return self.path / ".compressed" / self.md5sum_name

    def needs_compression(self):
        if not self.encrypted:
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
        if not self.encrypted:
            return

        if self.file_path.suffix == ".png":
            logging.info(f'Converting image "{self.filename}" to RGBA array')
            with Image.open(self.file_path) as img:
                img = img.convert("RGBA")
                data = pack("<II", img.width, img.height) + bytes(
                    (
                        byte if rgba[3] != 0 else 0
                    )  # Hack to force all transparent pixels to be (0, 0, 0, 0) instead of (255, 255, 255, 0)
                    for rgba in img.getdata()
                    for byte in rgba
                )
        else:
            with open(self.file_path, "rb") as f:
                data = f.read()

        md5sum = self.md5sum_of_file()
        with self.md5sum_path.open("wb") as md5sum_file:
            md5sum_file.write(md5sum)

        logging.info(f"Compressing {self.filename}...")
        cctx = zstd.ZstdCompressor(level=compression_level)
        data = cctx.compress(data)
        with open(self.compressed_path, "wb") as compressed_file:
            compressed_file.write(data)

    def get_data_size(self):
        if self.encrypted:
            path = self.compressed_path
        else:
            path = self.file_path
        return path.stat().st_size

    def get_data(self):
        if self.encrypted:
            path = self.compressed_path
        else:
            path = self.file_path

        with path.open("rb") as file_:
            return file_.read()
