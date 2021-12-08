from std import *
import re
import functools
import itertools

DAY = "08"
#INPUT = "../input/input{}.txt".format(DAY)
INPUT = "../input/test.txt"

display = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
value = [1, 2, 4, 8, 16, 32, 64]

d_value = [
    sum([pow(2, ord(ch) - ord('a')) for ch in x])
    for x in display
]

# which lines are active in a digit
digitmap = [set() for x in range(10)]
for line, x in enumerate("abcdefg"):
    for digit, n in enumerate(display):
        if x in n:
            digitmap[digit].add(x)

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