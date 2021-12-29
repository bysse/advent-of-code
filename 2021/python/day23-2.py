from std import *
from sortedcontainers import SortedList
import re
import collections
import functools
import itertools
import copy

DAY = "23"
INPUT = "../input/input{}.txt".format(DAY)
INPUT = "../input/test.txt"

cost_map= {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
rooms = {'A':[(3,3), (3,2)], 'B': [(5,3), (5,2)], 'C': [(7,3), (7,2)], 'D': [(9,3),(9,2)] }
invalid = set([(3,1), (5,1), (7,1), (9,1)])

field, width, height = load2D(INPUT)
state = {}
nodes = set()
edge = collections.defaultdict(dict)

for x, y, ch in iterate2D(field):
    if ch in cost_map:
        state[(x,y)] = (ch, 0)
        field[y][x] = '.'

for x, y, ch in iterate2D(field):            
    if ch == '.':
        nodes.add( (x,y) )

def explore(node, visited):
    global field, edge
    if node in visited:
        return
    visited.add(node)
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        x = node[0] + dx
        y = node[1] + dy
        if field[y][x] == '.':            
            edge[node][(x,y)] = 1
            edge[(x,y)][node] = 1
            explore((x,y), visited)

visited = set()
for node in nodes:
    explore(node, visited)

for node, adjacent in edge.items():
    if node in invalid:
        for nn, nw in adjacent.items():   
            del edge[nn][node]
            for ad in adjacent.keys():
                if ad != nn:
                    edge[nn][ad] = 2

def end_state(state):
    for t, ps in rooms.items():
        for p in ps:
            if p not in state or state.get(p)[0] != t:
                return False
    return True

def show(state):
    for y, line in enumerate(field):
        for x, ch in enumerate(line):
            print(state.get( (x,y), (ch, 0))[0], end='')
        print()

def get_cost(t):
    return cost_map[t.upper()]

def valid_move(state, p0, p1):
    # check if something could move from p0 to p1
    visited = set()
    frontier = set()
    frontier.add((p0, 0))

    while frontier:
        p0, c0 = frontier.pop()
        if p0 == p1:
            return c0

        for adjacent, cost in edge[p0].items():
            if adjacent in visited or adjacent in state:
                continue
            visited.add(adjacent)
            frontier.add((adjacent, c0 + cost))
    return -1

def get_moves(state):
    moves = []
    for pos, value in state.items():
        brick = value[0]
        if value[1] >= 2:
            continue
        if value[1] == 0:
            # move out
            for end in nodes:
                if end[1] != 1:
                    continue
                cost = valid_move(state, pos, end)
                if cost > 0:
                    moves.append((brick, pos, end, cost * get_cost(brick)))
        else:
            # move in
            for end in rooms[brick]: # destination rooms
                cost = valid_move(state, pos, end)
                if cost > 0:
                    moves.append((brick, pos, end, cost * get_cost(brick)))
                    break
    return moves

def commit(move, state, energy, trail):
    t, p0, p1, cost = move

    S2 = dict(state)
    S2[p1] = (t, state[p0][1] + 1)
    del S2[p0]

    return energy + cost, S2, trail# + [state]
            
def solve_a(state):           
    queue = [ (0, state, []) ]

    i = 0
    min_E = -1

    while queue:
        i += 1
        if i % 10000 == 0:
            print("Iteration:",i, len(queue), min_E)
            show(S)

        E, S, trail = queue.pop()
        if min_E > 0 and E > min_E:
            continue

        #show(S)

        if end_state(S):
            if min_E < 0 or E < min_E:
                min_E = E
                print("Min =", E)
            
        for move in get_moves(S):
            queue.append( commit(move, S, E, trail) )

        if i % 250 == 0:
            queue.sort(key=lambda x: x[0], reverse=True)
    
    return min_E

print("A:", solve_a(state))
#print(end_state(state))
#print("B:")
