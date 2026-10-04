"""
Container With Most Water
Medium

You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36
Explanation: The bars at indices 1 and 7 have heights 7 and 6. The container has width 7 - 1 = 6 and height min(7, 6) = 6, so it can store 6 * 6 = 36 units of water. This is the maximum possible area.

Example 2:
Input: height = [2,2,2]
Output: 4

Constraints:
2 <= height.length <= 100,000
0 <= height[i] <= 10,000
"""


class Solution:
    def maxArea(self, heights):

        left = 0
        right = len(heights) - 1
        best = 0

        while left < right:
            width = right - left
            h = min(heights[left], heights[right])
            best = max(best, width * h)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return best


height1 = [1, 7, 2, 5, 4, 7, 3, 6]
print(Solution().maxArea(height1))

height2 = [2, 2, 2]
print(Solution().maxArea(height2))
