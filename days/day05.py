import numpy as np
from lib import load_input
from collections import defaultdict
from functools import cmp_to_key
import time


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


def part_one_oneline(data):
    return sum(int(line.split(",")[line.count(",") // 2]) for line in data[data.index("") + 1:] if all(not any(x in ({a: set(line.split("|")[1] for line in data[:data.index("")] if line.split("|")[0] == a) for a in set(line.split("|")[0] for line in data[:data.index("")])})[line.split(",")[i + 1]] for x in line.split(",")[:i + 1]) for i in range(line.count(","))))


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
            o.sort(key=cmp_to_key(lambda a, b: -1 if b in rules[a] else 1))
            res += o[len(o) // 2]

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
