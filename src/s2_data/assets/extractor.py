import binascii
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import logging

from .assets import KNOWN_ASSETS, AssetStore, EXTRACTED_DIR, OVERRIDES_DIR

DEFAULT_DIR = Path("Mods")
EXTRACTED_DIR = DEFAULT_DIR / EXTRACTED_DIR
OVERRIDES_DIR = DEFAULT_DIR / OVERRIDES_DIR

DIRS = [
    "Data/Fonts",
    "Data/Levels/Arena",
    "Data/Textures/OldTextures"
]


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Extract Spelunky 2 Assets.")
    parser.add_argument("exe", type=argparse.FileType("rb"), help="Path to Spel2.exe")

    args = parser.parse_args()

    logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.INFO)

    asset_store = AssetStore.load_from_file(args.exe)
    seen = {}

    # Make all directories for extraction and overrides
    for dir_ in DIRS:
        (EXTRACTED_DIR / dir_).mkdir(parents=True, exist_ok=True)
        (EXTRACTED_DIR / ".compressed" / dir_).mkdir(parents=True, exist_ok=True)
        (OVERRIDES_DIR / dir_).mkdir(parents=True, exist_ok=True)
        (OVERRIDES_DIR / ".compressed" / dir_).mkdir(parents=True, exist_ok=True)

    for filename in KNOWN_ASSETS:
        asset = asset_store.find_asset(filename)
        name_hash = asset_store.filename_hash(filename)
        if asset is None:
            logging.warning("Asset %s not found with hash %s...",
                filename.decode(),
                binascii.hexlify(name_hash)
            )
            continue

        asset.filename = filename
        seen[asset.name_hash] = asset

        filepath = Path(filename.decode())
        asset.load_data(args.exe)

    def extract_single(asset):
        try:
            logging.info("Extracting %s... ", asset.filename.decode())
            asset.extract(EXTRACTED_DIR, asset_store.key)
        except Exception as err:
            logging.error(err)

    pool = ThreadPoolExecutor()
    pool.map(extract_single, seen.values())

    for asset in sorted(asset_store.assets, key=lambda a: a.offset):
        name_hash = asset_store.filename_hash(asset.filename)
        if asset.name_hash not in seen:
            logging.warning("Un-extracted Asset %s", asset)


if __name__ == '__main__':
    main()
