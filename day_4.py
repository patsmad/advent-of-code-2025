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
        self.neighbors = []

    def add_neighbors(self, node_map):
        for dx, dy in [(-1, 0), (0, -1), (-1, -1), (1, -1)]:
            if (self.y + dy, self.x + dx) in node_map:
                self.neighbors.append(node_map[self.y + dy, self.x + dx])
                node_map[self.y + dy, self.x + dx].neighbors.append(self)

    def poppable(self):
        paper_neighbors = [neighbor for neighbor in self.neighbors if neighbor.symbol == '@']
        return self.symbol == '@' and len(paper_neighbors) < 4

def run(test: bool) -> None:
    if not test:
        raw_input: str = get_input(day)
    else:
        raw_input: str = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
        """.strip()

    grid = raw_input.strip().split('\n')
    # part 1
    node_map = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            node_map[i, j] = Node(j, i, grid[i][j])
            node_map[i, j].add_neighbors(node_map)
    print(sum([node.poppable() for node in node_map.values()]))

    # part 2
    popped = 0
    poppable_nodes = [node for node in node_map.values() if node.poppable()]
    while len(poppable_nodes) > 0:
        popped += len(poppable_nodes)
        print(f'Popping {len(poppable_nodes)} nodes')
        for node in poppable_nodes:
            node.symbol = '.'
        poppable_nodes = [node for node in node_map.values() if node.poppable()]
    print(popped)


if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args: argparse.Namespace = parser.parse_args()
    run(args.test)
