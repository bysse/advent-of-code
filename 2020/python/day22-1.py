from std import *
from year import *
import re
import functools
import itertools

player = -1
deck = [[],[]]
for line in lines("../input/input22.txt"):
    if not line:
        continue
    if ":" in line:
        player += 1
        continue
    deck[player].append(int(line))

def score(deck):
    s = 0
    p = 1
    for m in reversed(deck):
        s += m * p
        p += 1
    return s

def round(deck):
    p0 = deck[0].pop(0)
    p1 = deck[1].pop(0)
    if p0 > p1:
        deck[0] += [p0, p1]
    else:
        deck[1] += [p1, p0]


rc = 0
while deck[0] and deck[1]:
    rc += 1
    print("Round", rc)
    print(deck[0])
    print(deck[1])
    round(deck)

print(score(deck[0] if deck[0] else deck[1]))
