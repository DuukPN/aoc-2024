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
    rules = defaultdict(set)
    for line in data:
        if not line:
            break
        a, b = [int(x) for x in line.split("|")]
        rules[a].add(b)

    res = 0
    for line in data[data.index("") + 1:]:
        o = [int(x) for x in line.split(",")]
        if all(not any(x in rules[o[i]] for x in o[:i]) for i in range(1, len(o))):
            res += o[len(o) // 2]

    return res


def part_two(data):
    rules = defaultdict(set)
    for line in data:
        if not line:
            break
        a, b = [int(x) for x in line.split("|")]
        rules[a].add(b)

    res = 0
    for line in data[data.index("") + 1:]:
        o = [int(x) for x in line.split(",")]
        if not all(not any(x in rules[o[i]] for x in o[:i]) for i in range(1, len(o))):
            my_sort(o, rules)
            res += o[len(o) // 2]

    return res


def my_sort(l, rules):
    for i, s in enumerate(l):
        min_idx = i
        for j in range(i + 1, len(l)):
            if l[min_idx] in rules[l[j]]:
                min_idx = j
        (l[i], l[min_idx]) = (l[min_idx], l[i])


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
