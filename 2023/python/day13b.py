from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"


def compare_with_smudge(a, b):
    c = 0
    for i,j in zip(a, b):
        if i != j:
            c += 1
    return c


def find_reflection(data):
    height = len(data)
    for y in range(1, len(data)):
        found = True
        smudges = 0
        for dy in range(min(y, height - y)):
            smudges += compare_with_smudge(data[y + dy], data[y - dy - 1])
            if smudges > 1:
                found = False
                break
        if found and smudges == 1:
            return y
    return -1


B = 0
for group in groups(INPUT):
    row = find_reflection(group)
    if row >= 0:
        B += 100 * row
        continue

    group_t = ["" for _ in range(len(group[0]))]
    for y in range(len(group)):
        for x, ch in enumerate(group[y]):
            group_t[x] += ch

    col = find_reflection(group_t)
    B += col

print("B:", B)
