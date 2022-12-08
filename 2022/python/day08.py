from std import *

DAY = "08"
INPUT = "../input/input{}.txt".format(DAY)
INPUT = "../input/test.txt"

field = []
for line in lines(INPUT):
    field.append([int(x) for x in line.strip()])


def look(x, y, dx, dy):
    height = -1
    size = len(field)
    visible = set()

    while 0 <= x < size and 0 <= y < size:
        if field[y][x] > height:
            visible.add((x, y))
            height = field[y][x]
        x += dx
        y += dy

    return visible


size = len(field)
visible = set()

for i in range(size):
    visible.update(look(i, 0, 0, 1))
    visible.update(look(i, size - 1, 0, -1))
    visible.update(look(0, i, 1, 0))
    visible.update(look(size - 1, i, -1, 0))

print("A:", len(visible))


def view(x, y, dx, dy):
    height = field[y][x]
    size = len(field)
    count = 0

    while 0 <= x < size and 0 <= y < size:
        if field[y][x] >= height:
            break
        count += 1
        x += dx
        y += dy
    return count


h_score = -1
for y in range(size):
    for x in range(size):
        score = 1
        score *= view(x, y, 1, 0)
        score *= view(x, y, -1, 0)
        score *= view(x, y, 0, 1)
        score *= view(x, y, 0, -1)

        if score > h_score:
            h_score = score

print("B:", h_score)
