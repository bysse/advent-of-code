from std import *
from year import *
import re
import math
import functools
import itertools


ll = [line for line in lines("../input/input13.txt")]
ts = int(ll[0])
ids = ints(ll[1])

result=[]
for id in ids:
    result.append( (math.ceil(ts/id)*id - ts, id) )

m = min(result)
print("A:", m[0]*m[1])


ids = []
for x in ll[1].split(","):
    if x == 'x':
        ids.append('x')
    else:
        ids.append(int(x))

v = ids[0]
mid = 0

incs = []
p = 1
for i in ids:
    if i != 'x':
        p = lcd(p, i)
        incs.append(p)
    else:
        incs.append(p)
    

def matches(value, ids):
    for i in range(len(ids)):
        if ids[i] == 'x':
            continue
        if (v+i) % ids[i] == 0:
            continue
        return False, i - 1
    return True, 0

for i in range(1000):
    ok, index = matches(v, ids)
    if ok:
        print("B:", int(v))
        break
    mid = max(mid, index)
    v += incs[mid]

#for i in range(len(ids)):
    #if ids[i] == 'x':
        #continue
    #print("{3}: {0} mod {1} = {2}".format(v+i, ids[i], (v+i) % ids[i], i))