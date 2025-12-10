import heapq

from std import *


def segments_intersect(p1: IVec2, p2: IVec2, p3: IVec2, p4: IVec2) -> bool:
    x1, x2 = min(p1.x, p2.x), max(p1.x, p2.x)
    y1, y2 = min(p1.y, p2.y), max(p1.y, p2.y)
    x3, x4 = min(p3.x, p4.x), max(p3.x, p4.x)
    y3, y4 = min(p3.y, p4.y), max(p3.y, p4.y)

    h1 = p1.y == p2.y
    h2 = p3.y == p4.y

    if h1 and h2 or (not h1 and not h2):
        return False
    elif h1:
        return x1 < x3 < x2 and y3 < y1 < y4
    return x3 < x1 < x4 and y1 < y3 < y2


def intersects(segments, a, b):
    rect_segments = [
        (IVec2(a.x, a.y), IVec2(b.x, a.y)),
        (IVec2(b.x, a.y), IVec2(b.x, b.y)),
        (IVec2(b.x, b.y), IVec2(a.x, b.y)),
        (IVec2(a.x, b.y), IVec2(a.x, a.y))
    ]

    for s in segments:
        for ra, rb in rect_segments:
            if segments_intersect(ra, rb, s[1], s[2]):
                return True
    return False


def contains_any_point(data, a, b):
    x0 = min(a.x, b.x)
    x1 = max(a.x, b.x)
    y0 = min(a.y, b.y)
    y1 = max(a.y, b.y)

    for p in data:
        if x0 < p.x < x1 and y0 < p.y < y1:
            return True
    return False


def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(IVec2(*tuple(ints(line))))

    A = 0
    B = 0

    for i, a in enumerate(data):
        for j in range(i + 1, len(data)):
            d = abs(a - data[j])
            area = (d.x + 1) * (d.y + 1)
            if area > A:
                A = area

    segments = []
    for i, a in enumerate(data):
        j = (i + 1) % len(data)
        d = a - data[j]
        heapq.heappush(segments, (d.x * d.x + d.y * d.y, a, data[j]))

    segments.reverse()
    segments = segments[:100]

    for i, a in enumerate(data):
        for j in range(i+1, len(data)):
            b = data[j]
            d = abs(a - b)
            area = (d.x + 1) * (d.y + 1)

            if contains_any_point(data, a, b):
                continue

            if intersects(segments, a, b):
                continue

            if area > B:
                B = area

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    # main("test.txt")
