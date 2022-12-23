import copy
from collections import defaultdict

from std import *

DAY = "23"
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test-{DAY}.txt"

elves = set()

y = 0
for line in lines(INPUT):
    for x, ch in enumerate(line):
        if ch == '#':
            elves.add((x, y))
    y += 1


def round(i, elves):
    occupancy = defaultdict(int)
    move = {}

    dirs = [
        (0, -1), (0, 1), (-1, 0), (1, 0)
    ]

    def free(x, y):
        return (x, y) not in elves

    still = 0
    for pos in elves:
        x, y = pos

        nw, ne = free(x - 1, y - 1), free(x + 1, y - 1)
        sw, se = free(x - 1, y + 1), free(x + 1, y + 1)

        freedom = [
            nw and free(x, y - 1) and ne,
            sw and free(x, y + 1) and se,
            nw and free(x - 1, y) and sw,
            ne and free(x + 1, y) and se
        ]

        if sum(freedom) == 4 or sum(freedom) == 0:
            occupancy[pos] += 1
            move[pos] = pos
            still += 1
            continue

        for j in range(4):
            index = (i+j) % 4
            if freedom[index]:
                np = x + dirs[index][0], y + dirs[index][1]
                occupancy[np] += 1
                move[pos] = np
                break

    state = set()
    for old, new in move.items():
        if occupancy[new] > 1:
            state.add(old)
            continue
        state.add(new)

    assert len(elves) == len(state)
    return state, still == len(state)


def part_a():
    positions = copy.deepcopy(elves)
    for r in range(10):
        positions, _ = round(r, positions)

    x0, y0 = [min(p) for p in zip(*positions)]
    x1, y1 = [max(p) for p in zip(*positions)]
    return (x1 - x0 + 1) * (y1 - y0 + 1) - len(positions)


def part_b():
    positions = copy.deepcopy(elves)
    count = 0
    while True:
        positions, still = round(count, positions)
        count += 1
        if still:
            return count


print("A:", part_a())
print("B:", part_b())
