import heapq
import heapq
from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

data = {}
for y, line in enumerate(lines(INPUT)):
    for x, n in enumerate(line):
        data[(x, y)] = int(n)

w, h = max(data)


def search(start, end):
    # ITEM (cost, pos (x, y), move (dx, dy), streak)
    queue = [
        (data[(1, 0)], (1, 0), (1, 0), 0),
        (data[(0, 1)], (0, 1), (0, 1), 0)
    ]
    visited = set()

    while queue:
        cost, pos, move, streak = heapq.heappop(queue)
        if pos == end and streak >= 3:
            return cost

        if (pos, move, streak) in visited:
            continue
        visited.add((pos, move, streak))

        # move forward
        if streak < 9:
            next_pos = (pos[0] + move[0], pos[1] + move[1])
            if next_pos in data:
                next_cost = cost + data[next_pos]
                heapq.heappush(queue, (next_cost, next_pos, move, streak + 1))

        if streak >= 3:
            for dx, dy in [(move[1], -move[0]), (-move[1], move[0])]:
                next_pos = (pos[0] + dx, pos[1] + dy)
                if next_pos in data:
                    next_cost = cost + data[next_pos]
                    heapq.heappush(queue, (next_cost, next_pos, (dx, dy), 0))

    return -1


print("B", search(min(data), max(data)))

# 1006 too low
