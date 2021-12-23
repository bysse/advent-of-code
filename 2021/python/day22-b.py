from std import *
from collections import Counter

DAY = "22"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

data = []
for line in lines(INPUT):
    rs = tuple(ints(line))
    value = 1 if line[1] == 'n' else -1
    data.append( (value, rs) )

def intersect(a, b):
    ax0, ax1, ay0, ay1, az0, az1 = a
    bx0, bx1, by0, by1, bz0, bz1 = b
    return (max(ax0, bx0), min(ax1, bx1), max(ay0, by0), min(ay1, by1), max(az0, bz0), min(az1, bz1))

def is_valid(a):
    return a[0] < a[1] and a[2] < a[3] and a[4] < a[5]

def volume(a):    
    return (a[1]-a[0]+1)*(a[3]-a[2]+1)*(a[5]-a[4]+1)

cubes = Counter()
for sign, cube in data:
    add = Counter()
    for ec, s in cubes.items():
        ic = intersect(ec, cube)
        if is_valid(ic):
            add[ic] -= s
    if sign > 0:
        cubes[cube] += sign
    cubes.update(add)

s = 0
for cube, v in cubes.items():
    s += volume(cube) * v

print("B:", s)