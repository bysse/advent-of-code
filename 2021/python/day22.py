from std import *
from collections import defaultdict
import re
import functools
import itertools

DAY = "22"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

data = []
for line in lines(INPUT):
    rs = ints(line)
    value = 1 if line[1] == 'n' else 0
    data.append( (value, rs) )


def cube(x0, x1, y0, y1, z0, z1):
    for z in range(z0, z1+1):
        for y in range(y0, y1+1):
            for x in range(x0, x1+1):
                yield (x,y,z)

def clip(x0, x1, y0, y1, z0, z1):
    if x1 < -50 or x0 > 50 or y1 < -50 or y0 > 50 or z1 < -50 or z0 > 50:
        return False, None
    rs = [x0, x1, y0, y1, z0, z1]
    return True, [min(max(-50, r), 50) for r in rs]

field = defaultdict(int)
for value, rs in data:
    ok, cubelet = clip(*rs)
    if not ok:
        continue
    for p in cube(*cubelet):
        if value:
            field[p] = 1
        elif p in field:
            del field[p]

print("A:", len(field))
