from std import *
import re
import functools
import itertools

DAY = "13"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

G = list(groups(INPUT))
dots = [ints(x) for x in G[0]]
folds = [extract(x, r"([xy])=(\d+)") for x in G[1]]
data = set()

A = None
for axis, s_position in folds:    
    position = int(s_position)    
    for x, y in dots: 
        if axis == "x" and x >= position:
            x = 2*position - x            
        if axis == "y" and  y >= position:
            y = 2*position - y
        data.add( (x, y) )  
    dots, data = data, set()
    
    if not A:
        A = len(dots)

print("A:", A)
print("B: ->")
for y in range(7):
    for x in range(40):
        print('#' if (x,y) in dots else '.', end='')
    print()