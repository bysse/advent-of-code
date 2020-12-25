from std import *
from year import *
import re
import functools
import itertools

def notnum(s):
    return s == '+' or s == '*' or s == '(' or s == ')'

def isnum(ch):
    return not notnum(ch)

def adds(s):
    for i in range(1, len(s)-1):
        if s[i] == '+' and isnum(s[i-1]) and isnum(s[i+1]):
            return True, s[0:i-1] + [int(s[i-1]) + int(s[i+1])] + s[i+2:]
    return False, s

def muls(s):
    for i in range(1, len(s)-1):
        if s[i] == '*' and isnum(s[i-1]) and isnum(s[i+1]):
            return True, s[0:i-1] + [int(s[i-1]) * int(s[i+1])] + s[i+2:]
    return False, s    

def expr(s):
    changed = True
    while changed:
        changed, s = adds(s)
        
    changed = True
    while changed:
        changed, s = muls(s)
    return s

def paren(s):
    prev = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            prev = i
        if s[i] == ')':
            ret = expr(s[prev+1:i])
            return True, s[0:prev] + ret + s[i+1:]
    return False, s

def solve(s):
    s = [x for x in s.replace(' ', '')]
    changed = True
    while changed:
        changed, s = paren(s)     
    return expr(s)

B = 0
for line in lines("../input/input18.txt"):
    print(line)
    B += solve(line)[0]
print("B:", B)