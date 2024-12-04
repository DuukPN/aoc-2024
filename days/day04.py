import numpy as np
from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    xmas = list("XMAS")
    d = len(data[0])
    d1, d2, d3 = range(len(data)), range(len(data[0])), range(len(data) + len(data[0]))
    lists = [
        [[c for c in data[i][:]] for i in d1],
        [[c for c in data[i][::-1]] for i in d1],
        [[l[j] for l in data] for j in d2],
        [[l[j] for l in data[::-1]] for j in d2],
        [[data[x + i - d][i] for i in d2 if 0 <= x + i - d < len(data) if 0 <= i < len(data[0])] for x in d3],
        [[data[x - i][i] for i in d2 if 0 <= x - i < len(data) if 0 <= i < len(data[0])] for x in d3],
        [[data[x + i - d][i] for i in reversed(d2) if 0 <= x + i - d < len(data) if 0 <= i < len(data[0])] for x in d3],
        [[data[x - i][i] for i in reversed(d2) if 0 <= x - i < len(data) if 0 <= i < len(data[0])] for x in d3],
    ]

    return sum(len([1 for idx in range(len(sub)) if sub[idx: idx + len(xmas)] == xmas]) for l in lists for sub in l)


def part_two(data):
    patterns = [
        [["M", None, "S"], [None, "A", None], ["M", None, "S"]],
        [["M", None, "M"], [None, "A", None], ["S", None, "S"]],
        [["S", None, "M"], [None, "A", None], ["S", None, "M"]],
        [["S", None, "S"], [None, "A", None], ["M", None, "M"]],
    ]

    def match(sub, p):
        if len(sub) != 3 or len(sub[0]) != 3:
            return False
        for i in range(3):
            for j in range(3):
                if p[i][j] and sub[i][j] != p[i][j]:
                    return False
        return True

    return sum(match([row[j:j + 3] for row in data[i:i + 3]], p) for p in patterns for i in range(len(data)) for j in range(len(data[0])))


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
