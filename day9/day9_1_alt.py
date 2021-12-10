def is_lowest_point(matrix, i, j):
    center = matrix[i][j]
    bounds = ((i-1,j), (i+1, j), (i, j-1), (i, j+1))

    for x, y in bounds:
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[x]):
            valid = valid and (center < matrix[x][y])

    return valid


matrix = []
while line := input():
    matrix.append([int(num) for num in line])

ans = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if is_lowest_point(matrix, i, j):
            ans += 1 + matrix[i][j]

print(ans)
