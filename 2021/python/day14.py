from std import *
import re
import functools
import itertools

DAY = "14"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

data = list(groups(INPUT))
seed = list(data[0][0])
rules = {}

for line in data[1]:
    k, v = line.split(' -> ')
    rules[k] = v

p = ""
pairs = {}
for i, x in enumerate(seed):
    pair = p + x
    if pair in rules:
        pairs[pair] = 1 + pairs.get(pair, 0)
    p = x


def iterate_b(pairs):
    step = {}
    for k, v in pairs.items():
        if k in rules:
            x = rules[k]
            k1 = k[0] + x
            k2 = x + k[1]
            step[k1] = v + step.get(k1, 0)
            step[k2] = v + step.get(k2, 0)
    return step

for i in range(10):
    pairs = iterate_b(pairs)

count = {}
for k,v in pairs.items():
    for kk in k:
        count[kk] = v + count.get(kk, 0)

A = count[max(count, key=count.get)] - count[min(count, key=count.get)]
print("A:", int(.5 + A/2))


for i in range(30):
    pairs = iterate_b(pairs)

count = {}
for k,v in pairs.items():
    for kk in k:
        count[kk] = v + count.get(kk, 0)

B = count[max(count, key=count.get)] - count[min(count, key=count.get)]
print("B:", int(.5 + B/2))