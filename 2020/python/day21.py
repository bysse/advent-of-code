from std import *
from year import *
import re
import functools
import itertools

prod = 0
data = {}
raw = {}
words = set()
for line in lines("../input/input21.txt"):
    p = line.split("(")
    content = set([x.strip() for x in p[0].strip().split(" ")])
    named = set([x.strip() for x in p[1].replace(")","").replace(",", "").replace("contains", "").strip().split(" ")])

    for n in named:
        if n in data:
            data[n] &= content
        else:
            data[n] = set(content)
    
    for c in content:
        raw[c] = raw.get(c, 0) + 1
    
    words |= content
    prod += 1

def getAllergens(word):
    result=set()
    for alg, poss in data.items():
        if word in poss:
            result.add(alg)
    return result

unsafe = {}
safe = set()
for word in words:
    lst = getAllergens(word)
    if not lst:
        safe.add(word)
    else:
        unsafe[word] = lst
    
count = 0
for s in safe:
    count += raw[s]

print("A:", count)

result={}
loops = len(unsafe)
for j in range(loops):
    for i, l in unsafe.items():
        if len(l) == 1:
            allergen = list(l)[0]
            result[i] = allergen
            unsafe.pop(i)
            for ll in unsafe.values():
                if allergen in ll:
                    ll.remove(allergen)
            break

print("B:", ",".join([x[0] for x in sorted(result.items(), key=lambda x: x[1])]))
