from std import *
import re
import functools
import itertools
import copy

DAY = "23"
INPUT = "../input/input{}.txt".format(DAY)
INPUT = "../input/test.txt"

cost_map= {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
rooms = {'a':[(3,2), (3,3)], 'b': [(5,2), (5,3)], 'c': [(7,2), (7,3)], 'd': [(9,2),(9,3)] }
forbidden = set([(3,1), (5,1), (7,1), (9,1)])
forbidden_c = set([(3,2), (5,2), (7,2), (9,2)])


data, width, height = load2D(INPUT)
pieces = {}
for x, y, ch in iterate2D(data):
    if ch in cost_map:
        pieces[(x,y)] = ch
        data[y][x] = '.'

def get(field, state, x, y):
    return state.get( (x,y), field[y][x])

def end_state(state):
    for t, ps in rooms.items():
        for p in ps:
            if state.get(p, ' ') != t:
                return False
    return True

def show(field, state):
    for y, line in enumerate(field):
        for x, ch in enumerate(line):
            print(state.get( (x,y), ch), end='')
        print()

def get_cost(t):
    return cost_map[t.upper()]

state = dict(pieces)
field = copy.copy(data)

def valid_moves(field, state, x, y, visited=None, length=0):
    if not visited:
        visited = {}

    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        np = (nx, ny)
        if np in visited or field[ny][nx] == '#' or np in state:
            continue
        visited[np] = length
        valid_moves(field, state, nx, ny, visited, length+1)            
    return visited

def get_sorted_moves(field, state):
    moves = []
    for p, t in state.items():
        found = valid_moves(field, state, *p)

        for f in forbidden:
            if f in found:
                del found[f]
        if t.isupper():
            for f in forbidden_c:
                if f in found:
                    del found[f]

        for pos, length in found.items():
            if t.islower() and pos not in rooms[t]:
                    continue
            moves.append( [length*get_cost(t), p, pos, t] )
    return sorted(moves, key=lambda x: x[0])


def solve_a(field, state, energy=0):   
    if end_state(state):
        print(energy)
        return True

    #show(field, state)
    for cost, p0, p1, t in get_sorted_moves(field, state):
        s2 = dict(state)
        del s2[p0]

        if t.isupper():
            s2[p1] = t.lower()
            solve_a(field, s2, energy + cost)

print("A:", solve_a(field, state))
print("B:")
