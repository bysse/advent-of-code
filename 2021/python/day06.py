from std import *
import re
import functools
import itertools

INPUT = "../input/input06.txt"
#INPUT = "../input/test.txt"

for line in lines(INPUT):
    age = ints(line)

fish = {}
for i in range(0, 9):
    fish[i] = age.count(i)


def iterate(fish, iterations):
    for iteration in range(iterations):
        new = {}
        new[8] = fish[0]
        new[6] = fish[0]
        for i in range(1, 9):        
            new[i-1] = fish[i] + new.get(i-1, 0)    
        fish = new
    return sum(fish.values())

print("A:", iterate(dict(fish), 80))
print("B:", iterate(dict(fish), 256))