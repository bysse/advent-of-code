from std import *
import sys

INPUT = "../input/input04.txt"


boards = []
for group in groups(INPUT, ints):
    boards.append(group)


seq = boards[0][0]
boards = boards[1:]

def mark(n, board):
    for i in range(5):
        for j in range(5):
            if n == board[i][j]:
                board[i][j] = 0
                return True
    return False

def winner(m):    
    for i in range(5):
        if 0 == sum(m[i]) or 0 == m[0][i]+m[1][i]+m[2][i]+m[3][i]+m[4][i]:
            return True
    return False

def score(board, num):
    u = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != 0:
                u += board[i][j]
    return u*num

def dump(board):
    for i in range(5):
        for j in range(5):    
            print("{0:3}".format(board[i][j]),end="")
        print("")


A = None
B = None
remove = []
exit = False

for num in seq:
    for b in range(len(boards)):
        board = boards[b]
        if mark(num, board):
            if winner(board):
                if not A:
                    A = score(board, num)
                if len(boards) == 1:
                    B = score(board, num)
                    exit = True
                remove.append(board)
    if exit:
        break
    if remove:
        for r in remove:
            boards.remove(r)
        remove = []

if not A or not B:
    print("FAIL")

print("A:", A)
print("B:", B)

#A: 87456
#B: 15561