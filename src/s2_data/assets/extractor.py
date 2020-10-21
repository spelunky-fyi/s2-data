import os.path

from .assets import KNOWN_ASSETS, AssetStore

EXTRACT_DIR = b"Extracted"


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Extract Spelunky 2 Assets.")

    parser.add_argument("exe", type=argparse.FileType("rb"), help="Path to Spel2.exe")
    args = parser.parse_args()

    asset_store = AssetStore(args.exe)

    for filename in KNOWN_ASSETS:
        asset = asset_store.find_asset(filename)
        if asset is None:
            print("Asset {} not found...".format(filename.decode()))
            continue

        dest_path = os.path.join(EXTRACT_DIR, filename)
        dirname = os.path.dirname(dest_path)
        if dirname != "" and not os.path.exists(dirname):
            os.makedirs(dirname)

        if os.path.exists(dest_path):
            print("{} already exists. Skipping... ".format(filename.decode()))
            continue

        print("Extracting {}... ".format(filename.decode()), end="")
        data = asset.extract(filename, args.exe, asset_store.key.key)
        if not data:
            continue
        with open(dest_path, "wb") as f:
            f.write(data)
        print("Done!")