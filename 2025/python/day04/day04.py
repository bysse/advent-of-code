from std import *


def main(input_file):
    data = set()
    for y, row in enumerate(lines(input_file)):
        for x, block in enumerate(row):
            if block == '@':
                data.add((x, y))

    A = 0
    B = 0

    for x,y in data:
        count = 0
        for nx, ny in adjacent_2d(x, y):
            if (nx, ny) in data:
                count += 1
        if count < 4:
            A += 1

    while True:
        remove = []
        for x,y in data:
            count = 0
            for nx, ny in adjacent_2d(x, y):
                if (nx, ny) in data:
                    count += 1
            if count < 4:
                B += 1
                remove.append( (x,y) )

        if not remove:
            break

        for pos in remove:
            data.remove(pos)

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
