import heapq

from std import *
import copy
import re
import functools
import itertools


def solve_a(walls, w, h):
    queue = [(0, 0, 0)]
    cost_map = {}

    while queue:
        cost, x, y = heapq.heappop(queue)
        if (x, y) == (w, h):
            return cost

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > w or ny > h:
                continue
            if (nx, ny) in walls:
                continue
            if (nx, ny) in cost_map and cost_map[(nx, ny)] <= cost + 1:
                continue
            cost_map[(nx, ny)] = cost + 1
            heapq.heappush(queue, (cost + 1, nx, ny))
    return -1


def solve_b(data, w, h):
    for i in range(len(data)):
        idx = len(data) - i - 1
        steps = solve_a(set(data[:idx]), w, h)
        if steps != -1:
            return data[idx]
    return -1


def main(input_file, w, h, steps):
    data = []
    for line in lines(input_file):
        data.append(tuple(ints(line)))

    A = solve_a(set(data[:steps]), w, h)
    B = solve_b(data, w, h)

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt", 70, 70, 1024)
    #main("test.txt", 6, 6, 12)
