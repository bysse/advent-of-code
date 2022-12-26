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
max_width = max([len(x) for x in field])
size = int(max_width / 3)


def is_num(x):
    return ord('0') <= ord(x) <= ord('9')


def get(x, y):
    if x < 0 or y < 0 or y >= len(field):
        return ' '
    if len(field[y]) <= x:
        return ' '
    return field[y][x]


wrap = {
    (1, 2, 0, 0): (0, 0, 3, 4,),
    (2, 3, 0, 0): (0, 1, 4, 4),
    (1, 1, 0, 1): (0, 0, 2, 3),
}

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


def one_step(x, y, facing):
    dx, dy = direction[facing]
    x += dx
    y += dy

    if get(x, y) != ' ':
        return x, y, facing

    if x < 0 and 100 <= y < 150 and facing == LEFT:     # C*
        return 50, 49 - (y - 100), RIGHT
    if x < 0 and 150 <= y < 200 and facing == LEFT:     # E
        return 50 + y - 150, 0, DOWN
    if x < 50 and 0 <= y < 50 and facing == LEFT:       # C*
        return 0, (49-y) + 100, RIGHT
    if x < 50 and 50 <= y < 100 and facing == LEFT:     # D
        return y - 50, 100, DOWN

    if x >= 150 and 0 <= y < 50 and facing == RIGHT:        # A*
        return 99, 100 + (49-y), LEFT
    if x >= 100 and 50 <= y < 100 and facing == RIGHT:      # B
        return 100 + y - 50, 49, UP
    if x >= 100 and 100 <= y < 150 and facing == RIGHT:     # A*
        return 149, 49 - (y - 100), LEFT
    if x >= 50 and 150 <= y < 200 and facing == RIGHT:      # G
        return 50 + y - 150, 149, UP

    if 0 <= x < 50 and y < 100 and facing == UP:        # D
        return 50, 50 + x, RIGHT
    if 50 <= x < 100 and y < 0 and facing == UP:        # E
        return 0, 150 + x - 50, RIGHT
    if 100 <= x < 150 and y < 0 and facing == UP:       # F
        return x - 100, 199, UP

    if 0 <= x < 50 and y >= 200 and facing == DOWN:     # F
        return 100 + x, 0, DOWN
    if 50 <= x < 100 and y >= 150 and facing == DOWN:   # G
        return 49, 150 + x - 50, LEFT
    if 100 <= x < 150 and y >= 50 and facing == DOWN:   # B
        return 99, 50 + x - 100, LEFT

    raise Exception(f"FAIL: {x}, {y} @ {iter}")


direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
token = ['>', 'v', '<', '^']
colors = {
    '>': (200, 0, 0),
    'v': (200, 0, 0),
    '<': (200, 0, 0),
    '^': (200, 0, 0),
    '9': (200, 0, 0),
    '8': (190, 0, 0),
    '7': (180, 0, 0),
    '6': (170, 0, 0),
    '5': (160, 0, 0),
    '4': (150, 0, 0),
    '3': (140, 0, 0),
    '2': (130, 0, 0),
    '1': (120, 0, 0),
    '0': (100, 0, 0),
    " ": (0, 0, 0),
    ".": (20, 20, 20),
    "#": (190, 190, 190),
}

y = 0
x = 50
facing = 0  # 0 = right, 1 = down, etc
cmd = 0
iter = 0
for match in re.finditer('[0-9]+|L|R', ops):
    match match.group(0):
        case 'L':
            facing = (facing - 1) % 4
        case 'R':
            facing = (facing + 1) % 4
        case steps:
            cmd += 1
            for _ in range(int(steps)):
                nx, ny, f2 = one_step(x, y, facing)
                tile = get(nx, ny)
                if tile == '#':
                    break
                x, y, facing = nx, ny, f2

    iter += 1
    if iter > 100000:
        display_2d(field, colors, output=f"images2/frame_{iter}.png", load=False)

    #for fy in range(len(field)):
    #    for fx in range(len(field[fy])):
    #        if ord('1') <= ord(field[fy][fx]) <= ord('9'):
    #            field[fy][fx] = chr(ord(field[fy][fx]) - 1)#


print("B:", 1000 * (y+1) + 4 * (x+1) + facing)
