from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"


def find_reflection(data):
    height = len(data)
    for y in range(1, len(data)):
        if data[y] == data[y - 1]:
            # verify perfect reflection
            found = True
            for dy in range(min(y, height - y)):
                if data[y + dy] != data[y - dy - 1]:
                    found = False
                    break
            if found:
                return y
    return -1


A = 0
B = 0

for group in groups(INPUT):
    row = find_reflection(group)
    if row >= 0:
        A += 100 * row
        continue

    group_t = ["" for _ in range(len(group[0]))]
    for y in range(len(group)):
        for x, ch in enumerate(group[y]):
            group_t[x] += ch

    col = find_reflection(group_t)
    A += col

print("A:", A)
print("B:", B)
