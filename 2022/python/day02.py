from std import *
import re
import functools
import itertools

DAY = "02"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

outcome = [
# ME|R  P  S     ENEMY
    [3, 6, 0], # rock
    [0, 3, 6], # paper
    [6, 0, 3], # scissors
]

def score(enemy, me):
    return outcome[enemy][me] + (1 + me)
 
A = 0
B = 0
for line in lines(INPUT):
    enemy = ord(line[0]) - ord('A')
    me    = ord(line[2]) - ord('X')
    A += score(enemy, me)

    B += score(enemy, outcome[enemy].index(me*3))


print("A:", A)
print("B:", B)
