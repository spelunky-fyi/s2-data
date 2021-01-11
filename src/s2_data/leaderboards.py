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
class Score:
    id: int = None
    name: str = None
    platform: int = None
    character: int = None
    frames: int = None
    ending: int = None
    score: int = None
    level: int = None
    block7: bytes = None
    block8: bytes = None


def get_scores(compressed_data_handle):

    scores = []

    dctx = zstandard.ZstdDecompressor()
    with dctx.stream_reader(compressed_data_handle) as reader:

        # We skip the first two entries for each array as they're always empty
        num_scores = int.from_bytes(reader.read(8), "little") - 2

        for _ in range(num_scores):
            scores.append(Score())

        reader.seek(ID_POSITION + 2 * 8)
        for idx in range(num_scores):
            scores[idx].id = int.from_bytes(reader.read(8), "little")

        reader.seek(NAMES_POSITION + 2 * NAME_LENGTH)
        for idx in range(num_scores):
            scores[idx].name = (
                reader.read(NAME_LENGTH).partition(b"\x00")[0].decode("utf-8")
            )

        reader.seek(META_POSITION + 2 * 2)
        for idx in range(num_scores):
            scores[idx].platform = int.from_bytes(reader.read(1), "little")
            scores[idx].character = int.from_bytes(reader.read(1), "little")

        reader.seek(RUNDATA_POSITION + 2 * 8)
        for idx in range(num_scores):
            scores[idx].frames = int.from_bytes(reader.read(4), "little")
            scores[idx].ending = int.from_bytes(reader.read(4), "little")

        reader.seek(SCORES_POSITION + 2 * 8)
        for idx in range(num_scores):
            scores[idx].score = int.from_bytes(reader.read(4), "little")
            scores[idx].level = int.from_bytes(reader.read(4), "little")

        reader.seek(BLOCK6_POSITION + 2 * 4)
        for idx in range(num_scores):
            scores[idx].block7 = reader.read(4)

        reader.seek(BLOCK7_POSITION + 2 * 4)
        for idx in range(num_scores):
            scores[idx].block8 = reader.read(4)

    return scores


def main():
    import sys

    with open(sys.argv[1], "rb") as fh:
        for score in get_scores(fh):
            print(score)
