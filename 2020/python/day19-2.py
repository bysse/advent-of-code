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
        if idx == 8:
            p[1] = " 42 | 42 8"
        if idx == 11:
            p[1] = " 42 31 | 42 11 31"
        if '"' in p[1]:           
            rules[idx] = ('=', p[1][2])
        else:
            rr = [ints(r) for r in p[1].split("|")]
            rules[idx] = ('m', rr)
    else:
        messages.append(line)


def rulematch(rule, msg, positions):
    ret = set()
    for pos in positions:
         ok, pp = match(rule, msg, pos)
         if ok:
             for p in pp:
                 ret.add(p)
    return len(ret) > 0, list(ret)

def match(idx, msg, offset=0):
    op, data = rules[idx]
    if op == '=':
        if offset >= len(msg):
            return False, 'EOF'
        return msg[offset] == data, [offset + 1]
    
    # branch
    positions = []
    for path in data:
        pos = [offset]
        ok = False
        for rule in path:
            ok, pos = rulematch(rule, msg, pos)
            if not ok:
                break
        if ok:
            positions += pos

    if positions:
        return True, positions    
    return False, 'dead branch'



if True:
    ac = 0
    for msg in messages:
        m, p = match(0, msg)
        if m and len(msg) in p:            
            ac += 1
            print(m, p, len(msg), msg)
    print("A:", ac)


# 275 too low