import heapq

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

# read all points
data = {}
for y, line in enumerate(lines(INPUT)):
    for x, ch in enumerate(line):
        if ch != '#':
            data[(x, y)] = ch

slopes = {'v': (0, 1), '^': (0, -1), '<': (-1, 0), '>': (1, 0)}

# find all connections tiles
neighbours = {}
for pos in data.keys():
    for dx, dy in slopes.values():
        np = (pos[0] + dx, pos[1] + dy)
        if np in data:
            neighbours.setdefault(pos, set()).add(np)

print(neighbours)
# find all intersections
intersections = {(1, 0), max(data)}
for pos, ns in neighbours.items():
    if len(ns) > 2:
        intersections.add(pos)

print(intersections)


def find_size(pos, base):
    queue = [pos]
    visited = {base}
    size = 1
    while queue:
        p = queue.pop(0)
        if p in intersections:
            return p, size
        size += 1
        visited.add(p)

        for np in neighbours[p]:
            if np not in visited:
                queue.append(np)
    raise Exception("No intersection found")


dag = {}
for i in intersections:
    for ni in neighbours[i]:
        dx = ni[0] - i[0]
        dy = ni[1] - i[1]
        if data[ni] in slopes and slopes[data[ni]] != (dx, dy):
            continue
        node, size = find_size(ni, i)
        dag.setdefault(i, set()).add((size, node))

for k, v in dag.items():
    print(" >", k, v)

A = 0
queue = [(0, (1, 0), [(1, 0)])]
visited = {}

while queue:
    cost, pos, path = heapq.heappop(queue)
    print(cost, pos, path)
    if pos == max(data):
        A = cost
        print("Found", cost, path)
        continue

    visited[pos] = cost

    for size, np in dag[pos]:
        nc = cost - size
        if np in visited and visited[np] < nc:
            continue
        heapq.heappush(queue, (nc, np, path[:] + [np]))

print(A)
