import argparse
from get_input import get_input
import re

def day_num() -> int:
    return int(re.search(r'.*day_([0-9]*)\.py', __file__).group(1))

day: int = day_num()

def get_value(start, end, N):
    s = set()
    length = max(len(start) // N, len(end) // N) * N
    if len(start) == length or len(end) == length:
        if len(start) == length:
            num = start[:length // N]
            if int(num * N) < int(start):
                num = str(int(num) + 1)
        else:
            num = '1' + '0' * (length // N - 1)
        while int(start) <= int(num * N) <= int(end):
            s |= {int(num * N)}
            num = str(int(num) + 1)
    return s

def run(test: bool) -> None:
    if not test:
        raw_input: str = get_input(day)
    else:
        raw_input: str = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
        """.strip()
    instructions = raw_input.split(',')

    # part 1
    s = 0
    for instruction in instructions:
        start, end = instruction.split('-')
        s += sum(get_value(start, end, 2))
    print(s)

    # part 2
    s = 0
    for instruction in instructions:
        start, end = instruction.split('-')
        curr_s = set()
        for N in range(2, max(len(start), len(end)) + 1):
            curr_s |= get_value(start, end, N)
        s += sum(curr_s)
    print(s)

if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args: argparse.Namespace = parser.parse_args()
    run(args.test)
