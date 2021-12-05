import numpy as np

MAX_SIZE = 1000
matrix = np.zeros((MAX_SIZE, MAX_SIZE))

while inp := input():
    # I'm considering conventional x,y numpy style, tranposing doesn't change the sum
    x1, y1, x2, y2 = [int(num) for p in inp.split("->") for num in p.split(",")]
    left_x, left_y, right_x, right_y = (x1, y1, x2, y2) if y1 <= y2 else (x2, y2, x1, y1)

    if left_x == right_x:  # -
        matrix[left_x, left_y:(right_y+1)] += 1
    elif left_y == right_y:  # |
        matrix[min(x1, x2):(max(x1, x2)+1), left_y] += 1
    else:
        continue

print((matrix >= 2).sum())
