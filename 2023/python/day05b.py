from collections import deque

from std import *
import copy
import re
import functools
import itertools

DAY = "05"
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

B = None

data = []
groups = list(groups(INPUT))

ss = ints(groups[0][1])
seeds = []
for i in range(0, len(ss), 2):
    seeds.append(Interval(ss[i], ss[i] + ss[i + 1]))

mappings = []
for group in groups[1:]:
    mapping = []
    for line in group[1:]:
        n = ints(line)
        mapping.append((Interval(n[1], n[1] + n[2]), Interval(n[0], n[0] + n[2])))
    mappings.append(mapping)


def map_interval(interval, m):
    return Interval(interval.x0 - m[0].x0 + m[1].x0, interval.x1 - m[0].x0 + m[1].x0)


def map_seed_list(seed_list, mapping):
    queue = deque(seed_list)
    lst = []
    while queue:
        seed = queue.popleft()
        for m in mapping:
            if seed in m[0]:
                if intersection := seed.intersect(m[0]):
                    lst.append(map_interval(intersection, m))
                    if intersection != seed:
                        # cut the range in two
                        queue += seed.cut_out(m[0])
                seed = None
                break
        if seed:
            lst.append(seed)
    return lst


for seed in seeds:
    seed_list = [seed]
    for mapping in mappings:
        seed_list = map_seed_list(seed_list, mapping)
    s_min = min(map(lambda x: x.x0, seed_list))
    if B is None or s_min < B:
        B = s_min

print("B:", B)
