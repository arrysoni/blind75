"""
Number of 1 Bits
Easy

You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:
Input: n = 23
Output: 4
Explanation: The binary representation of 23 is 10111, which contains four 1 bits.

Example 2:
Input: n = 2147483645
Output: 30
Explanation: The binary representation of 2147483645 is 1111111111111111111111111111101, which contains thirty 1 bits.

Constraints:
0 <= n <= 2^31 - 1.

"""


class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        while n:
            count += n & 1
            n >>= 1

        return count


n1 = 23
print(Solution().hammingWeight(n1))

n2 = 2147483645
print(Solution().hammingWeight(n2))
