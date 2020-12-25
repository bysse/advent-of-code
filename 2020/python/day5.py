from std import *
from functools import reduce

with open("../input/input5.txt", "r") as fd:    
    seats = sorted([reduce(lambda a, x: (a<<1)+(ord(x)%7)%2, line.strip(), 0) for line in fd])
    print("A:", seats[-1])
    print("B:", sum(range(seats[0], seats[-1]+1)) - sum(seats))