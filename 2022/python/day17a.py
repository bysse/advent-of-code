from std import *

DAY = "17"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

shapes = [
    (4, 1, "####"),
    (3, 3, ".#.###.#."),
    (3, 3, "..#..####"),
    (1, 4, "####"),
    (2, 2, "####"),
]

flow = []
for line in lines(INPUT):
    flow = line

rock_height = 0
field_height = 100
insert = field_height - 3

field = [["." for _ in range(7)] for _ in range(field_height)]


def overlay(w, h, data, x, y):
    i = 0
    for hh in range(h):
        for ww in range(w):
            if data[i] == '#':
                yield x + ww, y + hh
            i += 1


def test_shape(shape, x, y):
    for ox, oy in overlay(*shape, x, y - shape[1]):
        if ox < 0 or ox >= 7 or oy == field_height or field[oy][ox] == '#':
            return False
    return True


def sim(shape, x, y, t):
    while True:
        dx = -1 if flow[t % len(flow)] == '<' else 1
        print(f"Wind({t}): dx={dx}")
        t += 1
        if test_shape(shape, x + dx, y):
            x += dx
            print(f"Move: x + dx = {x}")

        if not test_shape(shape, x, y + 1):
            return x, y, t
        print(f"Down: y = {y+1}")
        y += 1

time = 0
for round in range(2022):
    shape = shapes[round % len(shapes)]
    x, y, time = sim(shape, 2, insert, time)

    for ox, oy in overlay(*shape, x, y - shape[1]):
        field[oy][ox] = '#'

    # adjust insert
    for i, line in enumerate(field):
        if '#' in line:
            insert = i - 3
            break

    if insert <= 25:
        rock_height += 5
        for _ in range(5):
            field.insert(0, ["." for _ in range(7)])
        field = field[:-5]
        insert += 5


print("A:", rock_height + (field_height - insert - 3))
