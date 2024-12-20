import heapq
from collections import deque

from std import *
import copy
import re
import functools
import itertools


def solve_optimal(start, end, walls):
    queue = [(0, start)]
    tile_cost = {}

    while queue:
        cost, pos = heapq.heappop(queue)
        if pos == end:
            return cost
        if pos in tile_cost:
            if tile_cost[pos] < cost:
                continue
        tile_cost[pos] = cost

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            x = pos[0] + dx
            y = pos[1] + dy
            if (x, y) in walls:
                continue

            heapq.heappush(queue, (cost + 1, (x, y)))

    return -1


def solve_cheats(start, end, walls, max_cost):
    queue = [(0, start, 0)]
    tile_cost = {}
    w, h = max(walls)

    while queue:
        print(queue)
        cost, pos, cheated = heapq.heappop(queue)
        if cost > max_cost:
            continue
        if pos == end:
            print("Solution", cost)
            continue

        if pos in tile_cost:
            if tile_cost[pos] < cost:
                continue

        tile_cost[pos] = cost

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            x = pos[0] + dx
            y = pos[1] + dy
            if (x, y) in walls:
                continue

            heapq.heappush(queue, (cost + 1, (x, y), cheated))

        if cheated == 0:
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                x = pos[0] + dx
                y = pos[1] + dy
                if (x, y) not in walls:
                    continue

                x += dx
                y += dy

                if (x,y) in walls or x < 0 or y < 0 or x >= w or y >= h:
                    continue

                heapq.heappush(queue, (cost + 2, (x, y), 1))

    return -1


def main(input_file):
    start = None
    end = None
    walls = set()
    for y, line in enumerate(lines(input_file)):
        for x, ch in enumerate(line):
            if ch == 'S':
                start = (x, y)
            elif ch == 'E':
                end = (x, y)
            elif ch == '#':
                walls.add((x, y))


    A = solve_optimal(start, end, walls)
    B = 0

    print(start)
    print(end)

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    # main("input.txt")
    main("test.txt")
