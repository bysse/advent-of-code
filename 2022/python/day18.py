from std import *
import copy
import re
import functools
import itertools

DAY = "18"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

data = set()
for line in lines(INPUT):
    data.add(tuple(ints(line)))

dim = []
for ds in list(zip(*data)):
    dim.append((min(ds), max(ds)))


def count_sides(p):
    sides = 6
    for x, y, z in adjacent_3d(*p):
        if (x, y, z) in data:
            sides -= 1
    return sides


def outside(p):
    for j in range(3):
        if p[j] < dim[j][0]-1 or dim[j][1]+1 < p[j]:
            return True
    return False


def scan(x, y, z):
    exterior = 0
    visited = set()
    points = {(x, y, z)}

    while points:
        explore = set()
        for p0 in points:
            for p in adjacent_3d(*p0):
                if p in visited or outside(p):
                    continue
                if p in data:
                    exterior += 1
                else:
                    explore.add(p)
            visited.add(p0)
        points = explore

    return exterior


visited = {}
for p in data:
    if p in visited:
        continue
    visited[p] = count_sides(p)
surface = sum(visited.values())

exterior = scan(dim[0][0], dim[1][0], dim[2][0])

print("A:", surface)
print("B:", exterior)
