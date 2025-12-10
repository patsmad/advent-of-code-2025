import argparse
from get_input import get_input
import re

def day_num() -> int:
    return int(re.search(r'.*day_([0-9]*)\.py', __file__).group(1))

day: int = day_num()

def get_distances(points):
    d = {}
    for idx in range(len(points)):
        for idy in range(idx + 1, len(points)):
            x1, y1, z1 = points[idx]
            x2, y2, z2 = points[idy]
            d[(idx, idy)] = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
    return d

def get_root(point_to_component, p):
    curr_p = p
    parent = point_to_component[curr_p]
    while parent != -1:
        curr_p = parent
        parent = point_to_component[curr_p]
    return curr_p

def run(test: bool) -> None:
    if not test:
        raw_input: str = get_input(day)
        N = 1000
    else:
        raw_input: str = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
        """.strip()
        N = 10

    points = [[int(c) for c in row.strip().split(',')] for row in raw_input.strip().split('\n')]

    # part 1
    distances = get_distances(points)
    sorted_idxs = sorted(distances, key=lambda x: distances[x])
    point_to_component = {idx: -1 for idx in range(len(points))}
    for i in range(N):
        p1, p2 = sorted_idxs[i]
        root_1 = get_root(point_to_component, p1)
        root_2 = get_root(point_to_component, p2)
        if root_1 < root_2:
            point_to_component[root_2] = root_1
        elif root_2 < root_1:
            point_to_component[root_1] = root_2

    roots = [get_root(point_to_component, idx) for idx in range(len(points))]
    counts = {}
    for r in roots:
        if r not in counts:
            counts[r] = 0
        counts[r] += 1
    p = 1
    for c in sorted(counts.values())[-3:]:
        p *= c
    print(p)

    # part 2
    point_to_component = {idx: -1 for idx in range(len(points))}
    i = 0
    while len([k for k, v in point_to_component.items() if v == -1]) > 1:
        p1, p2 = sorted_idxs[i]
        root_1 = get_root(point_to_component, p1)
        root_2 = get_root(point_to_component, p2)
        if root_1 < root_2:
            point_to_component[root_2] = root_1
        elif root_2 < root_1:
            point_to_component[root_1] = root_2
        i += 1
    print(points[p1][0] * points[p2][0])


if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args: argparse.Namespace = parser.parse_args()
    run(args.test)
