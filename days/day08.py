import numpy as np
from lib import load_input
from collections import defaultdict


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    nodes = defaultdict(set)
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c != ".":
                nodes[c].add((i, j))

    antinodes = set()
    for c in nodes:
        for a in nodes[c]:
            for b in nodes[c]:
                if a == b:
                    continue
                d = (a[0] - b[0], a[1] - b[1])
                antinodes.add((a[0] + d[0], a[1] + d[1]))
                antinodes.add((b[0] - d[0], b[1] - d[1]))

    return sum(0 <= x[0] < len(data) and 0 <= x[1] < len(data[0]) for x in antinodes)


def part_two(data):
    nodes = defaultdict(set)
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c != ".":
                nodes[c].add((i, j))

    antinodes = set()
    for c in nodes:
        for a in nodes[c]:
            for b in nodes[c]:
                if a == b:
                    continue
                d = (a[0] - b[0], a[1] - b[1])
                at = a
                while 0 <= at[0] < len(data) and 0 <= at[1] < len(data[0]):
                    antinodes.add(at)
                    at = (at[0] + d[0], at[1] + d[1])
                while 0 <= b[0] < len(data) and 0 <= b[1] < len(data[0]):
                    antinodes.add(b)
                    b = (b[0] - d[0], b[1] - d[1])

    return len(antinodes)


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
