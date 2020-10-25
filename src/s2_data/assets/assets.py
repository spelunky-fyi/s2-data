from struct import pack, unpack
from PIL import Image
import binascii
import io
import os.path
import zstandard as zstd

from .chacha import Key, filename_hash, chacha
from .known_assets import KNOWN_ASSETS

UNENCRYPTED_ASSETS = set([
    "soundbank.bank", "soundbank.strings.bank",
])

class Asset(object):
    def __init__(
        self, name_hash, name_len, filename, asset_len, encrypted, offset, data_offset, data_size
    ):
        self.name_hash = name_hash
        self.name_len = name_len
        self.filename = filename
        self.asset_len = asset_len
        self.encrypted = encrypted
        self.offset = offset
        self.data_offset = data_offset
        self.data_size = data_size

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

    def extract(self, filename, handle, key):
        handle.seek(self.data_offset)
        data = handle.read(self.data_size)
        if self.encrypted:
            try:
                data = chacha(filename, data, key)
                cctx = zstd.ZstdDecompressor()
                data = cctx.decompress(data)
            except Exception as exc:
                print(exc)
                return None

        if filename.endswith(b".png"):
            width, height = unpack(b"<II", data[:8])
            image = Image.frombytes("RGBA", (width, height), data[8:], "raw")
            new_data = io.BytesIO()
            image.save(new_data, format="PNG")
            data = new_data.getvalue()

        return data


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
            new_key.update(asset.asset_len)
        self._key = new_key

    def rehash_all_files(self):
        for asset in self.assets:
            if asset.filename is None:
                continue
            asset.name_hash = self.filename_hash(asset.filename)

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

    def pack_assets(self, asset_dir):
        self.exe_handle.seek(self.DATA_OFFSET)

        for asset in self.assets:
            asset_path = os.path.join(asset_dir.encode(), asset.filename)

            if asset.encrypted:
                asset_path += b".zst"

            data_size = os.path.getsize(asset_path)
            assert data_size == asset.data_size

            with open(asset_path, "rb") as asset_datefile:
                data = asset_datefile.read()

            if asset.encrypted:
                data = chacha(asset.filename, data, self.key)

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
                asset_len=asset_len,
                encrypted=encrypted,
                offset=offset,
                data_offset=data_offset,
                data_size=data_size,
            )
            asset_store.assets.append(asset)
            asset_store.total_size += asset.total_size

        return asset_store

    @classmethod
    def load_from_directory(cls, asset_dir, exe_handle, compression_level=20):
        asset_store = cls(exe_handle)
        offset = cls.DATA_OFFSET

        for dir_, _, files in os.walk(asset_dir):
            for file_ in files:
                filepath = os.path.join(dir_, file_)
                filename = filepath.replace(asset_dir, "").replace("\\", "/")[1:]
                compressed_name = f"{filepath}.zst"
                encrypted = filename not in UNENCRYPTED_ASSETS

                # Skip files that are compressed
                if filename.endswith(".zst"):
                    continue  # skip converted images

                if filename.endswith(".png") and not os.path.exists(compressed_name):
                    print('\nConverting image "{}" to RGBA array'.format(filename))
                    img = Image.open(filepath).convert("RGBA")
                    data = pack("<II", img.width, img.height) + bytes(
                        (
                            byte if rgba[3] != 0 else 0
                        )  # Hack to force all transparent pixels to be (0, 0, 0, 0) instead of (255, 255, 255, 0)
                        for rgba in img.getdata()
                        for byte in rgba
                    )
                else:
                    with open(filepath, "rb") as f:
                        data = f.read()

                data_size = len(data)

                if encrypted:
                    if os.path.exists(compressed_name):
                        data_size = os.path.getsize(compressed_name)
                    else:
                        print(f"Compressing {filepath}...")
                        cctx = zstd.ZstdCompressor(level=compression_level)
                        data = cctx.compress(data)
                        data_size = len(data)
                        with open(compressed_name, "wb") as f:
                            f.write(data)

                data_offset = offset + 8 + len(filename) + 1
                asset_len = data_size + 1

                filename = filename.encode()
                asset = Asset(
                    name_hash=None,
                    name_len=len(filename),
                    filename=filename,
                    asset_len=asset_len,
                    encrypted=encrypted,
                    offset=offset,
                    data_offset=data_offset,
                    data_size=data_size,
                )
                asset_store.assets.append(asset)
                asset_store.total_size += asset.total_size
                offset += asset.total_size

        asset_store.recalculate_key()
        asset_store.rehash_all_files()
        return asset_store




