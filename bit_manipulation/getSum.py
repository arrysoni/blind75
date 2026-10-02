"""
Sum of Two Integers
Medium

Given two integers a and b, return the sum of the two integers without using the + and - operators.

Example 1:
Input: a = 1, b = 1
Output: 2

Example 2:
Input: a = 4, b = 7
Output: 11

Constraints:
-1000 <= a, b <= 1000
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF        # keep only the lowest 32 bits
        MAX_INT = 0x7FFFFFFF     # largest positive 32-bit int

        while b != 0:
            carry = ((a & b) << 1) & MASK   # where both bits are 1, carry left
            a = (a ^ b) & MASK              # sum ignoring carries
            b = carry

        # bit 31 set means the 32-bit result is negative; convert back
        return a if a <= MAX_INT else ~(a ^ MASK)


print(Solution().getSum(1, 1))     # 2
print(Solution().getSum(4, 7))     # 11
print(Solution().getSum(-1, 1))    # 0
print(Solution().getSum(-5, -3))   # -8

