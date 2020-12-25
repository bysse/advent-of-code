from std import *

data = []
for line in lines("../input/input3.txt"):
    data.append(line)


def slope(dx, dy):
    x = 0
    tree = 0
    for y in range(0, len(data), dy):
        if data[y][x] == '#':
            tree += 1
        x = (x + dx) % len(data[y])

    return tree    

def partA():
    return slope(3,1)

def partB():
    return slope(1,1)*slope(3, 1)*slope(5, 1)*slope(7, 1)*slope(1, 2)

print("A:", partA())
print("B:", partB())

