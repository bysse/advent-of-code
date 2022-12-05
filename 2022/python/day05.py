from std import *
import copy

DAY = "05"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

with open(INPUT) as fd:
    data = fd.read().rstrip()

field_data, move_data = [g.split("\n") for g in data.split("\n\n")]
cols = max(ints(field_data[-1]))

field = [[] for x in range(cols)]
for line in field_data[:len(field_data) - 1]:
    for i in range(cols):
        index = 1 + 4*i
        if index < len(line) and line[index] != ' ':
            field[i].insert(0, line[index])

a_field = copy.deepcopy(field)
b_field = copy.deepcopy(field)

for move in move_data:
    n, src, dst = ints(move)

    for _ in range(n):
        a_field[dst-1].append(a_field[src-1].pop())

    b_field[dst-1] += b_field[src-1][-n:]
    b_field[src-1] = b_field[src-1][:-n]


A = "".join([x[-1] for x in a_field])
B = "".join([x[-1] for x in b_field])

print("A:", A)
print("B:", B)
