"""
Pacific Atlantic Water Flow
Medium

You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

Example 1:
Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

Example 2:
Input: heights = [[1],[1]]
Output: [[0,0],[1,0]]

Constraints:
1 <= heights.length, heights[r].length <= 100
0 <= heights[r][c] <= 1000
"""
from typing import List
class Solution:
    def pacificAtlantic(self, heights):

        ROWS,COLS = len(heights), len(heights[0])
        pac,atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            
            # Make sure r, c is not out of bound
            # Our logic would be opposite of what is given in the question:
            # Border -> Inward, value of the cell should grow, then only water can seep from in-->out
            if ((r,c) in visit
            or r < 0 or c < 0
            or r == ROWS or c == COLS
            or heights[r][c] < prevHeight):
                return

            visit.add((r,c))

            # Check in all 4 directions
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        # Col positions that are touching Pacific/Atlantic
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        # Row positions that are touching Pacific/Atlantic
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])

        res = []
        # Positions that are touching Pacific && Atlantic
        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) in pac and (r,c) in atl):
                    res.append([r,c])

        return res

if __name__ == "__main__":
    sol = Solution()

    heights1 = [
        [4, 2, 7, 3, 4],
        [7, 4, 6, 4, 7],
        [6, 3, 5, 3, 6],
    ]
    print(sorted(sol.pacificAtlantic(heights1)))
    # Expected: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

    heights2 = [[1], [1]]
    print(sorted(sol.pacificAtlantic(heights2)))
    # Expected: [[0,0],[1,0]]


        