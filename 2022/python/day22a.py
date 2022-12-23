from std import *

DAY = "22"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"

done = False
field = []
ops = None
with open(INPUT, 'r') as fd:
    for line in fd.readlines():
        if len(line.strip()) == 0:
            done = True
            continue

        if done:
            ops = line.strip()
        else:
            field.append(list(line[:-1]))
offset = {}
max_width = max([len(x) for x in field])


def is_num(x):
    return ord('0') <= ord(x) <= ord('9')


def get(x, y):
    if len(field[y]) <= x < max_width:
        return ' '
    return field[y][x]


def one_step(x, y, dx, dy):
    state = (x, y, dx, dy)
    if state in offset:
        return offset[state]

    for _ in range(10000):
        x += dx
        y += dy
        if y < 0:
            y += len(field)
        if y >= len(field):
            y -= len(field)
        if x < 0:
            x += len(field[y])
        if x >= max_width:
            x -= max_width
        if get(x, y) == ' ':
            continue
        offset[state] = x, y
        return x, y

    raise Exception("ERROR")




direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
token = ['>', 'v', '<', '^']
colors = {
    '>': (200, 0, 0),
    'v': (200, 0, 0),
    '<': (200, 0, 0),
    '^': (200, 0, 0),
    " ": (0, 0, 0),
    ".": (20, 20, 20),
    "#": (190, 190, 190),
}

y = 0
x = one_step(0, 0, 1, 0)[0]
facing = 0  # 0 = right, 1 = down, etc
index = 0

iter = 0
while True:
    if index >= len(ops):
        break
    if ops[index] == 'R':
        facing = (facing + 1) % 4
        index += 1
        continue
    if ops[index] == 'L':
        facing = (facing - 1) % 4
        index += 1
        continue

    # get the number of steps
    num = ""
    while index < len(ops) and is_num(ops[index]):
        num += ops[index]
        index += 1

    for _ in range(int(num)):
        field[y][x] = token[facing]
        nx, ny = one_step(x, y, *direction[facing])
        tile = get(nx, ny)
        if tile == '#':
            break
        x, y = nx, ny

    #iter += 1
    #display_2d(field, colors, output=f"images/frame_{iter}.png", load=False)

print("A:", 1000 * (y+1) + 4 * (x+1) + facing)
print("B:")
