from std import *


def is_left_turn(a, b, c):
    v1 = (b[0] - a[0], b[1] - a[1])
    v2 = (c[0] - b[0], c[1] - b[1])

    vp1 = (v1[1], -v1[0])
    dot = vp1[0] * v2[0] + vp1[1] * v2[1]
    return dot < 0


def triangle_area(i, j, k):
    ax = i[0] - j[0]
    ay = i[1] - j[1]
    bx = k[0] - j[0]
    by = k[1] - j[1]
    return abs(ax * by - ay * bx) / 2


def is_inside_triangle(a, b, c, x):
    area = triangle_area(a, b, c)
    area -= triangle_area(x, b, c)
    area -= triangle_area(a, x, c)
    area -= triangle_area(a, b, x)
    return area == 0


def is_any_point_inside(data, i, j, k):
    for x in range(len(data)):
        if x == i or x == j or x == k:
            continue

        if is_inside_triangle(data[i], data[j], data[k], data[x]):
            return True
    return False


def triangulate(data):
    triangles = []

    i = 0
    while len(data) >= 3:
        i = i % len(data)
        j = (i + 1) % len(data)
        k = (i + 2) % len(data)

        if is_left_turn(data[i], data[j], data[k]):
            if is_any_point_inside(data, i, j, k):
                i = j
            else:
                triangles.append((data[i], data[j], data[k]))
                del data[j]
        else:
            i += 1
    return triangles


def has_points_inside(data, x1, y1, x2, y2):
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    for x, y in data:
        if x1 < x < x2 and y1 < y < y2:
            return True
    return False


def is_point_inside_triangles(triangles, p):
    for triangle in triangles:
        if is_inside_triangle(triangle[0], triangle[1], triangle[2], p):
            return True
    return False


def has_points_in_triangles(triangles, x1, y1, x2, y2):
    points = [
        (x1, y1),
        (x1, y2),
        (x2, y1),
        (x2, y2)
    ]
    for p in points:
        if not is_point_inside_triangles(triangles, p):
            return False
    return True


def has_edge_in_triangles(triangles, x1, y1, x2, y2):
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    points = []

    for x in range(x1, x2 + 1):
        points.append((x, y1))
        points.append((x, y2))
    for y in range(y1, y2 + 1):
        points.append((x1, y))
        points.append((x2, y))

    for p in points:
        if not is_point_inside_triangles(triangles, p):
            return False
    return True


def segments_intersect(a, b, c, d):
    x1, x2 = min(a[0], b[0]), max(a[0], b[0])
    y1, y2 = min(a[1], b[1]), max(a[1], b[1])
    x3, x4 = min(c[0], d[0]), max(c[0], d[0])
    y3, y4 = min(c[1], d[1]), max(c[1], d[1])

    h1 = y1 == y2
    h2 = y3 == y4

    if h1 and h2:
        return y1 == y3 and x1 < x4 and x3 < x2
    elif not h1 and not h2:
        return x1 == x3 and y1 < y4 and y3 < y2
    elif h1:
        return x1 < x3 < x2 and y3 < y1 < y4
    return x3 < x1 < x4 and y1 < y3 < y2

def has_segments_inside(x1, y1, x2, y2, data):
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    segments = [
        ((x1, y1), (x2, y1)),
        ((x1, y2), (x2, y2)),
        ((x1, y1), (x1, y2)),
        ((x2, y1), (x2, y2)),
    ]

    for i in range(len(data)):
        j = (i + 1) % len(data)
        for a, b in segments:
            if segments_intersect(a, b, data[i], data[j]):
                return True
    return False

def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(tuple(ints(line)))

    A = 0
    B = 0

    for i, (x1, y1) in enumerate(data):
        for j in range(i + 1, len(data)):
            x2, y2 = data[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            A = max(A, area)

    # check if the polygon turns left or right
    turns = 0
    for i in range(len(data)):
        j = (i + 1) % len(data)
        k = (j + 1) % len(data)

        turn = is_left_turn(data[i], data[j], data[k])
        turns += 1 if turn else -1

    if turns < 0:
        raise Exception("Polygon turns right")

    triangles = triangulate(data[:])

    for i, (x1, y1) in enumerate(data):
        print(i)
        for j in range(i + 1, len(data)):
            x2, y2 = data[j]
            if has_points_inside(data, x1, y1, x2, y2):
                continue

            if False:
                if not has_points_in_triangles(triangles, x1, y1, x2, y2):
                    continue

                if not has_edge_in_triangles(triangles, x1, y1, x2, y2):
                    print("  edge outside triangles")
                    continue
            if has_segments_inside(x1, y1, x2, y2, data):
                continue

            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > B:
                print(f"{x1},{y1} - {x2},{y2}", "OK", area)
                B = area

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    #main("input.txt")
    main("test.txt")

# 4586842110 too high

# 1566346198
