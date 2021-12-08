from std import *
import re
import functools
import itertools

DAY = "08"
#INPUT = "../input/input{}.txt".format(DAY)
INPUT = "../input/test.txt"

display = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
linemap = [0]*10
for x in "abcdefg":
    for i, n in enumerate(display):
        if x in n:
            S = linemap.get(x, set())
            S.add(i)
            linemap[x] = S
print(linemap)

data = []
for line in lines(INPUT):    
    entry = [x.strip().split(' ') for x in line.split('|')]
    data.append([[set(digit) for digit in part] for part in entry])

count = {}
for entry in data:
    for digit in entry[1]:
        if len(digit) == 2:
            count[1] = 1 + count.get(1, 0)
        if len(digit) == 4:
            count[4] = 1 + count.get(4, 0)
        if len(digit) == 3:
            count[7] = 1 + count.get(7, 0)
        if len(digit) == 7:
            count[8] = 1 + count.get(8, 0)

print("A:", sum(list(count.values())))


def analyse(seq):
    mapping = [set() for x in range(10)]
    for digit in seq:
        if len(digit) == 2:
            mapping[1] = digit
        elif len(digit) == 4:
            mapping[4] = digit
        elif len(digit) == 3:
            mapping[7] = digit
        elif len(digit) == 7:
            mapping[8] = digit

    print(mapping)
    pass



for entry in data:
    analyse(entry[0] + entry[1])


print("B:")

