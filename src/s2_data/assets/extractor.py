from struct import pack, unpack
from PIL import Image
import io
import os
import os.path

from .chacha import decrypt_data, filename_hash
from .assets import KNOWN_ASSETS


EXTRACT_DIR = b"extracted"

class AssetDetails(object):
    def __init__(self, filename, hashed_name, encrypted, offset, size):
        self.filename = filename
        self.hashed_name = hashed_name
        self.encrypted = encrypted
        self.offset = offset
        self.size = size

    def __repr__(self):
        return "AssetDetails(filename={}, encrypted={}, offset={}, size={})".format(
            self.filename, self.encrypted, hex(self.offset), self.size,
        )

    def extract(self, handle):
        handle.seek(self.offset)
        data = handle.read(self.size)
        if self.encrypted:
            try:
                data = decrypt_data(self.filename, data)
            except Exception as exc:
                print(exc)
                return None

        if self.filename.endswith(b".png"):
            width, height = unpack(b'<II', data[:8])
            image = Image.frombytes('RGBA', (width, height), data, 'raw')
            new_data = io.BytesIO()
            image.save(new_data, format="PNG")
            data = new_data.getvalue()

        return data


class Extractor(object):
    def __init__(self, exe_handle):
        self.exe_handle = exe_handle

        self.asset_hashes = {}
        for asset in KNOWN_ASSETS:
            self.asset_hashes[filename_hash(asset)] = asset

    def get_filename(self, hashed_name):
        filename = self.asset_hashes.get(hashed_name)
        if filename:
            return filename

        hashed_len = len(hashed_name)
        for key in self.asset_hashes:
            min_len = min(hashed_len, len(key))
            if hashed_name[:min_len] == key[:min_len]:
                return self.asset_hashes[key]

        return None

    def extract_asset_details(self, offset=0x400):
        self.exe_handle.seek(offset)

        while True:
            asset_len, name_len = unpack(b'<II', self.exe_handle.read(8))
            if (asset_len, name_len) == (0, 0):
                break
            assert asset_len > 0

            hashed_name = self.exe_handle.read(name_len)
            # Remove NULL byte
            hashed_name = hashed_name[:-1]
            encrypted = self.exe_handle.read(1) == b'\x01'
            offset = self.exe_handle.tell()
            size = asset_len - 1

            self.exe_handle.seek(size, 1)

            filename = self.get_filename(hashed_name)
            if not filename:
                print("Unknown hash. Skipping...")
                continue

            yield AssetDetails(
                filename=filename,
                hashed_name=hashed_name,
                encrypted=encrypted,
                offset=offset,
                size=size,
            )


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Extract Spelunky 2 Assets.')

    parser.add_argument(
        'exe', type=argparse.FileType('rb'),
        help="Path to Spel2.exe"
    )
    args = parser.parse_args()

    extractor = Extractor(args.exe)
    for asset in extractor.extract_asset_details():
        dest_path = os.path.join(EXTRACT_DIR, asset.filename)
        dirname = os.path.dirname(dest_path)
        if dirname != "" and not os.path.exists(dirname):
            os.makedirs(dirname)

        if os.path.exists(dest_path):
            print("{} alread exists. Skipping... ".format(asset.filename.decode()))
            continue

        print("Extracting {}... ".format(asset.filename.decode()), end="")
        data = asset.extract(args.exe)
        if not data:
            continue
        with open(dest_path, "wb") as f:
            f.write(data)
        print("Done!")
