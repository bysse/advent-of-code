from collections import deque

from std import *
import copy
import re
import functools
import itertools


def main(input_file):
    walls = set()
    start = None
    goal = None
    for y, line in enumerate(lines(input_file)):
        for x, ch in enumerate(line):
            if ch == '#':
                walls.add((x, y))
            if ch == 'E':
                goal = (x, y)
            if ch == 'S':
                start = (x, y)

    B = 0

    A = search_a(walls, start, goal)

    print("A:", A)
    print("B:", B)


def turn(delta, clockwise):
    return (delta[1], delta[0]) if clockwise else (delta[1], -delta[0])


def search_a(walls, start, goal):
    queue = deque()
    queue.append((0, start, (1, 0)))
    visited_states = {}

    while queue:
        # TODO: sort queue
        cost, pos, delta = queue.pop()
        if pos == goal:
            return cost
        state = (pos, delta)
        if pos in walls:
            continue

        if state in visited_states and visited_states[state] <= cost:
            continue

        print(pos, cost)
        visited_states[state] = cost

        # forward
        queue.append((cost + 1, (pos[0] + delta[0], pos[1] + delta[1]), delta))

        for delta in [turn(delta, True), turn(delta, False)]:
            state = (pos, delta)
            if state in visited_states and visited_states[state] <= cost:
                continue

            queue.append((cost + 1000, pos, delta))

    return -1


if __name__ == "__main__":
    # main("input.txt")
    main("test.txt")
