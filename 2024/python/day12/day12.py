import math
from collections import defaultdict, deque

from std import *
import copy
import re
import functools
import itertools


def find_regions(plots):
    regions = []
    while plots:
        queue = deque([plots.pop()])
        region = set()
        while queue:
            x, y = queue.pop()
            region.add((x, y))
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                np = (x + dx, y + dy)
                if np in plots:
                    queue.append(np)
                    plots.remove(np)
        regions.append(region)
    return regions


def num_neighbours(region, x, y):
    neighbours = 0
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        np = (x + dx, y + dy)
        neighbours += 0 if np not in region else 1
    return neighbours


def edge_mask(region, x, y):
    mask = 0
    for i, (dx, dy) in enumerate([(-1, 0), (0, -1), (1, 0), (0, 1)]):
        np = (x + dx, y + dy)
        mask += (0 if np in region else 1) << i
    return mask


def plot_perimeter(region, x, y):
    mask = []
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        np = (x + dx, y + dy)
        mask.append(1 if np in region else 0)
    return tuple(mask)


def calc_cost_a(region):
    area = len(region)
    perimeter = 0
    for (x, y) in region:
        neighbours = num_neighbours(region, x, y)
        perimeter += 4 - neighbours

    return area * perimeter


def same_direction(l0, l1):
    p0, p1, i0 = l0
    q0, q1, i1 = l1
    if p0[0] == p1[0] and q0[0] == q1[0]:
        return True
    if p0[1] == p1[1] and q0[1] == q1[1]:
        return True
    return False


def is_valid(i0, i1, width):
    if abs(i0-i1) == 1:
        return True
    if abs(i0-i1) == width:
        return True
    return False


def calc_cost_b(region, width):
    area = len(region)
    if area == 1:
        return 4

    line_map = {
        1: ((0, 1), (0, 0)),
        2: ((0, 0), (1, 0)),
        4: ((1, 0), (1, 1)),
        8: ((1, 1), (0, 1))
    }

    lines = []
    for (x, y) in region:
        mask = edge_mask(region, x, y)
        for bit, (p0, p1) in line_map.items():
            if mask & bit != 0:
                lines.append(((x + p0[0], y + p0[1]), (x + p1[0], y + p1[1]), x + y * width))


    twists = defaultdict(int)
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            if lines[i] == lines[j]:
                continue
            if not same_direction(lines[i], lines[j]):
                if lines[i][0] == lines[j][1]:
                    twists[lines[i][0]] += 1
                if lines[i][1] == lines[j][0]:
                    twists[lines[i][1]] += 1

    perimeter = 0
    for count in twists.values():
        perimeter += min(2, count)

    return perimeter * area


def main(input_file):
    field, height, width = load_2d(input_file)

    type_map = defaultdict(set)
    plot_map = {}
    for y in range(height):
        for x in range(width):
            plot_map[(x, y)] = field[y][x]
            type_map[field[y][x]].add((x, y))

    A = 0
    B = 0
    for pt, plots in type_map.items():
        for region in find_regions(plots):
            # Find area and perimeter
            A += calc_cost_a(region)
            B += calc_cost_b(region, width)

    print("A:", A)
    print("B:", B)  # 1206


if __name__ == "__main__":
    # too high 815022
    main("input.txt")
    #main("test.txt")
