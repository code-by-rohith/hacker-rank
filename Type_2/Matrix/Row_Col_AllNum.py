# 2133. Check if Every Row and Column Contains All Numbers
# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true
# Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
# Hence, we return true.

# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false
# Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
# Hence, we return false.
def is_valid_matrix(matrix):
    n = len(matrix)
    if n == 0:
        return False
    for row in matrix:
        if sorted(row) != list(range(1, n+1)):
            return False

    for col in range(n):
        column = [matrix[row][col] for row in range(n)]
        if sorted(column) != list(range(1, n + 1)):
            return False
    return True


matrix = [
    [1,2, 3],
    [3, 1, 2],
    [2, 3, 1]
]

print(is_valid_matrix(matrix))
