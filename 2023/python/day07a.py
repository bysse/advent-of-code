from collections import defaultdict, Counter

from std import *
import copy
import re
import functools
import itertools

DAY = re.sub(r"day(\d\d).*.py", r"\1", os.path.basename(__file__))
INPUT = f"../input/input{DAY}.txt"
# INPUT = f"../input/test{DAY}.txt"

strength = {k: i + 1 for (i, k) in enumerate(reversed("AKQJT98765432"))}


def to_hand(hand, bid):
    pattern = "".join(sorted([str(v) for k, v in Counter(hand).items()], reverse=True))
    types = {v: i for i, v in enumerate(["11111", "2111", "221", "311", "32", "41", "5"])}
    return types[pattern], hand, bid


def key_func(h):
    return [h[0]] + list(map(lambda x: strength[x], str(h[1])))


A = 0
hands = []
for line in lines(INPUT):
    hand, bid = line.split()
    hands.append(to_hand(hand, int(bid)))

hands.sort(key=key_func, reverse=False)

for rank, hand in enumerate(hands):
    A += (rank + 1) * hand[2]

print("A:", A)
