from std import *
import copy
import re
import functools
import itertools

DAY = "02"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"


def to_dict(ss):
    return {x[1]: int(x[0]) for x in [s.strip().split(' ') for s in ss]}


def is_valid(constraint, game):
    for round in game:
        for k, limit in constraint.items():
            if round.get(k, 0) > limit:
                return False
    return True


data = []
for line in lines(INPUT):
    gid, game = line.split(":")
    id = ints(gid)[0]

    sets = [to_dict(x.split(',')) for x in game.strip().split(";")]
    data.append((id, sets))

A = 0
constraint = {'red': 12, 'green': 13, 'blue': 14}
for id, game in data:
    if is_valid(constraint, game):
        A += id

print("A:", A)

B = 0
for _, game in data:
    B += (max(map(lambda x: x.get('red', 0), game)) *
          max(map(lambda x: x.get('blue', 0), game)) *
          max(map(lambda x: x.get('green', 0), game)))

print("B:", B)
