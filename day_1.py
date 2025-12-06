import argparse
from get_input import get_input
import re

def day_num() -> int:
    return int(re.search(r'.*day_([0-9]*)\.py', __file__).group(1))

day: int = day_num()

def run(test: bool) -> None:
    if not test:
        raw_input: str = get_input(day)
    else:
        raw_input: str = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
        """.strip()

    # part 1
    instructions = raw_input.split('\n')

    dial = 50
    count = 0
    for instruction in instructions:
        if instruction[0] == 'L':
            dial = (dial - int(instruction[1:])) % 100
        else:
            dial = (dial + int(instruction[1:])) % 100
        if dial == 0:
            count += 1
    print(count)

    # part 2
    dial = 50
    count = 0
    for instruction in instructions:
        if instruction[0] == 'L':
            tmp_dial = (-dial % 100) + int(instruction[1:])
            count += tmp_dial // 100
            dial = -tmp_dial % 100
        else:
            tmp_dial = dial + int(instruction[1:])
            count += tmp_dial // 100
            dial = tmp_dial % 100

    print(count)

if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args: argparse.Namespace = parser.parse_args()
    run(args.test)
