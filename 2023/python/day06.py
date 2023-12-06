import math

from std import *
import copy
import re
import functools
import itertools

DAY = re.sub(r"day(\d\d).py", r"\1", os.path.basename(__file__))
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

ll = list(lines(INPUT))
records = list(zip(ints(ll[0]), ints(ll[1])))


def ways(t, d):
    d += 1
    sq = 0.5 * math.sqrt(t*t - 4*d)
    upper = math.floor(0.5 * t + sq)
    lower = math.ceil(0.5 * t - sq)
    return upper - lower + 1


A = 1
for t, d in records:
    A *= ways(t, d)

B = ways(
    int(re.sub(r"[^\d]", "", ll[0])),
    int(re.sub(r"[^\d]", "", ll[1]))
)

print("A:", A)
print("B:", B)

