from dataclasses import dataclass
import zstandard


ID_POSITION = 0x0000008
NAMES_POSITION = 0x07A1208
META_POSITION = 0x2719C48
RUNDATA_POSITION = 0x29020C8
SCORES_POSITION = 0x30A32C8
BLOCK6_POSITION = 0x38444C8
BLOCK7_POSITION = 0x3C14DC8

NAME_LENGTH = 33


@dataclass
class Run:
    id: int = None
    name: str = None
    platform: int = None
    character: int = None
    frames: int = None
    ending: int = None
    score: int = None
    level: int = None
    block6: bytes = None
    block7: bytes = None


def get_runs(compressed_data_handle):

    runs = []

    dctx = zstandard.ZstdDecompressor()
    with dctx.stream_reader(compressed_data_handle) as reader:

        # We skip the first two entries for each array as they're always empty
        num_runs = int.from_bytes(reader.read(8), "little") - 2

        for _ in range(num_runs):
            runs.append(Run())

        reader.seek(ID_POSITION + 2 * 8)
        for idx in range(num_runs):
            runs[idx].id = int.from_bytes(reader.read(8), "little")

        reader.seek(NAMES_POSITION + 2 * NAME_LENGTH)
        for idx in range(num_runs):
            data = reader.read(NAME_LENGTH).partition(b"\x00")[0]
            runs[idx].name = data.decode("utf-8", errors="replace")

        reader.seek(META_POSITION + 2 * 2)
        for idx in range(num_runs):
            runs[idx].platform = int.from_bytes(reader.read(1), "little")
            runs[idx].character = int.from_bytes(reader.read(1), "little")

        reader.seek(RUNDATA_POSITION + 2 * 8)
        for idx in range(num_runs):
            runs[idx].frames = int.from_bytes(reader.read(4), "little")
            runs[idx].ending = int.from_bytes(reader.read(4), "little")

        reader.seek(SCORES_POSITION + 2 * 8)
        for idx in range(num_runs):
            runs[idx].score = int.from_bytes(reader.read(4), "little")
            runs[idx].level = int.from_bytes(reader.read(4), "little")

        reader.seek(BLOCK6_POSITION + 2 * 4)
        for idx in range(num_runs):
            runs[idx].block6 = reader.read(4)

        reader.seek(BLOCK7_POSITION + 2 * 4)
        for idx in range(num_runs):
            runs[idx].block7 = reader.read(4)

    return runs


def main():
    import sys

    with open(sys.argv[1], "rb") as fh:
        for score in get_runs(fh):
            print(score)
