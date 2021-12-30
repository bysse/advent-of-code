from std import *
import re
import functools
import itertools

DAY = "24"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

data = []
for line in lines(INPUT):
    data.append( line.split(' ') )


def execute(ops, inp=[]):
    loc = {'w':0, 'x':1, 'y':2, 'z': 3}
    reg = [0,0,0,0]
    def get_op(v):        
        return reg[loc[v]] if v in loc else int(v)

    for op in ops:
        if op[0] == 'inp':
            v = int(inp.pop(0) if inp else input(">"))
            #print("INPUT", v)
            reg[loc[op[1]]] = v
        elif op[0] == 'add':
            reg[loc[op[1]]] += get_op(op[2])
        elif op[0] == 'mul':
            reg[loc[op[1]]] *= get_op(op[2])
        elif op[0] == 'div':
            reg[loc[op[1]]] = int(reg[loc[op[1]]] / get_op(op[2]))
        elif op[0] == 'mod':
            reg[loc[op[1]]] %= get_op(op[2])
        elif op[0] == 'eql':
            reg[loc[op[1]]] = int(reg[loc[op[1]]] == get_op(op[2]))
        else:
            print("Unknown op", op)
    return reg


weights = [
    ( 11, 14,  1), ( 14,  6,  1), 
    ( 15,  6,  1), ( 13, 13,  1), 
    (-12,  8, 26), ( 10,  8,  1), 
    (-15,  7, 26), ( 13, 10,  1), 
    ( 10,  8,  1), (-13, 12, 26), 
    (-13, 10, 26), (-14,  8, 26), 
    ( -2,  8, 26), ( -9,  7, 26)
]


def pp(n):
    p = 1
    while p < n:
        p *= 26

    p = int(p/26)

    s = ""
    while p > 0:
        d = int(n / p)
        n -= d*p
        p = int(p/26)
        s += str(d) + "-"
    return s

def iterate(inp, A, B, C, z):
    x = z % 26 + A
    x = int(x != inp)
    z = int(z/C)*(25*x + 1) + (inp + B) * x
    return z

def execute2(inp):
    print("{:3} {:3} {:3} {:3}   {:3} {:3} {:12} {}".format(' A', ' B', ' C', 'inp', 'i?', 'inp+B', '     z', 'b26'))
    z = 0    
    for i, w in zip(inp, weights):
        A, B, C = w
        zin = z
        z = iterate(int(i), A, B, C, z)        
        print("{:3} {:3} {:3} {:3}   {:3} {:3} {:12} {}".format(A, B, C, i, zin%26 + A, int(i)+B, z, pp(z)))
    return z

def execute3(index=0, z=0):
    if index >= 14:
        return True, []

    A, B, C = weights[index]
    #print("{:3} {:3} {:3} {:3}   {:12}".format(index, A, B, C, pp(z)))

    if C == 26:
        n = z%26 + A
        if n >= 1 and n <= 9:
            ok, nn = execute3(index+1, iterate(n, A, B, C, z))
            return ok, [n] + nn
        return False, []

    for digit in range(9, 0, -1):
        ok, n = execute3(index+1, iterate(digit, A, B, C, z))
        if ok:
            return True, [digit] + n
    return False, []

def execute4(index=0, z=0):
    if index >= 14:
        return True, []

    A, B, C = weights[index]
    #print("{:3} {:3} {:3} {:3}   {:12}".format(index, A, B, C, pp(z)))

    if C == 26:
        n = z%26 + A
        if n >= 1 and n <= 9:
            ok, nn = execute4(index+1, iterate(n, A, B, C, z))
            return ok, [n] + nn
        return False, []

    for digit in range(1, 10):
        ok, n = execute4(index+1, iterate(digit, A, B, C, z))
        if ok:
            return True, [digit] + n
    return False, []    
   

_, A = execute3(0, 0)
print("A:", "".join(map(str, A)))

_, B = execute4(0, 0)
print("B:", "".join(map(str, B)))