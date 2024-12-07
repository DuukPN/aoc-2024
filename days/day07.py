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
        ns = line.split(" ")
        t = int(ns[0][:-1])
        eq = [int(x) for x in ns[1:]]

        for i in range(2 ** (len(eq) - 1)):
            acc = eq[0]
            for j in eq[1:]:
                if i % 2:
                    acc *= j
                else:
                    acc += j
                i //= 2

            if acc == t:
                res += t
                break

    return res


def part_two(data):
    res = 0
    for line in data:
        ns = line.split(" ")
        t = int(ns[0][:-1])
        eq = [int(x) for x in ns[1:]]

        for i in range(3 ** (len(eq) - 1)):
            acc = eq[0]
            for j in eq[1:]:
                if not i % 3:
                    acc *= j
                elif i % 3 == 1:
                    acc += j
                else:
                    acc = int(str(acc) + str(j))
                i //= 3

            if acc == t:
                res += t
                break

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
