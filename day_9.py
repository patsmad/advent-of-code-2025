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

def get_points(tiles):
    points = []
    xs, ys = sorted(set([tile[0] for tile in tiles])), sorted(set([tile[1] for tile in tiles]))
    for idx in range(len(xs) - 1):
        for idy in range(len(ys) - 1):
            points.append(((xs[idx] + xs[idx + 1]) / 2, (ys[idy] + ys[idy + 1]) / 2))
    return points

def assign_points(points, lines):
    in_points, out_points = [], []
    for point in points:
        num = 0
        for line in lines:
            if (line[0][0] == line[1][0] and
                    point[0] > line[0][0] and
                    (line[0][1] <= point[1] <= line[1][1] or line[1][1] <= point[1] <= line[0][1])):
                num += 1
        if num % 2 == 0:
            out_points.append(point)
        else:
            in_points.append(point)
    return in_points, out_points

def no_points(x1, y1, x2, y2, points):
    for point in points:
        if x1 <= point[0] <= x2 and y1 <= point[1] <= y2:
            return False
    return True

def get_largest_in_pair(tiles, sizes, in_points, out_points):
    for idx, idy in sorted(sizes, key=lambda x: -sizes[x]):
        x1, y1 = tiles[idx]
        x2, y2 = tiles[idy]
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        if no_points(x1, y1, x2, y2, out_points):
            return sizes[idx, idy]


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
    lines = [(tiles[idx], tiles[idx + 1]) for idx in range(len(tiles) - 1)] + [(tiles[-1], tiles[0])]
    points = get_points(tiles)
    in_points, out_points = assign_points(points, lines)
    print(get_largest_in_pair(tiles, sizes, in_points, out_points))


if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args: argparse.Namespace = parser.parse_args()
    run(args.test)
