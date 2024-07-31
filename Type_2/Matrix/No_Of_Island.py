
# 18. -1 represents ocean and 1 represents land find the number of islands in the given matrix.
#
# Input:   n*n matrix
#        1 -1 -1  1
#       -1  1 -1  1
#       -1 -1  1 -1
#       -1 -1 -1  1
# Output: 2 (two islands that I have
# bold in matrix at 1, 1 and 2, 2)
#

def no_of_islands(matrix):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[x][y] != 1:
            return
        matrix[x][y] = -1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

    islands = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                islands += 1
                dfs(i, j)

    return islands
matrix = [
    [1, -1, -1, 1],
    [-1, 1, -1, 1],
    [-1, -1, 1, -1],
    [-1, -1, -1, 1]
]

ans = no_of_islands(matrix)
print(f"The total number of islands: {ans}")
