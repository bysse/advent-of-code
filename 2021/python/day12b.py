from std import *
import re
import functools
import itertools

DAY = "12"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

nodes = {} # node -> children
big = set()
small = set()
ticket = {} # node -> tickets

def connect(a, b):
    nodes[a] = nodes.get(a, set()).union(set({b}))
    nodes[b] = nodes.get(b, set()).union(set({a}))

def create(ns):
    for n in ns:
        if n not in nodes:
            nodes[n] = set()            
        ticket[n] = 1

for line in lines(INPUT):
    a, b = line.split('-')
    connect(a, b)
    create([a, b])    

    if a.isupper():
        big.add(a)
    else:
        small.add(a)

    if b.isupper():
        big.add(b)
    else:
        small.add(b)


for node in big:
    ticket[node] = len(nodes[node]) + 100


def find_paths(visited, node, tab=""):
    path = node
    paths = []    
    tab += "  "
    for child in nodes[node]:
        V = dict(visited)
        if child == 'start':
            continue
        if child == 'end':
            paths.append(path + ",end")
            continue            
        if V[child] > 0:
            V[child] -= 1
            for subpath in find_paths(V, child, tab):
                paths.append(path + ","+subpath)
    return paths


all_paths = set()
for exception in small:
    T = dict(ticket)
    T[exception] = 2
    all_paths |= set(find_paths(T, "start"))
    
#print("\n".join(sorted(all_paths)))
print("B:", len(all_paths))