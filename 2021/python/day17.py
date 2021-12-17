from std import *
import re
import math
import functools
import itertools

DAY = "17"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

for line in lines(INPUT):
    a, b, c, d = ints(line)
    x0 = min(a, b)
    x1 = max(a, b)
    y0 = min(c, d)
    y1 = max(c, d)

def sim_y(y0, y1):
    results = []

    for yv0 in range(-500, 500):
        yv = yv0
        y = 0
        y_max = y
        for _ in range(500):
            y += yv
            y_max = max(y, y_max)
            if y0 <= y and y <= y1:
                results.append((yv0, y_max))
                break
            if y < y0:
                break
            yv -= 1
    return results

def sim(xv, yv, x0, x1, y0, y1):
    x, y = 0, 0
    for _ in range(xv+500):
        x += xv
        y += yv

        if x0 <= x and x <= x1 and y0 <= y and y <= y1:
            return True
        if x > x1:
            break
        if y < y0:
            break

        yv -= 1
        if xv > 0:
            xv -= 1

    return False

#print("Target: X=[{}, {}] Y=[{}, {}]".format(x0, x1, y0, y1))
velocities = sim_y(y0, y1)

print("A:", sorted(velocities, key=lambda x: x[1])[-1][1])


xv0 = math.floor(math.sqrt(8*x0+1)/2.0 + 0.5)
xv1 = x1

T = []
count = 0
for yv, _ in velocities:    
    for xv in range(xv0, xv1+1):    
        if sim(xv, yv, x0, x1, y0, y1):
            T.append("{},{}".format(xv,yv))
            count += 1

print("B:", count)