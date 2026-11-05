"""
Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".

Example 1:
Input: nums = [9,1,4,2,3,3,7]
Output: 4
Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

Example 2:
Input: nums = [0,3,1,3,2,3]
Output: 4

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""

class Solution:
    def lengthOfLIS(self, nums):
        lis = [1] * len(nums)

        for i in range(len(nums), -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])

        return max(lis)

nums1 = [0,1,2,3,5,4,6,7]
print(Solution().lengthOfLIS(nums1))

nums2 = [9,1,4,2,3,3,7]
print(Solution().lengthOfLIS(nums2))

nums3 = [0,3,1,3,2,3]
print(Solution().lengthOfLIS(nums3))