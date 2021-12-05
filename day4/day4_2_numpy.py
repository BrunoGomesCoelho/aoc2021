import numpy as np
from sys import stdin


N = 5
boards = []  # [(board_i, marked_i), ...]
drawn_numbers = [int(num) for num in input().split(',')]

for line in stdin:  # skip newlines
    is_marked = np.full((N, N), False)
    board = np.array([[int(x) for x in input().split()] for _ in range(N)])

    boards.append((board, is_marked))

finished_games = np.full(len(boards), False)

for num in drawn_numbers:
    for board_idx, (board, is_marked) in enumerate(boards):
        is_marked[board == num] = True
        is_bingo = any(is_marked.sum(axis=0) == N) or any(is_marked.sum(axis=1) == N)

        if is_bingo and not finished_games[board_idx]:
            finished_games[board_idx] = True

        if finished_games.sum() == len(finished_games):
            score = int(board[~is_marked].sum()*num)
            print(score)
            exit(0)
