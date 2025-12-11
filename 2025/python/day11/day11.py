import heapq
from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools


def find_solutions(nodes, start, goal):
    explore = [start]
    count = 0
    while explore:
        node = heapq.heappop(explore)

        if node == goal:
            count += 1
            continue

        for child in nodes[node]:
            heapq.heappush(explore, child)
    return count


def find_solutions_b(nodes, start, goal):
    state_map = defaultdict(int)

    for _ in range(5):
        for node, found, state_map in state_map:



    return state_map


def main(input_file):
    nodes = {}
    for line in lines(input_file):
        parts = [x.rstrip(':') for x in line.split(' ')]
        nodes[parts[0]] = parts[1:]

    A = 0
    B = 0

    A += find_solutions(nodes, 'you', 'out')
    print("A:", A)

    B += find_solutions_b(nodes, 'out', 'svr')

    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")