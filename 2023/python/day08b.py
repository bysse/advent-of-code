import math

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

B = 0

nodes = {}
grp = list(groups(INPUT))
ops = grp[0][0]

for line in grp[1]:
    p = extract(line, [r"(\w+)", r"(\w+)", r"(\w+)"])
    nodes[p[0]] = (p[1], p[2])


def find_length(node):
    length = 0
    op = 0
    while not node.endswith('Z'):
        branch = 0 if ops[op] == 'L' else 1
        node = nodes[node][branch]
        op = (op + 1) % len(ops)
        length += 1

    return length


loop_length = []
for node in nodes.keys():
    if node.endswith('A'):
        loop_length.append(find_length(node))

print("B:", math.lcm(*loop_length))
