"""
Final Array State After K Multiplication Operations I
Easy

You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.

Example 1:
Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
Output: [8,4,6,5,6]
Explanation : [2, 2, 3, 5, 6] -> [4, 2, 3, 5, 6] -> [4, 4, 3, 5, 6] -> [4, 4, 6, 5, 6] -> [8, 4, 6, 5, 6]

Example 2:
Input: nums = [1,2], k = 3, multiplier = 4
Output: [16,8]
Explanation: [4, 2] -> [4, 8] -> [16, 8]

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 10
1 <= multiplier <= 5
"""

import heapq
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            val, idx = heapq.heappop(heap)
            val *= multiplier
            nums[idx] = val
            heapq.heappush(heap, (val, idx))

        return nums

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.getFinalState([2, 1, 3, 5, 6], 5, 2))   # expected [8, 4, 6, 5, 6]

    # Example 2
    print(sol.getFinalState([1, 2], 3, 4))            # expected [16, 8]