"""
House Robber II
Medium

You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [3,4,3]
Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 200
"""
class Solution:
    def rob(self,nums):
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self,nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3, 4, 3], 4),
        ([2, 9, 8, 3, 6], 15),
        ([1, 2, 3, 1], 4),
        ([5], 5),        # single house: why nums[0] is in the max()
    ]
    for nums, expected in tests:
        print(f"{nums} → {sol.rob(nums)}, expected: {expected}")
