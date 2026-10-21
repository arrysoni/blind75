"""
Spiral Matrix
Medium

Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

Example 1:
Input: matrix = [[1,2],[3,4]]
Output: [1,2,4,3]

Example 2:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 3:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
1 <= matrix.length, matrix[i].length <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix):

        res = []
        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # Traverse Top Row (Left -> Right)
            for j in range(left, right+1):
                res.append(matrix[top][j])
            top += 1

            # Traverse Right Col (Top -> Bottom)
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            # Traverse Bottom Row (Right -> Left) : only if row remains
            if top <= bottom:
                for j in range(right, left-1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # Traverse Left Col (Bottom -> Top) : only if col remains
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


matrix1 = [[1, 2], [3, 4]]
print(Solution().spiralOrder(matrix1))

matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().spiralOrder(matrix2))

matrix3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(Solution().spiralOrder(matrix3))
