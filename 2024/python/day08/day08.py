import math
from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools


def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(list(line))

    width = len(data[0])
    height = len(data)

    antennas = defaultdict(list)
    for x, line in enumerate(data):
        for y, ch in enumerate(line):
            if ch != '.':
                antennas[ch].append((x, y))

    anti_nodes_a = set()
    anti_nodes_b = set()
    for freq, positions in antennas.items():
        for node in find_anti_nodes_a(positions, width, height):
            anti_nodes_a.add(node)

        for node in find_anti_nodes_b(positions, width, height):
            anti_nodes_b.add(node)


    A = len(anti_nodes_a)
    B = len(anti_nodes_b)

    #print("\n".join(map(lambda l: "".join(l), data)))

    print("A:", A)
    print("B:", B)


def find_anti_nodes_a(positions, width, height):
    for a, b in itertools.combinations(positions, 2):
        dx, dy = a[0] - b[0], a[1] - b[1]
        px, py = a[0] - 2 * dx, a[1] - 2 * dy

        if 0 <= px < width and 0 <= py < height:
            yield px, py
        px, py = b[0] + 2 * dx, b[1] + 2 * dy
        if 0 <= px < width and 0 <= py < height:
            yield px, py


def find_anti_nodes_b(positions, width, height):
    for a, b in itertools.combinations(positions, 2):
        dx, dy = a[0] - b[0], a[1] - b[1]
        px, py = a[0] - dx, a[1] - dy
        while 0 <= px < width and 0 <= py < height:
            yield px, py
            px -= dx
            py -= dy

        px, py = b[0] + dx, b[1] + dy
        while 0 <= px < width and 0 <= py < height:
            yield px, py
            px += dx
            py += dy


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
