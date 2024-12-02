import numpy as np
from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    res = 0
    for line in data:
        l = [int(x) for x in line.split(" ")]
        res += (all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))) and (
            all(1 <= abs(l[i] - l[i + 1]) <= 3 for i in range(len(l) - 1))
        )

    return res


def part_two(data):
    res = 0
    for line in data:
        li = [int(x) for x in line.split(" ")]
        res += any((all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(
            l[i] >= l[i + 1] for i in range(len(l) - 1))) and (
                   all(1 <= abs(l[i] - l[i + 1]) <= 3 for i in range(len(l) - 1))
               ) for l in [[li[x] for x in range(len(li)) if x != a] for a in range(len(li))])

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
