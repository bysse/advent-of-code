import heapq
from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
# INPUT = f"../input/test{DAY}.txt"

data = []
for line in lines(INPUT):
    data.append([int(x) for x in line])

w = len(data[0])
h = len(data)

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def search_a(start, end):
    # cost, pos (x, y), move (orientation, streak)
    queue = [(0, start, (0, 0)), (0, start, (1, 0))]
    node_cost = {}

    while queue:
        cost, pos, move = heapq.heappop(queue)
        if pos == end:
            return cost

        for next_orientation in [move[0], (move[0] + 1) % 4, (move[0] - 1) % 4]:
            movement = delta[next_orientation]
            next_pos = (pos[0] + movement[0], pos[1] + movement[1])

            if next_pos[0] < 0 or next_pos[0] >= w or next_pos[1] < 0 or next_pos[1] >= h:
                continue
            next_streak = move[1] + 1 if next_orientation == move[0] else 0
            if next_streak >= 3:
                continue

            next_cost = data[next_pos[1]][next_pos[0]] + cost
            next_move = (next_orientation, next_streak)
            next_key = (next_pos, next_move)

            if next_cost < node_cost.get(next_key, 999999999):
                heapq.heappush(queue, (next_cost, next_pos, next_move))
                node_cost[next_key] = next_cost

    return -1


def search_b(start, end):
    # cost, pos (x, y), move (orientation, streak)
    queue = [(data[0][1], (1, 0), (0, 0)), (data[1][0], (0, 1), (1, 0))]
    node_cost = {}

    while queue:
        cost, pos, move = heapq.heappop(queue)
        if pos == end and move[1] >= 3:
            return cost

        for next_orientation in [move[0], (move[0] + 1) % 4, (move[0] - 1) % 4]:
            movement = delta[next_orientation]
            next_pos = (pos[0] + movement[0], pos[1] + movement[1])

            if next_pos[0] < 0 or next_pos[0] >= w or next_pos[1] < 0 or next_pos[1] >= h:
                continue
            if move[0] != next_orientation and move[1] < 3:
                continue
            next_streak = move[1] + 1 if next_orientation == move[0] else 0
            if next_streak >= 10:
                continue

            next_cost = data[next_pos[1]][next_pos[0]] + cost
            next_move = (next_orientation, next_streak)
            next_key = (next_pos, next_move)

            if next_cost < node_cost.get(next_key, 999999999):
                heapq.heappush(queue, (next_cost, next_pos, next_move))
                node_cost[next_key] = next_cost

    return -1


A = search_a((0, 0), (w - 1, h - 1))
B = search_b((0, 0), (w - 1, h - 1))

print("A:", A)
print("B:", B)

# 1006 too low
