from std import *
import copy
import re
import functools
import itertools

DAY = "14"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

segments = []
for line in lines(INPUT):
    segments.append([tuple(ints(x)) for x in line.split("->")])

# find dimensions
x0 = min([min([x[0] for x in s]) for s in segments])
x1 = max([max([x[0] for x in s]) for s in segments])
y0 = 0
y1 = max([max([x[1] for x in s]) for s in segments])
# width = (x1 - x0) + 2
height = (y1 - y0) + 2
width = 2*y1 + 4
x0 = 500 - y1 - 2


# Sand source
source = (500-x0, 0)

field = []
for _ in range(height):
    field.append(['.']*width)


# draw field
def line(a, b):
    try:
        if a[1] == b[1]:
            line_start = min(a[0], b[0])
            for x in range(abs(b[0]-a[0])+1):
                field[a[1]][x+line_start-x0] = '#'
        else:
            line_start = min(a[1], b[1])
            for y in range(abs(b[1]-a[1])+1):
                field[y+line_start][a[0]-x0] = '#'
    except IndexError:
        print(f"X:{x0}-{x1} Y:{y0}-{y1}")
        raise Exception(f"{a}-{b}")


for points in segments:
    p0 = points[0]
    for p in points[1:]:
        line(p0, p)
        p0 = p


def get(x, y):
    return field[y][x]


def set(x, y, ch):
    field[y][x] = ch


def time_step_a():
    x = source[0]
    y = source[1]

    for _ in range(10000):
        if x < 0 or x >= width or y+1 >= height:
            return False

        if get(x, y+1) == '.':
            y += 1
        elif get(x-1, y+1) == '.':
            x -= 1
            y += 1
        elif get(x+1, y+1) == '.':
            x += 1
            y += 1
        else:
            set(x, y, 'o')
            return True


def solve(func):
    time = 0
    for sand in range(100000):
        if get(*source) != '.':
            return sand

        if not func():
            return sand

    return -1


A = solve(time_step_a)
print("A:", A)


def time_step_b():
    x = source[0]
    y = source[1]

    for _ in range(10000):
        if x < 0 or x >= width:
            return False

        if y+1 == height:
            set(x, y, 'o')
            return True
        elif get(x, y+1) == '.':
            y += 1
        elif get(x-1, y+1) == '.':
            x -= 1
            y += 1
        elif get(x+1, y+1) == '.':
            x += 1
            y += 1
        else:
            set(x, y, 'o')
            return True


B = solve(time_step_b)
print("B:", A + B)
