from std import *
from year import *
import re
import functools
import itertools


seed = "398254716"
#seed = "389125467" # test

setup = (1000000, 10000000)
#setup = (9, 10)

cups = [int(x) for x in seed]
cmin = min(cups)
cmax = max(cups)

while len(cups) < setup[0]:
    cmax += 1
    cups.append(cmax)

link = [0]*(setup[0]+1)
prev = 0
for j in range(len(cups)):
    link[prev] = cups[j]
    prev = cups[j]
link[prev] = 0


def translate(chain):
    global cups
    n = []
    p = 0
    for _ in range(len(cups)):        
        p = chain[p]
        n.append(p)
    return n

def round2(chain, current):
    pick = []
    lastpick = current
    for _ in range(3):
        lastpick = chain[lastpick]
        if lastpick == 0:
            lastpick = chain[lastpick]
        pick.append(lastpick)

    # relink current
    chain[current] = chain[lastpick]
    
    dest = current - 1
    while True:        
        if dest < cmin:
            dest = cmax
        if dest not in pick:
            break
        dest -= 1

    next = chain[dest]
    chain[dest] = pick[0]
    chain[lastpick] = next

def show(i, link, index):
    print("-- move", i+1,"--")
    n = [("({0})" if x == index else "{0:3d}").format(x) for x in translate(link)]
    print(" ".join(n))

index = link[0]
for i in range(setup[1]):
    #show(i, link, index)
    round2(link, index)
    index = link[index]

a = link[1]
b = link[a]
print(a, b, a*b)

# 10000, 10000 = 525
# - 3.45s
# - 2.20s
