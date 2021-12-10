from std import *
from statistics import median
import re
import functools
import itertools

DAY = "10"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

data = []
for line in lines(INPUT):
    data.append(line)

tokens = {'(':')','[':']','{':'}','<':'>'}
inverse = {y:x for x,y in tokens.items()}
token_score_a = {')':3, ']': 57, '}': 1197, '>': 25137}
token_score_b = {')':1, ']': 2, '}': 3, '>': 4}

def check_syntax(line):
    stack = []
    for x in line:
        if x in tokens:
            stack.append(x)
            continue
        opening = stack.pop()
        if opening != inverse[x]:            
            return False, token_score_a[x]
    
    score = 0
    for x in reversed(stack):
        score = 5*score + token_score_b[tokens[x]]
    return True, score

score_a = 0
score_b = []

for line in data:
    ret, score = check_syntax(line)
    if not ret:
        score_a += score
    else:
        score_b.append(score)

print("A:", score_a)
print("B:", median(sorted(score_b)))
