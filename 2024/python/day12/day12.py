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


def calc_cost(region):
    # find perimeter
    area = len(region)
    perimeter = 0
    for (x, y) in region:
        # check if there is a neighbour
        neighbours = 0
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            np = (x + dx, y + dy)
            neighbours += 0 if np not in region else 1

        perimeter += 4 - neighbours

    return area * perimeter


def main(input_file):
    field, height, width = load_2d(input_file)

    type_map = defaultdict(set)
    plot_map = {}
    for y in range(height):
        for x in range(width):
            plot_map[(x, y)] = field[y][x]
            type_map[field[y][x]].add((x, y))

    cost = 0
    for pt, plots in type_map.items():
        for region in find_regions(plots):
            # Find area and perimeter
            cost += calc_cost(region)

    A = cost
    B = 0

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
