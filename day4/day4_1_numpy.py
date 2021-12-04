import numpy as np
from sys import stdin


def read_board():
    board = np.zeros((5, 5))
    is_marked = np.full((5, 5), False)
    for i in range(5):
        for j, num in enumerate(input().split()):
            board[i, j] = int(num)

    return (board, is_marked)

drawn_numbers = [int(num) for num in input().split(',')]

for line in stdin: # ignore newlines
    boards.append(read_board())


for number in drawn_numbers:
    for (board, is_marked) in boards:
        is_marked[board == number] = True
        if any(is_marked.sum(axis=0) == 5) or any(is_marked.sum(axis=1) == 5):
            score = int(board[~is_marked].sum()*number)
            print(score)
            exit(0)
