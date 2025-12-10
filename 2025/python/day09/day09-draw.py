from std import *


def is_left_turn(a: IVec2, b: IVec2, c: IVec2):
    v1 = b - a
    v2 = c - b
    dot = v1.y * v2.x - v1.x * v2.y
    return dot < 0


def make_rect(a, b, c, d):
    return IVec2(min(a.x, b.x, c.x, d.x), min(a.y, b.y, c.y, d.y)), IVec2(max(a.x, b.x, c.x, d.x), max(a.y, b.y, c.y, d.y))

def rectify(data):
    rects = []
    i = 0
    escape = 100000
    while len(data) > 4 and escape > 0:
        escape -= 1
        i = i % len(data)
        j = (i + 1) % len(data)
        k = (j + 1) % len(data)
        l = (k + 1) % len(data)

        a, b, c, d = data[i], data[j], data[k], data[l]

        if a.x == b.x and b.x == c.x:
            del data[j]
            continue
        if a.y == b.y and b.y == c.y:
            del data[j]
            continue

        if is_left_turn(a, b, c) and is_left_turn(b, c, data[l]):
            if c.y == d.y:
                # closing line will be vertical
                if a.x == d.x:
                    rects.append(make_rect(a, b, c, d))
                    del data[max(j, k)]
                    del data[min(j, k)]
                else:
                    way = 1 if a.x > b.x else -1
                    if way * a.x > way * d.x:
                        # extra on top
                        extra = IVec2(d.x, a.y)
                        rects.append(make_rect(extra, b, c, d))
                        data[j] = extra
                        del data[k]
                    else:
                        # extra on bottom
                        extra = IVec2(a.x, d.y)
                        rects.append(make_rect(a, b, c, extra))
                        data[k] = extra
                        del data[j]

            else:
                # vertical
                if a.y == d.y:
                    rects.append(make_rect(a, b, c, d))
                    del data[max(j, k)]
                    del data[min(j, k)]
                else:
                    way = 1 if a.y > b.y else -1
                    if way * a.y > way * d.y:
                        extra = IVec2(a.x, d.y)
                        rects.append(make_rect(extra, b, c, d))
                        data[j] = extra
                        del data[k]
                    else:
                        extra = IVec2(d.x, a.y)
                        rects.append(make_rect(a, b, c, extra))
                        data[k] = extra
                        del data[j]
        i += 1

    return rects

def in_rect(r: tuple[IVec2, IVec2], p: IVec2):
    return r[0].x <= p.x <= r[1].x and r[0].y <= p.y <= r[1].y

def in_rects(rects, p: IVec2):
    for r in rects:
        if in_rect(r, p):
            return True
    return False

def rect_in_rects(rects, p0, p1):
    p2 = IVec2(p0.x, p1.y)
    p3 = IVec2(p1.x, p0.y)

    count = 0
    for p in [p0, p1, p2, p3]:
        for r in rects:
            if in_rect(r, p):
                count += 1
                break
    return count == 4


def point_in_rect(data, i, j):
    x0 = min(data[i].x, data[j].x)
    x1 = max(data[i].x, data[j].x)
    y0 = min(data[i].y, data[j].y)
    y1 = max(data[i].y, data[j].y)

    for k in range(len(data)):
        if k == i or k == j:
            continue

        if x0 < data[k].x < x1 and y0 < data[k].y < y1:
            return True
    return False


def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(IVec2(*tuple(ints(line))))

    A = 0
    B = 0

    for i, p in enumerate(data):
        for j in range(i + 1, len(data)):
            d = abs(p - data[j])
            area = (d.x + 1) * (d.y + 1)
            if area > A:
                A = area

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")

# It's a fucking circle!
# 1566346198 is correct
