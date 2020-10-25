from PIL import Image
from struct import pack
import os
from pathlib import Path

from .assets import AssetStore, MissingAsset
from .patcher import Patcher


def main():
    import argparse
    import sys
    import shutil

    parser = argparse.ArgumentParser(description="Extract Spelunky 2 Assets.")

    parser.add_argument(
        "--mods-dir",
        type=str,
        default="Mods",
        help="Path to directory containing mods.",
    )
    parser.add_argument(
        "--compression-level",
        type=int,
        default=16,
        help=(
            " Value between 1 and 22 (higher = smaller data size)"
            " - if modified assets are too large, increase compression"
        ),
    )
    parser.add_argument(
        "source",
        type=argparse.FileType("rb"),
        help="Path to original Spel2.exe. This should be used as a source and not ever patched.",
    )
    parser.add_argument(
        "dest",
        type=str,
        default="Spel2-modded.exe",
        help="Path where patched binary will be created.",
    )
    args = parser.parse_args()

    if os.path.exists(args.dest):
        answer = input(
            f"File {args.dest} already exists. Would you like to overwrite it? [y/N]: "
        )
        if answer.lower() not in ("y", "yes"):
            print("Exiting...")
            sys.exit(0)

    print(f"Making copy of {args.source.name} to {args.dest}")
    shutil.copy2(args.source.name, args.dest)

    with open(args.dest, "rb+") as dest_file:
        asset_store = AssetStore.load_from_file(dest_file)
        try:
            asset_store.repackage(Path(args.mods_dir), args.compression_level)
        except MissingAsset as err:
            print("")
            print(f"Failed to find expected asset: {err}. Unabled to proceed...")
            print("Did you run s2-asset-extract in this directory?")
            print("")
            sys.exit(1)

        patcher = Patcher(dest_file)
        patcher.patch()


if __name__ == "__main__":
    main()