from std import *
import copy
import re
import functools
import itertools

DAY = "05"
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

A = None
B = 0

data = []
groups = list(groups(INPUT))
seeds = list(map(int, groups[0][1].split()))

mappings = []
for group in groups[1:]:
    mapping = []
    for line in group[1:]:
        mapping.append(ints(line))
    mappings.append(mapping)


def map_seed(seed, mapping):
    for m in mapping:
        if m[1] <= seed <= m[1] + m[2]:
            seed = (seed - m[1]) + m[0]
            break
    return seed


for seed in seeds:
    for mapping in mappings:
        seed = map_seed(seed, mapping)
    if A is None or seed < A:
        A = seed

print("A:", A)
print("B:", B)
