import numpy as np
from lib import load_input
import re


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    res = 0
    for line in data:
        m = re.findall(r"mul\(\d+,\d+\)", line)
        for match in m:
            a, b = match[4:-1].split(",")
            res += int(a) * int(b)

    return res


def part_two(data):
    res = 0
    do = True
    for line in data:
        m = re.findall(r"(mul\(\d+,\d+\))|(do(n't)?\(\))", line)
        for match in m:
            if match[1]:
                do = not match[2]
            if match[0] and do:
                a, b = match[0][4:-1].split(",")
                res += int(a) * int(b)

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
