from std import *
import sys

INPUT = "../input/input04.txt"
#INPUT = "../input/test.txt"


boards = []
for group in groups(INPUT, ints):
    boards.append({
            "marked": [0]*25,
            "num": group
        })


seq = boards[0]['num'][0]
boards = boards[1:]

def mark(n, board):
    # mark board
    data = board['num']
    for i in range(5):
        for j in range(5):
            if n == data[i][j]:
                board['marked'][i*5+j] = 1
                return True
    return False

def winner(board):
    m = board['marked']
    for i in range(5):
        if 5 == sum(m[i*5:i*5+5]):
            return True            
        if 5 == m[i]+m[i+5]+m[i+10]+m[i+15]+m[i+20]:
            return True
    return False

def score(board, num):
    marked = board['marked']
    data = board['num']
    u = 0
    for i in range(5):
        for j in range(5):
            if marked[i*5+j] == 0:
                u += data[i][j]
    return u*num

def dump(board):
    marked = board['marked']
    data = board['num']
    for i in range(5):
        for j in range(5):    
            print("{0:3}.{1}".format(data[i][j], marked[i*5+j]),end="")
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
