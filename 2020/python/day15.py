from std import *
from year import *
import re
import functools
import itertools


for line in lines("../input/input15.txt"):
    entries = ints(line)

record = [-1]*30000001

turn = 1
for e in entries[:-1]:
    record[e] = turn
    turn += 1

speak = 0
last = entries[-1]
for turn in range(len(entries)+1, 30000000 + 1):
    speak = turn - record[last] - 1 if record[last] >= 0 else 0
    record[last] = turn - 1        
    last = speak  

print(speak)
