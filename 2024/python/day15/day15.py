from collections import deque

from six import moves

from std import *
import copy
import re
import functools
import itertools

MOVES = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1),
}


def parse_move(x):
    return MOVES[x]


def move_boxes(pos, dx, dy, boxes, walls):
    if pos in walls:
        return False
    if pos in boxes:
        np = (pos[0] + dx, pos[1] + dy)
        if not move_boxes(np, dx, dy, boxes, walls):
            return False

        boxes.remove(pos)
        boxes.add(np)
    return True


def solve_a(walls, boxes, robot, moves, width, height):
    for (dx, dy) in moves:
        x, y = robot
        np = (x + dx, y + dy)
        if np in walls:
            continue
        if move_boxes(np, dx, dy, boxes, walls):
            robot = np

    A = 0
    for (x, y) in boxes:
        A += x + 100 * y

    return A


def find_box(x, y, boxes):
    if (x, y) in boxes:
        return x, y, x + 1
    elif (x - 1, y) in boxes:
        return x - 1, y, x
    return None


def move_boxes_b(pos, dx, dy, boxes, walls):
    queue = deque()
    queue.append(pos)

    apply = set()

    while queue:
        pos = queue.pop()
        if pos in walls:
            return False

        hit = find_box(*pos, boxes)
        if not hit:
            continue

        bx0, by, bx1 = hit

        if dx == 0:
            # vertical movement
            queue.append((bx0, by + dy))
            queue.append((bx1, by + dy))
        elif dx < 0:
            queue.append((bx0 - 1, by))
        elif dx > 0:
            queue.append((bx1 + 1, by))

        apply.add((bx0, by))

    for px, py in apply:
        boxes.remove((px, py))
        boxes.add((px + dx, py + dy))
    return True


def solve_b(walls, boxes, robot, moves, width, height):
    index = 0
    for (dx, dy) in moves:
        dump(width, height, walls, boxes, robot)
        print(index, dx, dy)
        index += 1

        x, y = robot
        np = (x + dx, y + dy)
        if move_boxes_b(np, dx, dy, boxes, walls):
            robot = np

    dump(width, height, walls, boxes, robot)
    B = 0
    for (x, y) in boxes:
        B += x + 100 * y

    return B


def dump(width, height, walls, boxes, robot):
    for y in range(height):
        for x in range(width):
            if (x, y) == robot:
                print("@", end="")
            elif (x, y) in walls:
                print("#", end="")
            elif (x, y) in boxes:
                print("[", end="")
            elif (x-1, y) in boxes:
                print("]", end="")
            else:

                print(".", end="")
        print()


def main(input_file):
    f_data, m_data = groups(input_file)

    width = len(f_data[0])
    height = len(f_data)

    robot = None
    boxes = set()
    walls = set()

    for y, line in enumerate(f_data):
        for x, c in enumerate(line):
            if c == "@":
                robot = (x, y)
            if c == "#":
                walls.add((x, y))
            if c == "O":
                boxes.add((x, y))

    moves = []
    for line in m_data:
        for c in line:
            moves.append(parse_move(c))

    #print("A:", solve_a(set(walls), set(boxes), robot, moves, width, height))

    # double the width for everything
    walls2 = set()
    for (x, y) in walls:
        walls2.add((2 * x + 0, y))
        walls2.add((2 * x + 1, y))

    boxes2 = set()
    for (x, y) in boxes:
        boxes2.add((2 * x, y))

    robot2 = (robot[0] * 2, robot[1])


    print("B:", solve_b(walls2, boxes2, robot2, moves, 2 * width, height))


if __name__ == "__main__":
    #main("input.txt")

    main("test.txt")

    # too high: 1526833
