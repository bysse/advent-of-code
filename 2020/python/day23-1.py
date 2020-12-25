from std import *
from year import *
import re
import functools
import itertools


data = "398254716"
#data = "389125467" # test

cups = [int(x) for x in data]

cmin = min(cups)
cmax = max(cups)


def round(cups, index):
    current = cups[index]
    size = len(cups)
    pick = []
    for i in range(3):
        pick.append(cups[(index+i + 1)%size])
    for p in pick:
        cups.remove(p)
    
    dest = current - 1
    while True:        
        if dest < cmin:
            dest = cmax
        if dest not in pick:
            break
        dest -= 1

    i = cups.index(dest)
    cups = cups[0:i+1] + pick + cups[i+1:]
    index = (cups.index(current) + 1) % size

    return cups, index

def show(i, cups, index):
    print("-- move", i+1,"--")
    print(" ".join([("("+str(x)+")") if x == cups[index] else str(x) for x in cups]))


index = 0
for i in range(100):    
    show(i, cups, index)
    cups, index = round(cups, index)


index = cups.index(1)
order = []
for i in range(1, len(cups)):
    order.append(cups[(i+index)%len(cups)])

print("A:", "".join(map(str, order)) )