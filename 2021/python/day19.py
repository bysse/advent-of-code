from std import *
import numpy as np
import re
import collections
import functools
import itertools

DAY = "19"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

data = []
for line in groups(INPUT):
    id = ints(line[0])[0]
    data.append([tuple(ints(x)) for x in line[1:]])


def makef(m):    
    return lambda x: tuple(np.matrix.tolist(np.array(x).dot(m))[0])

pm = []
for p in [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]:
    m = np.matrix([[0,0,0],[0,0,0],[0,0,0]])
    for i in range(3):
        m[i, p[i]] = 1
    pm.append(m)

fm = []
for i in [-1, 1]:
    for j in [-1, 1]:
        for k in [-1, 1]:
            fm.append(np.matrix([[i,0,0],[0,j,0],[0,0,k]]))

transforms = []
for p in pm:
    for f in fm:
        m = np.matmul(f, p)
        if np.linalg.det(m) == 1:
            transforms.append(makef(m))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])    

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])

def qualifying_diffs(A, B):
    dcount = collections.defaultdict(int)     
    for a in A:
        for b in B:
            delta = sub(b, a)
            dcount[delta] += 1
            if dcount[delta] >= 12:
                return delta
    return None


def find_overlap(beacons, results):
    for transform in transforms:
        rotated = list(map(transform, results))
        if delta := qualifying_diffs(beacons, rotated):
            # now we have an overlap and position, transform and return
            return set([sub(x, delta) for x in rotated]), delta
    return None, None


beacons = set(data[0])
positions = [(0,0,0)]
remaining = data[1:]

while len(remaining):
    for results in remaining:
        bnew, position = find_overlap(beacons, results)
        if bnew:
            beacons |= bnew
            positions.append(position)
            remaining.remove(results)
            break

print("A:", len(beacons))

dmax = 0
for i, s1 in enumerate(positions):
    for j, s2 in enumerate(positions):
        dmax = max(dmax, dist(s1, s2))

print("B:", dmax) 
