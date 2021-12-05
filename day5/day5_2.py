import numpy as np

MAX_SIZE = 1000
matrix = np.zeros((MAX_SIZE, MAX_SIZE))
biggest = float("-inf")

diagonals = []
while inp := input():
    x1, y1, x2, y2 = [int(num) for p in inp.split("->") for num in p.split(",") ]
    biggest = max([x1, y1, x2, y2, biggest])

    # I'm considering conventional x,y numpy style and transposing later
    if x1 == x2 and y1 < y2:
            matrix[x1, y1:(y2+1)] += 1
    elif x1 == x2:
        matrix[x1, y2:(y1+1)] += 1
    elif y1 == y2 and x1 < x2:
        matrix[x1:(x2+1), y1] += 1
    elif y1 == y2:
        matrix[x2:(x1+1), y1] += 1
    else:
        # process after transpose since easier to debug
        diagonals.append([x1, y1, x2, y2] )

matrix = matrix[:(biggest+1), :(biggest+1)].T  # transpose since x,y read inverted

for y1, x1, y2, x2 in diagonals:
    diag = np.arange(abs(x1-x2)+1)

    if (x1 > x2 and y1 > y2):  # \
        matrix[x2+diag, y2+diag] += 1
    elif (x1 < x2 and y1 < y2):  # \
        matrix[x1+diag, y1+diag] += 1
    elif (x1 > x2 and y1 < y2):  # /
        matrix[x2+diag, y2-diag] += 1
    elif (x1 < x2 and y1 > y2):  # /
        matrix[x1+diag, y1-diag] += 1

#  print(matrix)
print((matrix >= 2).sum())
