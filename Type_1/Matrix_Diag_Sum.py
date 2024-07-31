def diagonalSum(mat):
   res ,n=0,len(mat)
   for i in range(n):
       res += mat[i][i]
       res+= mat[i][n-1-i]
   return  res - (mat[n//2][n//2] if n%2 else 0)

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonalSum(mat))  # Output: 25
