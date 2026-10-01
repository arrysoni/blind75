"""
Contains Duplicate
Easy

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

"""

class Solution:
    def hasDuplicate(self, nums):

        nums_set = set(nums)

        if (len(nums_set) == len(nums)):
            return False
        return True


nums1 = [1, 2, 3, 3]
print(Solution().hasDuplicate(nums1))

nums2 = [1, 2, 3, 4]
print(Solution().hasDuplicate(nums2))

