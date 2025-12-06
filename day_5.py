import argparse
from get_input import get_input
import re

def day_num() -> int:
    return int(re.search(r'.*day_([0-9]*)\.py', __file__).group(1))

day: int = day_num()

def fresh(ingredient_id, ranges):
    for range in ranges:
        if range[0] <= ingredient_id <= range[1]:
            return True
    return False

def merge(ranges):
    merged_ranges = []
    sorted_ranges = sorted(ranges)
    curr_start, curr_end = sorted_ranges[0]
    for range in sorted_ranges[1:]:
        if range[0] > curr_end:
            merged_ranges.append((curr_start, curr_end))
            curr_start = range[0]
            curr_end = range[1]
        if range[1] > curr_end:
            curr_end = range[1]
    merged_ranges.append((curr_start, curr_end))
    return merged_ranges


def run(test: bool) -> None:
    if not test:
        raw_input: str = get_input(day)
    else:
        raw_input: str = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
        """.strip()

    raw_ranges, raw_ingredient_ids = raw_input.strip().split('\n\n')
    ranges = [tuple(map(int, raw_range.strip().split('-'))) for raw_range in raw_ranges.strip().split('\n')]
    ingredient_ids = list(map(int, raw_ingredient_ids.strip().split('\n')))

    # part 1
    count = 0
    for ingredient_id in ingredient_ids:
        count += fresh(ingredient_id, ranges)
    print(count)

    # part 2
    merged_ranges = merge(ranges)
    count = 0
    for range in merged_ranges:
        count += range[1] - range[0] + 1
    print(count)

if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args: argparse.Namespace = parser.parse_args()
    run(args.test)
