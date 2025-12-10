import argparse
from get_input import get_input
import re

def day_num() -> int:
    return int(re.search(r'.*day_([0-9]*)\.py', __file__).group(1))

day: int = day_num()

class Node:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.edges = []

def run(test: bool) -> None:
    if not test:
        raw_input: str = get_input(day)
    else:
        raw_input: str = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
        """.strip()

    # part 1
    lines = [[c for c in line] for line in raw_input.strip().split('\n')]
    nodes = {}
    for idx in range(len(lines[0])):
        if lines[0][idx] == 'S':
            nodes[(0, idx)] = Node(0, idx, 'S')
    curr_line = lines[0]
    for i, line in enumerate(lines[1:]):
        for idx in range(len(line)):
            if curr_line[idx] in ['|', 'S'] and line[idx] != '^':
                line[idx] = '|'
                if (i + 1, idx) not in nodes:
                    nodes[(i + 1, idx)] = Node(i + 1, idx, '|')
                nodes[(i, idx)].edges.append(nodes[(i + 1, idx)])
            elif line[idx] == '^' and curr_line[idx] == '|':
                nodes[(i + 1, idx)] = Node(i + 1, idx, '^')
                nodes[(i, idx)].edges.append(nodes[(i + 1, idx)])
                line[idx - 1] = '|'
                if (i + 1, idx - 1) not in nodes:
                    nodes[(i + 1, idx - 1)] = Node(i + 1, idx - 1, '|')
                nodes[(i + 1, idx)].edges.append(nodes[(i + 1, idx - 1)])
                line[idx + 1] = '|'
                if (i + 1, idx + 1) not in nodes:
                    nodes[(i + 1, idx + 1)] = Node(i + 1, idx + 1, '|')
                nodes[(i + 1, idx)].edges.append(nodes[(i + 1, idx + 1)])
        curr_line = line
    nodes[(len(lines), 0)] = Node(len(lines), 0, 'E')
    for idx in range(len(lines[-1])):
        if (len(lines) - 1, idx) in nodes and nodes[(len(lines) - 1, idx)].symbol == '|':
            nodes[(len(lines) - 1, idx)].edges.append(nodes[(len(lines), 0)])
    print(len([n for n in nodes.values() if n.symbol == '^']))

    # part 2
    count = {}
    count[len(lines), 0] = 1
    while len(count) < len(nodes):
        for node in nodes.values():
            if len(node.edges) > 0 and all([(edge.x, edge.y) in count for edge in node.edges]):
                count[(node.x, node.y)] = sum([count[edge.x, edge.y] for edge in node.edges])
    start = [node for node in nodes.values() if node.symbol == 'S'][0]
    print(count[start.x, start.y])

if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args: argparse.Namespace = parser.parse_args()
    run(args.test)
