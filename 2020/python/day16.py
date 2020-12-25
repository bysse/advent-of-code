from std import *
from year import *
import re
import functools
import itertools

def makeRule(limit):
    return lambda x: (limit[0] <= x and x <= limit[1]) or (limit[2] <= x and x <= limit[3])

const = {}
near=[]
mine = None
mode = 0
for line in lines("../input/input16.txt"):
    if not line:
        mode += 1
        continue
    if mode == 0:
        name = line.split(":")[0]
        limit = ints(line)
        const[name] = makeRule(limit)
    if mode == 1:
        mine = ints(line)
    if mode == 2:
        num = ints(line)
        if num:
            near.append(num)
    

def invalid(n):
    for p in const.values():
        if p(n):
            return False
    return True


valids = []
A = 0
for ticket in near:
    add = True
    for num in ticket:
        if invalid(num):
            A += num
            add = False
    if add:
        valids.append(ticket)

print("A:", A)
valids.append(mine)

def matches(column):
    hits = {}
    for ticket in valids:
        num = ticket[column]
        for n, f in const.items():
            if f(num):
                hits[n] = hits.get(n, 0) + 1
    return hits                

def smallest(m):
    least = (10000,[])
    for k, v in m.items():
        if v < least[0]:
            least = (v, [k])
        elif v == least[0]:
            least[1].append(k)
    return least

columnMap = {}
columns = list(range(len(mine)))

candidates = []
for col in range(len(mine)):
    candidates.append(list(const.keys()))

for i in range(len(mine)):    
    if not columns:
        break
    for column in columns:
        m = matches(column)
        for cname, cnt in m.items():
            if cnt > 0 and cnt != len(valids):
                if cname in candidates[column]:
                    candidates[column].remove(cname)
                    #print("---",cname, "is not a candidate for", column)
    
    #print(candidates)
    remove = True
    while remove:
        remove = False
        for col in range(len(candidates)):
            v = candidates[col]            
            if len(v) == 1:
                name = v[0]
                #print("Found column for", name, "=", col)
                columnMap[name] = col
                remove = True
                for lst in candidates:
                    if name in lst:
                        lst.remove(name)
                columns.remove(col)
                const.pop(name)


prod = 1
for rule in columnMap.keys():
    if rule.startswith("departure"):
        prod *= mine[columnMap[rule]]
print("B:", prod)        

