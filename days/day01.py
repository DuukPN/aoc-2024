import numpy as np
from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    a, b = [], []
    for line in data:
        al, bl = line.split("  ")
        a.append(int(al))
        b.append(int(bl))

    a.sort()
    b.sort()

    res = 0
    for i in range(len(a)):
        res += abs(a[i] - b[i])

    return res


def part_two(data):
    a, b = [], []
    for line in data:
        al, bl = line.split("  ")
        a.append(int(al))
        b.append(int(bl))

    res = 0
    for e in a:
        res += b.count(e) * e

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
