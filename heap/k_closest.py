"""
K Closest Points to Origin
Medium

You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order. The answer is guaranteed to be unique(except for the order in which the points are returned.)

Example 1:
Input: points = [[0,2],[2,2]], k = 1
Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

Example 2:
Input: points = [[0,2],[2,0],[2,2]], k = 2
Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.

Constraints:
1 <= k <= points.length <= 1000
-100 <= points[i][0], points[i][1] <= 100
"""

import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # max-heap via negated distances

        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)  # drops the farthest point

        return [[x, y] for _, x, y in heap]

if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[0, 2], [2, 2]], 1))              # [[0, 2]]
    print(sol.kClosest([[0, 2], [2, 0], [2, 2]], 2))      # [[0, 2], [2, 0]] (any order)