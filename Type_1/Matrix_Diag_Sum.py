def diagonalSum(mat):
   res ,n=0,len(mat)
   for i in range(n):
       res += mat1[i][i]
       res+= mat1[i][n-1-i]
   return  res - (mat[n//2][n//2] if n%2 else 0)

mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonalSum(mat1))  # Output: 25
