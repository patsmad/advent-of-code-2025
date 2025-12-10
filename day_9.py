import argparse
from get_input import get_input
import re

def day_num() -> int:
    return int(re.search(r'.*day_([0-9]*)\.py', __file__).group(1))

day: int = day_num()

def get_sizes(tiles):
    s = {}
    for idx in range(len(tiles)):
        for idy in range(idx + 1, len(tiles)):
            x1, y1 = tiles[idx]
            x2, y2 = tiles[idy]
            s[(idx, idy)] = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    return s

def run(test: bool) -> None:
    if not test:
        raw_input: str = get_input(day)
    else:
        raw_input: str = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
        """.strip()

    tiles = [list(map(int, line.strip().split(','))) for line in raw_input.strip().split('\n')]

    # part 1
    sizes = get_sizes(tiles)
    print(max(sizes.values()))

    # part 2


if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args: argparse.Namespace = parser.parse_args()
    run(args.test)
