import binascii
import os.path

from .assets import KNOWN_ASSETS, AssetStore

EXTRACT_DIR = b"Extracted"


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Extract Spelunky 2 Assets.")
    parser.add_argument(
        "--lazy", default=False, action="store_true",
        help="Whether to be lazy when rebuilding and only extract files that don't exist."
    )
    parser.add_argument("exe", type=argparse.FileType("rb"), help="Path to Spel2.exe")

    args = parser.parse_args()

    asset_store = AssetStore.load_from_file(args.exe)
    seen = {}

    for filename in KNOWN_ASSETS:
        asset = asset_store.find_asset(filename)
        name_hash = asset_store.filename_hash(filename)
        if asset is None:
            print("Asset {} not found with hash {!r}...".format(
                filename.decode(),
                binascii.hexlify(name_hash)
            ))
            continue

        asset.filename = filename
        seen[asset.name_hash] = asset

        dest_path = os.path.join(EXTRACT_DIR, filename)
        dirname = os.path.dirname(dest_path)
        if dirname != "" and not os.path.exists(dirname):
            os.makedirs(dirname)

        if args.lazy and os.path.exists(dest_path):
            print("{} already exists. Skipping... ".format(filename.decode()))
            continue

        print("Extracting {}... ".format(filename.decode()), end="")
        data = asset.extract(filename, args.exe, asset_store.key)
        if not data:
            continue
        with open(dest_path, "wb") as f:
            f.write(data)
        print("Done!")

    for asset in sorted(asset_store.assets, key=lambda a: a.offset):
        name_hash = asset_store.filename_hash(asset.filename)
        if asset.name_hash not in seen:
            print("Un-extracted Asset", asset)
