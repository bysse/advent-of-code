import heapq
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

    A, path = search_a(walls, start, goal)
    print("A:", A)



    B = search_b(walls, start, goal)
    print("B:", B)


def turn(delta, clockwise):
    return (-delta[1], delta[0]) if clockwise else (delta[1], -delta[0])


def search_a(walls, start, goal):
    queue = [(0, start, (1, 0), [])]
    visited_states = {}

    while queue:
        cost, pos, delta, path = heapq.heappop(queue)
        if pos == goal:
            return cost, path + [goal]
        state = (pos, delta)
        if pos in walls:
            continue

        if state in visited_states and visited_states[state] <= cost:
            continue

        #print(pos, delta, cost)
        visited_states[state] = cost

        # forward
        heapq.heappush(queue, (cost + 1, (pos[0] + delta[0], pos[1] + delta[1]), delta, path + [pos]))

        for delta in [turn(delta, True), turn(delta, False)]:
            # do an early check for walls since we will never do a 180 turn
            if (pos[0] + delta[0], pos[1] + delta[1]) in walls:
                continue
            heapq.heappush(queue, (cost + 1000, pos, delta, path))

    return -1


def search_b(walls, start, goal):
    queue = [(0, start, (1, 0), [])]
    visited_states = {}

    tiles = set()

    best_cost = -1

    while queue:
        cost, pos, delta, path = heapq.heappop(queue)
        if 0 < best_cost < cost:
            continue

        if pos == goal:
            if best_cost == -1:
                best_cost = cost

            for p in path + [goal]:
                tiles.add(p)
            continue

        state = (pos, delta)
        if pos in walls:
            continue

        if state in visited_states and visited_states[state] < cost:
            continue

        #print(pos, delta, cost)
        visited_states[state] = cost

        # forward
        heapq.heappush(queue, (cost + 1, (pos[0] + delta[0], pos[1] + delta[1]), delta, path + [pos]))

        for delta in [turn(delta, True), turn(delta, False)]:
            # do an early check for walls since we will never do a 180 turn
            if (pos[0] + delta[0], pos[1] + delta[1]) in walls:
                continue
            heapq.heappush(queue, (cost + 1000, pos, delta, path))

    return len(tiles)

if __name__ == "__main__":
    #main("input.txt")
    main("test.txt")

