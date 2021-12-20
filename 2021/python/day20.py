from std import *
import re
import functools
import itertools

DAY = "20"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

data = []
lines = list(groups(INPUT))

lookup = [1 if x == '#' else 0 for x in list("".join(lines[0]))]

field = {}
for y, row in enumerate(lines[1]):
    for x, ch in enumerate(row):
        if ch == '#':
            field[ (x, y) ] = 1

def dump(field):
    for y in range(-5, 5):
        for x in range(-5, 10):
            print(field.get( (x,y), '.'), end='')
        print()            

def adjacent(x, y):
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            yield (x+dx, y+dy)

def get_pixel(field, x, y, is_outside, inf_value):
    if is_outside(x, y):
        return inf_value
    elif (x,y) in field:
        return 1
    return 0

def get_number(field, x, y, is_outside, inf_value):
    n = 0
    for nx, ny in adjacent(x, y):        
        n <<= 1
        n += get_pixel(field, nx, ny, is_outside, inf_value)
    return n

def enhance(field, inf_value):
    x0 = min(field.keys(), key=lambda e: e[0])[0]
    x1 = max(field.keys(), key=lambda e: e[0])[0]
    y0 = min(field.keys(), key=lambda e: e[1])[1]
    y1 = max(field.keys(), key=lambda e: e[1])[1]

    is_outside = lambda x, y: x < x0 or x > x1 or y < y0 or y > y1

    field2 = {}
    for y in range(y0-1, y1+2):
        for x in range(x0-1, x1+2):
            n = get_number(field, x, y, is_outside, inf_value)
            if lookup[n]:
                field2[ (x, y) ] = 1
    return field2

inf_value = 0
for i in range(2):
    field = enhance(field, inf_value)
    inf_value = 1 - inf_value

print("A:", len(field))


for i in range(48):
    field = enhance(field, inf_value)
    inf_value = 1 - inf_value

print("B:", len(field))
