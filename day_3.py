import argparse
from get_input import get_input
import re

def day_num() -> int:
    return int(re.search(r'.*day_([0-9]*)\.py', __file__).group(1))

day: int = day_num()

def get_joltage(bank, N):
    result = []
    idx = 0
    last_idx = len(bank) - N + len(result) + 1
    while len(result) < N:
        idx += bank[idx:last_idx].index(max(bank[idx:last_idx]))
        result.append(bank[idx])
        last_idx = len(bank) - N + len(result) + 1
        idx += 1
    return int(''.join(result))


def run(test: bool) -> None:
    if not test:
        raw_input: str = get_input(day)
    else:
        raw_input: str = """
987654321111111
811111111111119
234234234234278
818181911112111
        """.strip()

    # part 1
    banks = raw_input.strip().split('\n')
    s = 0
    for bank in banks:
        s += get_joltage(bank, 2)
    print(s)

    # part 2
    s = 0
    for bank in banks:
        s += get_joltage(bank, 12)
    print(s)

if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args: argparse.Namespace = parser.parse_args()
    run(args.test)
