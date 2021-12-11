from std import *
import re
import functools
import itertools

DAY = "11"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

data = []
for line in lines(INPUT):
    data.append([int(x) for x in line])


def iterate(field):
    for row in field:
        for i in range(10):
            row[i] += 1
    
    flash = set()

    for y in range(10):
        row = field[y]
        for x in range(10):
            if row[x] > 9:
                flash.add( (x, y) )

    flash_count = 0    
    while len(flash):
        x, y = flash.pop()
        field[y][x] = -1000
        flash_count += 1
        for ax, ay in adjacent2D(x, y, 10, 10):
            field[ay][ax] += 1
            if field[ay][ax] > 9:
                flash.add( (ax, ay) )
    
    for y in range(10):
        row = field[y]
        for x in range(10):
            if row[x] < 0:
                row[x] = 0
    return flash_count

count = 0
for _ in range(100):
    count += iterate(data)

print("A:", count)

step = 0
for i in range(1, 1000):
    num = iterate(data)
    if num == 100:
        step = 100 + i
        break

print("B:", step)