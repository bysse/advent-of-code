from std import *
import re
import functools
import itertools

DAY = "21"
INPUT = "../input/input{}.txt".format(DAY)
INPUT = "../input/test.txt"

pos = [3, 7] #[4, 8]
pos = [0, 1] #[4, 8]
score = [0, 0]
die = 0
rolls = 0

def cast():
    global die, rolls
    rolls += 1
    d = die
    die = (die + 1) % 100
    return d + 1

index = 0
while True:
    roll = cast() + cast() + cast()
    pos[index] = (pos[index] + roll) % 10
    score[index] += 1 + pos[index]
    #print(index, "ROLL:", roll, "POS:", pos[index], "SCORE:", score[index])
    if score[index] >= 1000:
        break
    index = 1-index

print("A:", score[1-index] * rolls)
