import re
import sys
import collections 

ops = []
with open('../input-08.txt') as fp:
#with open('../test.txt') as fp:
        for line in fp.readlines():
            ops.append(line.strip().split(" "))


reg = collections.defaultdict(int)

def alu(l, op, r):
    if op == "inc":
        return reg[l] + int(r)
    if op == "dec":
        return reg[l] - int(r)
    raise Exception("Unkown op " + op)

def compare(l, op, r):
    if op == ">":
        return l > int(r)
    if op == ">=":
        return l >= int(r)
    if op == "==":
        return l == int(r)
    if op == "!=":
        return l != int(r)
    if op == "<=":
        return l <= int(r)
    if op == "<":
        return l < int(r)
    raise Exception("Unkown op " + op)


B = 0
for l, op, r, _, cl, cop, v in ops:
    t = alu(l, op, r)    
    if compare(reg[cl], cop, v):
        reg[l] = t
        if t > B:
            B = t

print("A:", max(reg.values()))
print("B:", B)
