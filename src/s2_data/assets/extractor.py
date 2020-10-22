import os.path

from .assets import KNOWN_ASSETS, AssetStore
from .chacha import filename_hash

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

    asset_store = AssetStore(args.exe)
    seen = {}

    for idx, filename in enumerate(KNOWN_ASSETS):
        asset = asset_store.find_asset(filename)
        if asset is None:
            print("Asset {} not found with hash {}...".format(filename.decode(), repr(filename_hash(filename, asset_store.key.key))))
            continue

        seen[asset.name_hash] = (filename, asset)

        dest_path = os.path.join(EXTRACT_DIR, filename)
        dirname = os.path.dirname(dest_path)
        if dirname != "" and not os.path.exists(dirname):
            os.makedirs(dirname)

        if args.lazy and os.path.exists(dest_path):
            print("{} already exists. Skipping... ".format(filename.decode()))
            continue

        print("Extracting {}... ".format(filename.decode()), end="")
        data = asset.extract(filename, args.exe, asset_store.key.key)
        if not data:
            continue
        with open(dest_path, "wb") as f:
            f.write(data)
        print("Done!")

    for idx, asset in enumerate(sorted(asset_store.assets, key=lambda a: a.offset)):
#        #print(seen.get(asset.name_hash, (None, None)))
        if asset.name_hash not in seen:
            print("Un-extracted Asset", asset)
#            print("Before:", seen.get(asset_store.assets[idx-1].name_hash))
#            print("After:", seen.get(asset_store.assets[idx+1].name_hash))
#            print("")