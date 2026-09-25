"""
Find Minimum in Rotated Sorted Array
Medium

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:
Input: nums = [3,4,5,6,1,2]
Output: 1

Example 2:
Input: nums = [4,5,0,1,2,3]
Output: 0

Example 3:
Input: nums = [4,5,6,7]
Output: 4

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

"""

class Solution:
    def findMin(self, nums):

        min_Num = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:

            # Case 1: The array ended up rotating to itself
            if (nums[left] < nums[right]):
                min_Num = min(min_Num, nums[left])
                break

            # Case 2: The array just rotated randomly
            mid = (left + right) // 2
            min_Num = min(min_Num, nums[mid])

            # The mid number is part of the left sorted array, which means that the min. number lies on the right sorted array
            if (nums[left] <= nums[mid]):
                left = mid + 1
            # The mid number is part of the right sorted array, which means that the min. number lies on the left sorted array, or can actually be the min element; reduce range of right
            else:
                right = mid - 1

        return min_Num


nums1 = [3, 4, 5, 6, 1, 2]
print(Solution().findMin(nums1))

nums2 = [4, 5, 0, 1, 2, 3]
print(Solution().findMin(nums2))

nums3 = [4, 5, 6, 7]
print(Solution().findMin(nums3))
