"""
Maximum Product Subarray
Medium

Given an integer array nums, find a subarray that has the largest product, and return the product.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

Example 1:
Input: nums = [2,4,-3,5]
Output: 8
Explanation: [2,4] has the largest product 8.

Example 2:
Input: nums = [-3,0,-2]
Output: 0
Explanation: The result cannot be 6, because [-3,-2] is not a subarray.

Constraints:
1 <= nums.length <= 20,000
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def maxProduct(self, nums):
        pass


nums1 = [2,4,-3,5]
print(Solution().maxProduct(nums1))
nums2 = [-3,0,-2]
print(Solution().maxProduct(nums2))
nums3 = [0,0,0,0]
        


print(Solution().maxProduct(nums3))