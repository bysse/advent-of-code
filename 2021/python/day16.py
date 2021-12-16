from std import *
import re
import functools
import itertools

DAY = "16"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

data = []
for line in lines(INPUT):
    if not line:
        continue
    for ch in line:
        x = int(ch, 16)
        for bit in [8,4,2,1]:
            data.append(int(x & bit == bit))
bit_count = 0

def to_dec(seq):
    out = 0
    for bit in seq:
        out = (out << 1) | bit
    return out

def next_header():
    global bit_count, pkg_count
    v = data[bit_count:bit_count+3]
    t = data[bit_count+3:bit_count+6]
    bit_count += 6
    return to_dec(v), to_dec(t)

def next_num(bits=1):
    global bit_count
    n = data[bit_count:bit_count+bits]
    bit_count += bits
    return to_dec(n)

versions = []

def parse(bit_l, pack_l):
    bit0 = bit_count
    pkg_count = 0
    values = []
    while True:
        if (bit_count - bit0) >= bit_l:
            break
        if pack_l >= 0 and pkg_count >= pack_l:
            break
        v, t = next_header()
        versions.append(v)
        pkg_count += 1
        if t == 4: # literal
            literal = 0
            while next_num(1) == 1:
                literal = literal * 16 + next_num(4)
            literal = literal * 16 + next_num(4)
            values.append(literal)
        else:
            length_type = next_num(1)
            bits = bit_l - (bit_count - bit0)
            packets = -1

            if length_type == 0: # length type 0: 15 bits are the total length in bits of the sub-packets contained by this packet.
                bits = next_num(15)
            else: # length_type 1: 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
                packets = next_num(11)

            sub = parse(bits, packets)

            if t == 0:
                values.append(sum(sub))
            elif t == 1:
                values.append(functools.reduce(lambda a,x: a*x, sub))
            elif t == 2:
                values.append(min(sub))
            elif t == 3:
                values.append(max(sub))
            elif t == 5:
                values.append(1 if sub[0] > sub[1] else 0)
            elif t == 6:
                values.append(1 if sub[0] < sub[1] else 0)
            elif t == 7:
                values.append(1 if sub[0] == sub[1] else 0)

    return values
value = parse(len(data), 1)

# too low 191
print("A:", sum(versions))
print("B:", value[0])