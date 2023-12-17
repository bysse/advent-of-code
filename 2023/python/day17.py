from queue import Queue

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
INPUT = f"../input/test{DAY}.txt"

data = []
for line in lines(INPUT):
    data.append([int(x) for x in line])

w = len(data[0])
h = len(data)

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dir_char = ['>', 'v', '<', '^']


def search(start, end):
    #       x, y, d, s
    que = [(start[0], start[1], 0, 0, [start])]
    visited = {(start[0], start[1]): 0}

    result = 100000000000000
    sol = 1

    while que:
        x, y, direction, streak, path = que.pop(0)
        c = visited[(x, y)] #, direction, streak)]

        # Check for exit
        if x == end[0] and y == end[1]:
            print()
            for y, line in enumerate(data):
                for x, ch in enumerate(line):
                    if (x, y) in path:
                        print("#", end="")
                    else:
                        print(ch, end="")
                print()

            result = min(result, c)
            break

        if False:
            for iy, line in enumerate(data):
                for ix, ch in enumerate(line):
                    if x == ix and y == iy:
                        print(dir_char[direction], end="")
                    else:
                        print(ch, end="")
                print()

            print("Cost:", c)
            print()
        for next_dir in [direction, (direction + 1) % 4, (direction - 1) % 4]:
            next_pos = (x + delta[next_dir][0], y + delta[next_dir][1])
            next_streak = streak + 1 if next_dir == direction else 0
            if next_streak > 3:
                continue
            if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= w or next_pos[1] >= h:
                continue
            next_cost = c + data[next_pos[1]][next_pos[0]]
            key = (next_pos[0], next_pos[1]) #, next_dir, next_streak)
            if key in visited:
                old_cost = visited[key]
                if old_cost < next_cost:
                    continue
            # valid pos, replace in visited
            visited[key] = next_cost

            p2 = path[:] + [next_pos]
            que.append((next_pos[0], next_pos[1], next_dir, next_streak, p2))

        que.sort(key=lambda l: l[3])
        print(len(que))

    return result


A = search((0, 0), (w - 1, h - 1))
B = 0

print("A:", A)
print("B:", B)

# 888 too high
