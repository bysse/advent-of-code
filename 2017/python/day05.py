#!/bin/python3
with open("../input-05.txt") as fp:
    jumps = [int(x) for x in fp.readlines()]

ip = 0
step = 0
while ip >= 0 and ip < len(jumps):
    jump = jumps[ip]
    jumps[ip] = jump + 1
    ip += jump
    step += 1
print("A:", step)


with open("../input-05.txt") as fp:
    jumps = [int(x) for x in fp.readlines()]

ip = 0
step = 0
while ip >= 0 and ip < len(jumps):
    jump = jumps[ip]
    jumps[ip] = (jump - 1) if jump >= 3 else jump + 1
    ip += jump
    step += 1
print("B:", step)