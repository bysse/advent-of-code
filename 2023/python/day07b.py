from collections import defaultdict, Counter

from std import *
import copy
import re
import functools
import itertools

DAY = re.sub(r"day(\d\d).*.py", r"\1", os.path.basename(__file__))
INPUT = f"../input/input{DAY}.txt"
# INPUT = f"../input/test{DAY}.txt"

strength = {k: i + 1 for (i, k) in enumerate(reversed("AKQT98765432J"))}


def to_hand(hand, bid):
    count = Counter(hand)
    jokers = 0
    if 'J' in count:
        jokers = count['J']
        count.pop('J')
        if len(count) == 0:
            count['J'] = 5
        else:
            mc = count.most_common(1)[0]
            count[mc[0]] += jokers

    pattern = "".join(sorted([str(v) for k, v in count.items()], reverse=True))
    print(pattern)
    types = {v: i for i, v in enumerate(["11111", "2111", "221", "311", "32", "41", "5"])}
    return types[pattern], hand, bid


def key_func(h):
    return [h[0]] + list(map(lambda x: strength[x], str(h[1])))


B = 0
hands = []
for line in lines(INPUT):
    hand, bid = line.split()
    hands.append(to_hand(hand, int(bid)))

hands.sort(key=key_func, reverse=False)

for rank, hand in enumerate(hands):
    B += (rank + 1) * hand[2]

print("B:", B)

# 253767629 too high
# 253498818
# 252721789
# 252686195 too low
# 252382745
