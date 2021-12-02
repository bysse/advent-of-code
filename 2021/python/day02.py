from std import *
import re
import functools
import itertools

INPUT = "../input/input02.txt"

x = 0
y = 0
for line in lines(INPUT):
    cmd = line.split(" ")
    n = int(cmd[1])
    if cmd[0] == 'forward':
        x += n
    if cmd[0] == 'down':
        y += n
    if cmd[0] == 'up':
        y -= n

print("A:", x * y)

x = 0
y = 0
aim = 0
for line in lines(INPUT):
    cmd = line.split(" ")
    n = int(cmd[1])
    if cmd[0] == 'forward':
        x += n
        y += aim * n
    if cmd[0] == 'down':
        aim += n
    if cmd[0] == 'up':
        aim -= n

print("B:", x * y)
