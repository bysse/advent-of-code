from std import *
import copy
import re
import functools
import itertools

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


def main(input_file):
    pieces = []
    boards = []
    for group in groups(input_file):
        if 'x' in group[0]:
            for board in group:
                x,y,*r = ints(board)
                boards.append( (x,y,r) )
        else:
            pieces.append(group[1:])

    A = 0
    B = 0

    show_piece(pieces[0])
    #show_piece(flip(pieces[0], True))
    #show_piece(flip(pieces[0], False))
    #show_piece(rotate(pieces[0], 3))

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    # main("input.txt")
    main("test.txt")
