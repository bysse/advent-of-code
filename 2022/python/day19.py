from std import *
import copy
import re
import functools
import itertools

DAY = "19"
INPUT = f"../input/input{DAY}.txt"
INPUT = "../input/test.txt"

blueprints = {}
for line in lines(INPUT):
    id, ore, clay, oo, oc, go, gc = ints(line)
    blueprints[id] = ((ore, 0), (clay, 0), (oo, oc), (go, gc))


def dump(state):
    s, r = state
    print(f"{s[0]} {s[1]} {s[2]} {s[3]} | {r[0]} {r[1]} {r[2]} {r[3]}")


def produce(stuff, robots):
    for i in range(4):
        stuff[i] += robots[i]
    return stuff


for id, bp in blueprints.items():
    print(id, bp)
    # do DFS





print("A:")
print("B:")

