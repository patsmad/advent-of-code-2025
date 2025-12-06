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
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
        """.strip()

    lines = [re.sub(r'\s{2,}', ' ', line).split() for line in raw_input.strip().split('\n')]

    # part 1
    count = 0
    for idx in range(len(lines[0])):
        op = lines[-1][idx]
        nums = [int(lines[j][idx]) for j in range(len(lines) - 1)]
        if op == '*':
            ps = 1
            for num in nums:
                ps *= num
        else:
            ps = 0
            for num in nums:
                ps += num
        count += ps
    print(count)

    # part 2
    raw_lines = raw_input.strip().split('\n')
    space_set = {idx for idx, c in enumerate(raw_lines[-1]) if c == ' '}
    for raw_line in raw_lines[:-1]:
        space_set &= {idx for idx, c in enumerate(raw_line) if c == ' '}

    lines = []
    for raw_line in raw_lines:
        line = []
        idx_l = 0
        for idx_r in sorted(space_set):
            line.append(raw_line[idx_l:idx_r])
            idx_l = idx_r + 1
        line.append(raw_line[idx_l:])
        lines.append(line)

    count = 0
    for idx in range(len(lines[0])):
        op = re.sub(r'\s+', '', lines[-1][idx])
        nums = [lines[j][idx] for j in range(len(lines) - 1)]
        ps = 1 if op == '*' else 0
        for j in range(max([len(num) for num in nums])):
            if op == '*':
                ps *= int(''.join([num[j] for num in nums]))
            else:
                ps += int(''.join([num[j] for num in nums]))
        count += ps
    print(count)


if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args: argparse.Namespace = parser.parse_args()
    run(args.test)
