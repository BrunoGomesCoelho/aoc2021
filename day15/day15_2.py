from heapq import heappush, heappop
import numpy as np

#  submatrix = np.genfromtxt("input.txt", delimiter=1)
submatrix = np.genfromtxt("big_input.txt", delimiter=1)
n = len(submatrix)

# create 5x5 matrix from submatrix
matrix = np.zeros((n*5, n*5))
matrix[:n, :n] = submatrix
for i in range(4):
    matrix[:n, (i+1)*n:(i+2)*n] = (matrix[:n, i*n:(i+1)*n] % 9) + 1
for i in range(4):
    matrix[(i+1)*n:(i+2)*n, :] = (matrix[i*n:(i+1)*n, :] % 9) + 1

n = len(matrix)
start, end = [0, 0], [n-1, n-1]

visited = np.full((n, n), False)
visited[0, 0] = True

answer = None
possible_paths = []  # list of (cost, last_visit), we don't need to keep full path
heappush(possible_paths, (0, start))

while possible_paths:
    cost, (x, y) = heappop(possible_paths)
    if [x, y] == end:
        answer = cost
        break

    for i, j in [(x-1, y), (x,y-1), (x, y+1), (x+1, y)]:
        if not (0 <= i < n) or not(0 <= j < n) or visited[i, j]:
            continue
        visited[i, j] = True
        heappush(possible_paths, (cost+matrix[i, j], [i, j]))

print(answer)
