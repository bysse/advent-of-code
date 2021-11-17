input_value = 265149

def step_direction():
    # 1 2 2 3 3 4 4 5 5
    dx, dy = (0, -1)
    step = 0
    yield (0,0,1)
    while True:
        step += 1
        dx, dy = -dy, dx 
        yield (dx, dy, step)
        dx, dy = -dy, dx
        yield (dx, dy, step)

def neighbours(x, y):
    yield (x-1, y-1)
    yield (x-1, y)
    yield (x-1, y+1)
    yield (x  , y-1)
    #yield (x  , y)
    yield (x  , y+1)
    yield (x+1, y-1)
    yield (x+1, y)
    yield (x+1, y+1)

# A
steps = input_value
x, y = (0,0)
for dx, dy, s in step_direction():    
    s = min(s, steps)
    steps -= s
    x += s*dx
    y += s*dy
    if steps <= 0:
        print('A:', abs(x) + abs(y))
        break

# B
field = {}
x, y = (0,0)
initial = 1
value = 0
for dx, dy, s in step_direction():    
    for i in range(0, s):
        x += dx
        y += dy
        value = initial
        for nx, ny in neighbours(x, y):
            value += field.get((nx, ny), 0)
        field[(x, y)] = value
        initial = 0
        if value > input_value:
            print('B:', value)
            break
    if value > input_value:
        break
