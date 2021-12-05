import numpy as np
from sys import stdin


N = 5
boards = []  # [(board_i, marked_i), ...]
drawn_numbers = [int(num) for num in input().split(',')]

for line in stdin:  # skip newlines
    is_marked = np.full((N, N), False)
    board = np.array([[int(x) for x in input().split()] for _ in range(N)])

    boards.append((board, is_marked))

for num in drawn_numbers:
    for (board, is_marked) in boards:
        is_marked[board == num] = True

        if any(is_marked.sum(axis=0) == N) or any(is_marked.sum(axis=1) == N):
            score = int(board[~is_marked].sum()*num)
            print(score)
            exit(0)
