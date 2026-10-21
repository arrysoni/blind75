"""
Set Matrix Zeroes
Medium

Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Example 1:
Input: matrix = [
  [0,1],
  [1,0]
]
Output: [
  [0,0],
  [0,0]
]

Example 2:
Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= (2^31) - 1
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row/col as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out inner cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row and column last
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

        return matrix

matrix1 = [
  [0,1],
  [1,0]
]
print(Solution().setZeroes(matrix1))

matrix2 = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
print(Solution().setZeroes(matrix2))