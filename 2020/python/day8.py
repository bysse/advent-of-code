from std import *
from year import *
import re
import functools
import itertools
import copy

code=[]
for line in lines("../input/input8.txt"):
    p=line.split(' ')
    code.append([p[0], int(p[1]), 0])


def run(code):
    code = copy.deepcopy(code)
    ip = 0
    acc = 0
    while ip < len(code):
        op, addr, count = code[ip]
        if count > 0:
            return False, acc
        code[ip][2] += 1

        if op == 'acc':
            acc += addr
        if op == 'jmp':
            ip += addr - 1
        ip += 1
    return True, acc

_, a = run(code)
print("A:", a)

for mp in range(len(code)):
    op = code[mp][0]
    if op == 'acc':
        continue
    version = copy.deepcopy(code)
    if op == 'nop':
        version[mp][0] = 'jmp'
    elif op == 'jmp':
        version[mp][0] = 'nop'
    else:
        print("ERROR")

    result, acc = run(version)
    if result:
        print("B:", acc)
        break
