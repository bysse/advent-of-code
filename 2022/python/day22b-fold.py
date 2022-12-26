import math

from std import *

DAY = "22"
INPUT = f"../input/input{DAY}.txt"
INPUT = "../input/test.txt"

done = False
ops = None
with open(INPUT, 'r') as fd:
    data = fd.read()

field, instructions = data.split("\n\n")
size = int(math.sqrt(len([x for x in field if x in '.#']) / 6))
field = field.split('\n')


def get(x, y):
    return ' ' if y >= len(field) or x >= len(field[y]) else field[y][x]


tiles = []
for i in range(16):
    x, y = i % 4, i // 4
    tiles.append(get(x * size, y * size) != ' ')

face = {}
face_inv = {}
rect = {}


def fold(tx, ty, sx: Vec3, sy: Vec3):
    if tx < 0 or ty < 0 or tx >= 4 or ty >= 4:
        return
    index = tx + ty * 4
    if not tiles[index]:
        return
    tiles[index] = False

    # calculate the mapping
    face[(tx, ty)] = (sx, sy)
    rect[(tx, ty)] = (tx * size, ty * size, (1 + tx) * size, (1 + ty) * size)
    face_inv[(sx, sy)] = (tx, ty)

    # recurse
    fold(tx - 1, ty, sy @ sx, sy)
    fold(tx + 1, ty, sx @ sy, sy)
    fold(tx, ty + 1, sx, sy @ sx)


# TODO: we need to keep track of the position of the face as well
tx, ty = tiles.index(1) % 3, tiles.index(1) // 3
fold(tx, ty, Vec3(1, 0, 0), Vec3(0, 1, 0))


def step(steps, u, v, du, dv, x3, y3):
    u0 = (u // size) * size
    v0 = (v // size) * size
    for _ in range(steps):
        if get(u + du, v + dv) == '#':
            break

        u += du
        v += dv

    return u, v, du, dv, x3, y3


def main():
    u, v = tx * size, ty * size
    du, dv = 1, 0
    x3, y3 = Vec3(1, 0, 0), Vec3(0, 1, 0)

    for match in re.finditer('[0-9]+|L|R', instructions):
        match match.group(0):
            case 'L':
                du, dv = -dv, du
            case 'R':
                du, dv = dv, -du
            case steps:
                u, v, du, dv, x3, y3 = step(int(steps), u, v, du, dv, x3, y3)


for (tx, ty), (sx, sy) in face.items():
    x0 = tx * size
    y0 = ty * size

    print(f"if {x0} <= x < {x0+size} and y == {y0-1} and facing == UP:")
    print(face_inv[(sx, sy @ sx)])

