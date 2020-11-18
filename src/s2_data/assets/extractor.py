import argparse
import binascii
import logging
from concurrent.futures import ThreadPoolExecutor, wait
from pathlib import Path

from .assets import EXTRACTED_DIR, KNOWN_ASSETS, AssetStore

DEFAULT_MODS_DIR = "Mods"

DIRS = [
    "Data/Fonts",
    "Data/Levels/Arena",
    "Data/Textures/OldTextures"
]


def main():

    parser = argparse.ArgumentParser(description="Extract Spelunky 2 Assets.")
    parser.add_argument("exe", type=argparse.FileType("rb"), help="Path to Spel2.exe")
    parser.add_argument("--mods-dir", default=DEFAULT_MODS_DIR)

    args = parser.parse_args()

    mods_dir = Path(args.mods_dir)

    logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.INFO)

    asset_store = AssetStore.load_from_file(args.exe)
    seen = {}

    # Make all directories for extraction and overrides
    (mods_dir / "Packs").mkdir(parents=True, exist_ok=True)
    (mods_dir / "Overrides").mkdir(parents=True, exist_ok=True)
    for dir_ in DIRS:
        (mods_dir / EXTRACTED_DIR / dir_).mkdir(parents=True, exist_ok=True)
        (mods_dir / ".compressed" / EXTRACTED_DIR / dir_).mkdir(parents=True, exist_ok=True)

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

        Path(filename.decode())
        asset.load_data(args.exe)

    def extract_single(asset):
        try:
            logging.info("Extracting %s... ", asset.filename.decode())
            asset.extract(mods_dir, EXTRACTED_DIR, asset_store.key)
        except Exception:
            logging.exception("Failed Extraction")

    pool = ThreadPoolExecutor()
    futures = [pool.submit(extract_single, asset) for asset in seen.values()]
    wait(futures, timeout=300)
    #for asset in seen.values():
    #    extract_single(asset)

    for asset in sorted(asset_store.assets, key=lambda a: a.offset):
        name_hash = asset_store.filename_hash(asset.filename)
        if asset.name_hash not in seen:
            logging.warning("Un-extracted Asset %s", asset)


if __name__ == '__main__':
    main()
