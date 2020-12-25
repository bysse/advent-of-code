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
        return 0
    deck[1] += [p1, p0]
    return 1

def fp(deck):
    return tuple([tuple(x) for x in deck])  

def game(deck, depth):
    p0 = deck[0].pop(0)
    p1 = deck[1].pop(0)

    winner = 0 if p0 > p1 else 1
    if len(deck[0]) >= p0 and len(deck[1]) >= p1:
        # recursive game
        winner = gameloop([deck[0][:p0], deck[1][:p1]], depth + 1)

    if winner == 0:
        deck[0] += [p0, p1]
    else:
        deck[1] += [p1, p0]
    return False, 0

def gameloop(deck, depth=0):
    memory = set()

    rc = 0    
    while True:
        rc += 1
        #print("-- Round", rc, "(Game", depth+1, ") --")
        #print("Player 1", deck[0])
        #print("Player 2", deck[1])

        deckId = fp(deck)
        if deckId in memory:        
            return 0
        memory.add(deckId)

        decided, winner = game(deck, depth)
        if decided:
            return winner
        if not deck[0]:
            return 1
        if not deck[1]:
            return 0


winner = gameloop(deck)
print(score(deck[winner]))
