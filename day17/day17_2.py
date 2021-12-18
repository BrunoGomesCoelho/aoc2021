import numpy as np
import re

x1, x2, y1, y2 = map(int, re.findall(r"\-?\d+", input()))

start_y = x2+y1  # after x2 steps, you're exactly at y1
answers = set()  # set is overkill since we always add unique answers

while start_y > y1-1:
    for start_x in range(1, x2+1):
        pos_y  = np.cumsum(range(start_y, y1-1, -1))

        pos_x = list(range(start_x, 0, -1))
        pos_x = np.cumsum(pos_x[:len(pos_y)] + [0]*(len(pos_y)-len(pos_x)))

        assert len(pos_x) == len(pos_y)

        valid  = (x1 <= pos_x) & (pos_x <= x2) &  (y1 <= pos_y) & (pos_y <= y2)
        if valid.any():
            answers.add((start_x, start_y))

    start_y -= 1

print(len(answers))
