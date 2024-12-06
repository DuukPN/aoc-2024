import numpy as np
from lib import load_input


def solve(data, part=2):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    objs = set()
    pos = None
    di = None
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "^":
                pos = (i, j)
                di = (-1, 0)
            elif c == "#":
                objs.add((i, j))

    visited = set()
    while 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0]):
        visited.add(pos)
        if (pos[0] + di[0], pos[1] + di[1]) in objs:
            di = (di[1], -di[0])
        pos = (pos[0] + di[0], pos[1] + di[1])
    return len(visited)


def part_two(data):
    objs = set()
    start_pos = None
    start_di = None
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "^":
                start_pos = (i, j)
                start_di = (-1, 0)
            elif c == "#":
                objs.add((i, j))

    visited1 = set()
    pos, di = start_pos, start_di
    while 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0]):
        visited1.add(pos)
        if (pos[0] + di[0], pos[1] + di[1]) in objs:
            di = (di[1], -di[0])
        pos = (pos[0] + di[0], pos[1] + di[1])

    res = 0
    for oi in range(len(data)):
        for oj in range(len(data[0])):
            pos = start_pos
            di = start_di
            if (oi, oj) == start_pos or (oi, oj) in objs or (oi, oj) not in visited1:
                continue
            visited = set()
            while 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0]):
                if (pos, di) in visited:
                    res += 1
                    break
                visited.add((pos, di))
                if (pos[0] + di[0], pos[1] + di[1]) in objs or (pos[0] + di[0], pos[1] + di[1]) == (oi, oj):
                    di = (di[1], -di[0])
                    continue
                pos = (pos[0] + di[0], pos[1] + di[1])

    return res


if __name__ == "__main__":
    print(solve(load_input(), 1))
    print(solve(load_input()))
