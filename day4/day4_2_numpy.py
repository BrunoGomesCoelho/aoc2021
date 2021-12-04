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

boards = [] # [(b1, marked1), ...]
for line in stdin: # ignore newlines
    boards.append(read_board())


finished_games = np.full(len(boards), False)

for number in drawn_numbers:
    for i, (board, is_marked) in enumerate(boards):
        is_marked[board == number] = True
        is_bingo = any(is_marked.sum(axis=0) == 5) or any(is_marked.sum(axis=1) == 5)

        if is_bingo and finished_games[i] == False:
            finished_games[i] = True

        if finished_games.sum() == len(finished_games):
            score = int(board[~is_marked].sum()*number)
            print(score)
            exit(0)
