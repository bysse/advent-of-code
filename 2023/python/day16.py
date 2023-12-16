from queue import Queue

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"


def handle(dx: int, dy: int, ch: str):
    if ch == '.':
        return [(dx, dy)]
    if ch == '-':
        if dy == 0:
            return [(dx, dy)]
        return [(-1, 0), (1, 0)]
    if ch == '|':
        if dx == 0:
            return [(dx, dy)]
        return [(0, -1), (0, 1)]
    if ch == '/':
        if dy == 0:
            return [(0, -dx)]
        return [(-dy, 0)]

    if ch == '\\':
        if dx == 0:
            return [(dy, 0)]
        return [(0, dx)]

    raise Exception("Unknown piece " + str(ch))


def dump(data, energy, pos):
    print()
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if (x, y) == pos:
                print("O", end="")
            elif (x, y) in energy:
                print("#", end="")
            else:
                print(ch, end="")
        print()


data = []
for line in lines(INPUT):
    data.append(line)

w = len(data[0])
h = len(data)


def trace(pos, direction):
    que = [(pos, direction)]
    energized = set()

    done = set()

    while que:
        pos, light_dir = que.pop(0)
        if (pos, light_dir) in done:
            continue
        done.add((pos, light_dir))

        if 0 <= pos[0] < w and 0 <= pos[1] < h:
            energized.add(pos)
            ch = data[pos[1]][pos[0]]
            for d2 in handle(*light_dir, ch):
                que.append(((pos[0] + d2[0], pos[1] + d2[1]), d2))
    return len(energized)


A = trace((0, 0), (1, 0))

B = 0
for x in range(w):
    B = max(B, trace((x, 0), (0, 1)))
    B = max(B, trace((x, h-1), (0, -1)))

for y in range(h):
    B = max(B, trace((0, y), (1, 0)))
    B = max(B, trace((w-1, y), (-1, 0)))


print("A:", A)
print("B:", B)
