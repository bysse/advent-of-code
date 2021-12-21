from std import *
from collections import Counter
import re
import functools
import itertools

DAY = "21"

multiverse = Counter([(0, 0, 1, 0)])
outcomes = Counter(sum(x) for x in itertools.product([1, 2, 3], repeat=3))

def player_round(multiverse, player):
    wins = [0, 0]
    state = Counter()
    for key, n in multiverse.items():
        pos = key[2*player+0]
        score = key[2*player+1]
        for roll, times in outcomes.items():
            np = (pos + roll) % 10
            ns = score + np + 1
            if ns >= 21:
                wins[player] += n * times
                continue
            nkey = list(key)
            nkey[2*player+0] = np
            nkey[2*player+1] = ns
            state[tuple(nkey)] += n * times
    return state, wins

def round(multiverse):
    multiverse, w1 = player_round(multiverse, 0)
    multiverse, w2 = player_round(multiverse, 1)
    return multiverse, [w1[0] + w2[0], w1[1] + w2[1]]

wins = [0,0]
while len(multiverse):
    multiverse, rw = round(multiverse)
    wins[0] += rw[0]
    wins[1] += rw[1]

print("B:", max(wins))