from PIL import Image
from struct import pack
import os

from .assets import AssetStore

KEEP_CONVERTED_RAW_IMAGES = False  # Keep .png.raw files with RGBA array after conversion (for debug purposes only)
DEBUG_LIST_ASSETS = (
    False  # Lists all asset offsets while scanning the original game binary
)


# * Copy the original Spel2.exe and name it Spel2-orig.exe
# * Create a folder Mod and put any assets in there that you want to replace
#   (with the same folder structure inside, e.g. Data/Textures/). You don't
#   need to (and shouldn't) put any unmodified assets in there.
#   Textures (.png files) are read from the Mod folder as actual PNG files,
#   you do not need to convert them into raw RGBA arrays.
# * Run spelunky2_mod.py, it will create Spel2-modded.exe that contains the
#   modified assets and has the asset checksum patched out.
# * Replace your Spel2.exe with Spel2-modded.exe and run the game.
#
# Currently each modified asset has to be the same size or smaller than the
# original asset for this to work. This shouldn't be a problem, since the assets
# are stored compressed and you can just up the compression factor. It's set to
# 16 in the script, which is already higher than the one used originally, but
# you can increase it up to 22 if your assets are too big.


# Patch out checksum check for asset loading
#
# This is the code that validates the checksum and calls exit() when it doesn't match:
#                   /------------------------------------------\
# cmp rax,rcx  jz -/   xor ecx,ecx  call cs:exit        int 3   \-> mov rcx,[rbp+17h]
# 48 3B C1     74 09   33 C9        FF ?? ?? ?? ?? ??   CC          48 8B 4D 17
# 48 3B C1     74 09   90 90        90 90 90 90 90 90   90
#                      [               nop               ]
# We overwrite the exit() call with NOPs
PATCH_START = b"\x48\x3B\xC1\x74\x09\x33\xC9\xFF"
PATCH_END = 0xCC
PATCH_REPLACE = b"\x48\x3B\xC1\x74\x09" + b"\x90" * 9


class Patcher:
    def __init__(self, exe_handle):
        self.exe_handle = exe_handle

    def find(self, needle, offset=0, bsize=4096):
        if bsize < len(needle):
            raise ValueError(
                "The buffer size must be larger than the string being searched for."
            )

        self.exe_handle.seek(offset)
        overlap = len(needle) - 1
        while True:
            buffer = self.exe_handle.read(bsize)
            pos = buffer.find(needle)
            if pos >= 0:
                return self.exe_handle.tell() - len(buffer) + pos
            if not buffer:
                return -1
            self.exe_handle.seek(self.exe_handle.tell() - overlap)

    def patch(self):
        print("Patching asset checksum check")
        index = self.find(PATCH_START)
        if index == -1:
            print("Didn't find instructions to patch. Is game unmodified?")
            return False

        self.exe_handle.seek(index)
        ops = self.exe_handle.read(14)
        print(repr(ops))

        if ops[-1] != PATCH_END:
            print(
                "Checksum check has unexpected form, this script has to be updated for the current game version."
            )
            print("(Expected 0x{:02x}, found 0x{:02x})".format(PATCH_END, ops[-1]))
            return False

        print("Found check at 0x{:08x}, replacing with NOPs".format(index))
        self.exe_handle.seek(index)
        self.exe_handle.write(PATCH_REPLACE)


def main():
    import argparse
    import sys
    import shutil

    parser = argparse.ArgumentParser(description="Extract Spelunky 2 Assets.")

    parser.add_argument(
        "--asset-dir",
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


    source_asset_store = AssetStore.load_from_file(args.source)

    with open(args.dest, "rb+") as dest_file:

        dest_asset_store = AssetStore.load_from_directory(args.asset_dir, dest_file)

        if dest_asset_store.total_size > source_asset_store.total_size:
            print("New asset bundle larger than previous... Failing.")
            sys.exit(1)

        dest_asset_store.pack_assets(args.asset_dir)
        patcher = Patcher(dest_file)
        patcher.patch()


if __name__ == "__main__":
    main()
