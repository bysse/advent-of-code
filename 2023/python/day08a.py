from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

nodes = {}
grp = list(groups(INPUT))
ops = grp[0][0]

for line in grp[1]:
    p = extract(line, [r"(\w+)", r"(\w+)", r"(\w+)"])
    nodes[p[0]] = (p[1], p[2])

op = 0
node = 'AAA'
iterations = 0
while node != 'ZZZ':
    branch = 0 if ops[op] == 'L' else 1
    node = nodes[node][branch]
    op = (op + 1) % len(ops)
    iterations += 1

print("A:", iterations)
