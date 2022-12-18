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
        t += 1
        if test_shape(shape, x + dx, y):
            x += dx

        if not test_shape(shape, x, y + 1):
            return x, y, t
        y += 1


def encode(line):
    p = 1
    v = 0
    for n in line:
        v += 0 if n == '.' else p
        p *= 2
    return v


def encode_state(x):
    state = ""
    for line in field:
        state += hex(encode(line))
    return state


def get_height():
    return rock_height + (field_height - insert - 3)


states = set()
repeat = []
height_list = []

time = 0
for round in range(20000):
    shape = shapes[round % len(shapes)]
    x, y, time = sim(shape, 2, insert, time)

    for ox, oy in overlay(*shape, x, y - shape[1]):
        field[oy][ox] = '#'

    # adjust insert
    for i, line in enumerate(field):
        if '#' in line:
            insert = i - 3
            break

    state = encode_state(insert)
    if state in states:
        repeat.append((round, get_height()))
        print(f"Repeat at: {round} = {get_height()}")
        states.clear()
        if len(repeat) > 1:
            break
    states.add(state)

    if len(repeat) > 0:
        height_list.append(get_height() - repeat[0][1])

    if insert <= 25:
        rock_height += 5
        for _ in range(5):
            field.insert(0, ["." for _ in range(7)])
        field = field[:-5]
        insert += 5


cycle_height = rock_height + (field_height - insert - 3)

target = 1000000000000
offset = repeat[0][0]
cycle = repeat[1][0] - repeat[0][0]
change = repeat[1][1] - repeat[0][1]

#print(f"CYCLE:  {offset} + n*{cycle}")
#print(f"HEIGHT: {repeat[0][1]} + n*{change}")

n = int((target - offset - 1)/cycle)
overflow = (target - offset - 1) % cycle
#print(f"N = {n} + {overflow}")
#print(f"height@{overflow} = {height_list[overflow]}")


print("B:", repeat[0][1] + n * change + height_list[overflow])
#print("   1514285714288")

# 1514285714288
# 1514285714294