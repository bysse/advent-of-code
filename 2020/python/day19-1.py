from std import *
from year import *
import re
import functools
import itertools

rules={}
messages=[]
mode = 0
for line in lines("../input/input19.txt"):
    if not line:
        mode += 1
        continue
    if mode == 0:
        p = line.split(":")
        idx = int(p[0])
        if '"' in p[1]:           
            rules[idx] = ('=', p[1][2])
        else:
            rr = [ints(r) for r in p[1].split("|")]
            rules[idx] = ('m', rr)
    else:
        messages.append(line)


def match(idx, msg, offset=0):
    op, data = rules[idx]
    if op == '=':
        return msg[offset] == data, offset + 1
    
    # branch
    for path in data:
        pos = offset
        ok = False
        for rule in path:
            ok, pos = match(rule, msg, pos)
            if not ok:
                break
        if ok:
            return True, pos
    return False, 0



ac = 0
for msg in messages:
    m, p = match(0, msg)
    if m and p == len(msg):
        ac += 1
        print(m, p, msg)
print("A:", ac)

# 247 too high