import pygame

from std import *


def evaluate(robots, turns, width, height):
    pos = set()
    for robot in robots:
        x = (robot[0] + turns * robot[2]) % width
        y = (robot[1] + turns * robot[3]) % height
        pos.add((x, y))
    return pos


def is_tree(pos, width, height):
    count = 0
    for x, y in pos:
        if 35 <= x <= 67 and 45 <= y <= 78:
            count += 1

    return count > 320


def main(input_file):
    robots = []
    for line in lines(input_file):
        robots.append(ints(line))

    width = 101
    height = 103
    turns = 100
    cx = width // 2
    cy = height // 2

    quadrant = [0, 0, 0, 0]

    for robot in robots:
        x = (robot[0] + turns * robot[2]) % width
        y = (robot[1] + turns * robot[3]) % height
        if x == cx or y == cy:
            continue
        index = (0 if x < cx else 1) + (0 if y < cy else 2)
        quadrant[index] += 1

    A = quadrant[0] * quadrant[1] * quadrant[2] * quadrant[3]
    print("A:", A)

    pygame.init()
    window = pygame.display.set_mode((2 * width, 2 * height))

    pos = evaluate(robots, 18261, width, height)
    is_tree(pos, width, height)

    turns = 1
    run = True
    found = False
    while run:
        if not found:
            turns += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pos = evaluate(robots, turns, width, height)
        if not is_tree(pos, width, height):
            continue

        found = True
        window.fill(0x00)
        rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size())//2]*2))
        for i in range(width):
            window.set_at((rect.left+i, rect.top-1), 0xffffff)
        for x, y in pos:
            window.set_at((rect.left + x, rect.top + y), 0xff00)

        pygame.image.save(window, f"frame_{turns}.png")
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main("input.txt")
    # main("test.txt")
