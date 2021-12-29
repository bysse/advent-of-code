from std import *
from sortedcontainers import SortedSet
import collections

DAY = "23"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

cost_map= {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
rooms = {'A':[(3,5), (3,4), (3,3), (3,2)], 'B': [(5,5), (5,4), (5,3), (5,2)], 'C': [(7,5), (7,4), (7,3), (7,2)], 'D': [(9,5),(9,4), (9,3),(9,2)] }
invalid = set([(3,1), (5,1), (7,1), (9,1)])

field, _, _ = load2D(INPUT)
state = {}
nodes = set()
edge = collections.defaultdict(dict)

field.insert(3, list("  #D#C#B#A#"))
field.insert(4, list("  #D#B#A#C#"))

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

for n in invalid:
    nodes.remove(n)

def find_path(p0, p1):
    cost_map = {}
    path_map = {}
    frontier = SortedSet(key=lambda x: x[0])
    
    frontier.add((0, p0))
    cost_map[p0] = 0
    path_map[p0] = []

    while frontier:
        c0, p0 = frontier.pop()        
        path0 = path_map[p0]

        for an, ac in edge[p0].items():
            if an in cost_map and cost_map[an] <= c0 + ac:
                continue

            cost_map[an] = c0 + ac
            path_map[an] = path0 + [an]

            if p0 == p1:
                break
            frontier.add((c0 + ac, an))

    return cost_map[p1], path_map.get(p1, None)        

paths = {}
for n0 in nodes:
    for n1 in nodes:
        if n0 == n1:
            continue
        paths[(n0, n1)] = find_path(n0, n1)

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
    cost, nodes = paths[(p0, p1)]
    for node in nodes:
        if node in state:
            return -1
    return cost

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
            skip = False
            for end in rooms[brick]:
                if end in state and state[end][0] != brick:
                    skip = True
                    break
            if not skip:            
                for end in rooms[brick]: # destination rooms
                    cost = valid_move(state, pos, end)
                    if cost > 0:
                        moves.append((brick, pos, end, cost * get_cost(brick)))
                        break
    return moves

def commit(move, state, energy):
    t, p0, p1, cost = move

    S2 = dict(state)
    S2[p1] = (t, state[p0][1] + 1)
    del S2[p0]

    return energy + cost, S2
            
def solve_a(state):           
    queue = set()
    energy = {}

    def insert(state, e):
        id = repr(sorted(state.items()))
        queue.add(id)
        e = min(e, energy[id][0]) if id in energy else e
        energy[id] = (e, state)

    insert(state, 0)

    i = 0
    min_E = -1
    discarded = 0
    P = 1

    while queue:
        P -= 1
        if P <= 0:
            P += 100000
            print("Iteration:", i, len(queue), min_E, discarded)
            
        i += 1
        id = queue.pop()
        E, S = energy[id]
        del energy[id]
        if min_E > 0 and E > min_E:
            discarded += 1
            continue
           
        for move in get_moves(S):
            E2, S2 = commit(move, S, E)
            if end_state(S2):
                if min_E < 0 or E2 < min_E:
                    min_E = E2
                    print("Min =", E2)
            else:
                insert(S2, E2)
    
    return min_E

print("B:", solve_a(state))