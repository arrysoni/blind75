"""
Course Schedule
Medium

You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.

Example 1:
Input: numCourses = 2, prerequisites = [[0,1]]
Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:
Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
Output: false
Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.

Constraints:
1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
prerequisites[i].length == 2
0 <= a[i], b[i] < numCourses
All prerequisite pairs are unique.
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses along the curr DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))                  # expected True
    print(sol.canFinish(2, [[1, 0], [0, 1]]))          # expected False (cycle)
    print(sol.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))  # expected True