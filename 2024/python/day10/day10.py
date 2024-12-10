from collections import deque

from tomlkit.container import ends_with_whitespace

from std import *
import copy
import re
import functools
import itertools


def main(input_file):
    starts = set()
    ends = set()

    data = []
    for y, line in enumerate(lines(input_file)):
        row = []
        for x, ch in enumerate(line):
            height = int(ch)
            row.append(height)
            if height == 0:
                starts.add((x, y))
            if height == 9:
                ends.add((x, y))
        data.append(row)

    # Find all paths
    A = 0
    B = 0
    for pos in starts:
        found = find_path_a(data, pos, ends, lambda dh: dh == -1)
        A += len(found)

        found, count = find_path_b(data, pos, ends, lambda dh: dh == -1)
        B += count

    print("A:", A)
    print("B:", B)


def find_path_a(field, start, goals, valid_step):
    width = len(field[0])
    height = len(field)

    queue = deque([start])
    visited = set()

    found_goals = set()

    while queue:
        pos = queue.pop()
        if pos in goals:
            found_goals.add(pos)
            continue
        visited.add(pos)
        h = field[pos[1]][pos[0]]
        for nx, ny in tdlr_2d(*pos, width, height):
            if (nx, ny) in visited:
                continue
            nh = field[ny][nx]
            if valid_step(h - nh):
                queue.append((nx, ny))

    return found_goals

def find_path_b(field, start, goals, valid_step):
    width = len(field[0])
    height = len(field)

    queue = deque([start])
    found_goals = set()
    found_count = 0

    while queue:
        pos = queue.pop()
        if pos in goals:
            found_count += 1
            found_goals.add(pos)
            continue
        h = field[pos[1]][pos[0]]
        for nx, ny in tdlr_2d(*pos, width, height):
            nh = field[ny][nx]
            if valid_step(h - nh):
                queue.append((nx, ny))

    return found_goals, found_count


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
