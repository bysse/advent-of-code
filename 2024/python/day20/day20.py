import heapq
from collections import deque

from std import *
import copy
import re
import functools
import itertools

def solve_optimal2(start, end, walls, min_save=100, cheat=2):
    queue = [(0, start)]
    tile_cost = {}

    w, h = max(walls)
    count = 0

    while queue:
        cost, pos = heapq.heappop(queue)
        if pos in tile_cost:
            if tile_cost[pos] < cost:
                continue
        tile_cost[pos] = cost
        if pos == end:
            continue

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            x = pos[0] + dx
            y = pos[1] + dy
            if (x, y) in walls:
                continue

            heapq.heappush(queue, (cost + 1, (x, y)))

    # look for cheats
    for (x, y) in tile_cost.keys():
        for dy in range(-cheat, cheat + 1):
            for dx in range(-cheat, cheat + 1):
                cost = abs(dx) + abs(dy)
                if cost > cheat:
                    continue
                nx, ny = x + dx, y + dy
                if (nx, ny) in walls or nx < 0 or ny < 0 or nx >= w or ny >= h:
                    continue

                n = tile_cost[(nx, ny)]
                c = tile_cost[(x, y)] + cost

                if n - c >= min_save:
                    count += 1

    return count

def main(input_file, min_save=100):
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

    A = solve_optimal2(start, end, walls, min_save, 2)
    B = solve_optimal2(start, end, walls, min_save, 20)

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt", 100)
    # main("test.txt", 1)
