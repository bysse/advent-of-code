from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools


def main(input_file):
    pos = (0, 0)
    start = (0,0)
    field = []
    for (y, line) in enumerate(lines(input_file)):
        field.append(line)
        if "^" in line:
            pos = start = (line.index("^"), y)

    width = len(field[0])
    height = len(field)

    delta = (0, -1)
    visited = set()

    max_length = 0
    while True:
        visited.add(pos)
        np = (pos[0] + delta[0], pos[1] + delta[1])
        if not (0 <= np[0] < width and 0 <= np[1] < height):
            break

        if field[np[1]][np[0]] == "#":
            delta = rotate_right(delta)
            continue
        else:
            pos = np
            max_length += 1

    print("A:", len(visited))

    B = 0
    for blocker in visited:
        if detect_loop(field, start, (0, -1), blocker, 1.5*max_length):
            B += 1
    print("B:", B)


def detect_loop(field, pos, delta, extra, max_length):
    width = len(field[0])
    height = len(field)

    steps = 0
    while True:
        if steps >= max_length:
            return True

        np = (pos[0] + delta[0], pos[1] + delta[1])
        if not (0 <= np[0] < width and 0 <= np[1] < height):
            break

        if field[np[1]][np[0]] == "#" or np == extra:
            delta = rotate_right(delta)
        else:
            pos = np
        steps += 1
    return False

def rotate_right(delta):
    if delta == (0, -1):
        return 1, 0
    if delta == (1, 0):
        return 0, 1
    if delta == (0, 1):
        return -1, 0
    if delta == (-1, 0):
        return 0, -1

if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
