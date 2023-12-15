from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

A = 0
B = 0


def hash(ss):
    value = 0
    for s in ss:
        value += ord(s)
        value = (value * 17) & 0xff
    return value


data = []
ops = []
for line in lines(INPUT):
    data += [x.strip() for x in line.split(",")]

for op in data:
    fl = ints(op)
    label = op.split("-")[0].split("=")[0]
    ops.append((label, hash(label), '-' if '-' in op else '=', fl[0] if fl else -1))

for seq in data:
    A += hash(seq)

buckets = [[] for _ in range(256)]
for (label, bucket, op, focal) in ops:
    if op == '-':
        for lens in buckets[bucket]:
            if lens[0] == label:
                buckets[bucket].remove(lens)
                break
    if op == '=':
        found = False
        for i, lens in enumerate(buckets[bucket]):
            if lens[0] == label:
                found = True
                buckets[bucket][i] = (label, focal)
                break
        if not found:
            buckets[bucket].append((label, focal))

for i, bucket in enumerate(buckets):
    for j, lens in enumerate(bucket):
        B += lens[1] * (i + 1) * (j + 1)

print("A:", A)
print("B:", B)
