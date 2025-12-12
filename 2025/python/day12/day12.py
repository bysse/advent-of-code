from typing import Set

from std import *


class Board:
    def __init__(self, size: IVec2, free: Set[tuple[int, int]] = None):
        self.size = size
        if free is None:
            self.free = set([(x, y) for x in range(size.x) for y in range(size.y)])
        else:
            self.free = free

    def apply(self, delta: tuple[int, int], positions: Set[tuple[int, int]]):
        for x, y in positions:
            self.free.remove((x + delta[0], y + delta[1]))

    def is_open(self, delta: tuple[int, int], positions: Set[tuple[int, int]]):
        for x, y in positions:
            if (x + delta[0], y + delta[1]) not in self.free:
                return False
        return True

    def key(self):
        return tuple(sorted(self.free))

    def clone(self):
        return Board(self.size, self.free.copy())

    def find_positions(self, combination):
        for dx, dy in self.free:
            if dx + 3 < self.size.x and dy + 3 < self.size.y:
                if self.is_open((dx, dy), combination):
                    yield dx, dy


def show_piece(piece):
    for line in piece:
        print(line)
    print()


def flip(piece, horizontal):
    if horizontal:
        return [line[::-1] for line in piece]
    else:
        return piece[::-1]


def rotate(piece, turns):
    turns = turns % 4
    if turns == 0:
        return piece

    for _ in range(turns):
        piece = [''.join(row) for row in zip(*piece[::-1])]
    return piece


def add_piece(variations, piece):
    for variation in variations:
        if variation == piece:
            return
    variations.append(piece)


def convert(piece):
    coords = set()
    for y, line in enumerate(piece):
        for x, char in enumerate(line):
            if char == '#':
                coords.add((x, y))
    return coords


def fits(board, piece, dx, dy):
    for (x, y) in piece:
        if (x + dx, y + dy) in board:
            return False
    return True


def apply_to_board(board, combination, position):
    new_board = board.copy()
    for (x, y) in combination:
        new_board.add((x + position[0], y + position[1]))
    return new_board


def solve_a(template, combinations):
    # get a list of actual pieces
    queue = []
    size = IVec2(template[0][0], template[0][1])
    board = Board(size)
    for piece_num, n in enumerate(template[1]):
        for _ in range(n):
            queue.append(piece_num)


    if len(queue) * 9 <= size.x * size.y:
        return True

    if sum([len(combinations[x]) for x in queue]) > size.x * size.y:
        return False

    return False

    memory = set()

    def solve(queue_index: int, board: Board):
        if queue_index >= len(queue):
            return True

        key = board.key()
        if key in memory:
            return False

        piece_index = queue[queue_index]

        for combination in combinations[piece_index]:
            for position in board.find_positions(combination):
                cloned_board = board.clone()
                cloned_board.apply(position, combination)
                if solve(queue_index + 1, cloned_board):
                    return True

        memory.add(key)

        return False

    return solve(0, board)


def main(input_file):
    pieces = []
    boards = []
    for group in groups(input_file):
        if 'x' in group[0]:
            for board in group:
                x, y, *r = ints(board)
                boards.append(((x, y), r))
        else:
            pieces.append(group[1:])

    combinations = []
    for piece in pieces:
        variations = []
        for rotation in range(4):
            rotated_piece = rotate(piece, rotation)
            add_piece(variations, rotated_piece)
            add_piece(variations, flip(rotated_piece, False))
            add_piece(variations, flip(rotated_piece, True))

        combinations.append([convert(x) for x in variations])

    A = 0
    B = 0

    for i, board in enumerate(boards):
        print("Solving", i)
        if solve_a(board, combinations):
            print("  OK")
            A += 1
        else:
            print("  NOT OK")

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
