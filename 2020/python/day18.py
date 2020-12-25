from std import *
from year import *
import re
import functools
import itertools

def isnum(ch):
    return ord('0') <= ord(ch) and ord(ch) <= ord('9')

def tokens(s):
    s = s.replace(" ", "")
    token = ""
    num = False
    for ch in s:
        if ch == '+' or ch == '*' or ch == '(' or ch == ')':
            if token:
                yield token
            token = ch
            num = False            
        elif isnum(ch):
            if not num:
                if token:
                    yield token
                token = ''
            num = True
            token += ch
    if token:
        yield token


def eval(it):
    left = None
    op = None
    try:    
        while tkn := next(it):        
            if tkn == ')':
                return left
            if tkn == '(':
                tkn = eval(it)
            if tkn == '+' or tkn == '*':
                op = tkn
                continue
            if not left:
                left = int(tkn)
            else:
                if op == '+':
                    left += int(tkn)
                elif op == '*':
                    left *= int(tkn)
                else:
                    raise Exception("invalid op")
                op = None
    except StopIteration:
        pass                
    return left

A = 0
for line in lines("../input/input18.txt"):
    A += eval(tokens(line))
print("A:", A)

