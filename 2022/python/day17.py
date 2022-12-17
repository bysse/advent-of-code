from std import *
import copy
import re
import functools
import itertools

DAY = "17"
INPUT = "../input/input{}.txt".format(DAY)
# INPUT = "../input/test.txt"

shapes = {
    (4, 1, "####"),
    (3, 3, ".#.###.#."),
    (3, 3, "..#..####"),
    (1, 4, "####"),
    (2, 2, "####"),
}

flow = []
for line in lines(INPUT):
    flow = line

height = 25
field = [["."]*7]*height
wind = 0
insert = height - 3


def sim(w, h, data, y):
    pass


for round in range(2022):
    shape = shapes[round % len(shapes)]
    sim(*shape, insert)

print("A:")
print("B:")
