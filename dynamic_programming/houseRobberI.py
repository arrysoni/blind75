"""
House Robber
Medium

You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [1,1,3,3]
Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

# Top Down Approach
class SolutionTopDown:
    def rob(self, nums):

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        memo = {0: nums[0], 1: max(nums[0], nums[1])}

        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i]+helper(i-2), helper(i-1))
                return memo[i]

        return helper(n-1)

# Bottom Up Approach
class SolutionBottomUp:
    def rob(self, nums):

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n-1]

if __name__ == "__main__":
    tests = [
        ([1, 1, 3, 3], 4),
        ([2, 9, 8, 3, 6], 16),
        ([5], 5),
        ([2, 7], 7),
    ]
    for nums, expected in tests:
        td = SolutionTopDown().rob(nums)
        bu = SolutionBottomUp().rob(nums)
        print(f"{nums} → top-down: {td}, bottom-up: {bu}, expected: {expected}")





    

        