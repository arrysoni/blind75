"""
Rotate Image
Medium

Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [
  [1,2],
  [3,4]
]
Output: [
  [3,1],
  [4,2]
]

Example 2:
Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

class Solution:
    def rotate(self, matrix):

        n = len(matrix)

        # Transpose
        for i in range(0, n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for row in matrix:
            row.reverse()

        return matrix

matrix1 = [
    [1,2], 
    [3,4]
]
print(Solution().rotate(matrix1))

matrix2 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(Solution().rotate(matrix2))
        