"""
Reverse Bits
Easy

Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Example 1:
Input: n = 00000000000000000000000000010101
Output:    2818572288 (10101000000000000000000000000000)
Explanation: Reversing 00000000000000000000000000010101, which represents the unsigned integer 21, gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.

"""


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)  # make room, drop in n's last bit
            n >>= 1                            # move to n's next bit
        return result


n1 = 0b00000000000000000000000000010101   # binary literal = 21
print(Solution().reverseBits(n1))

n2 = 0b100111
print(Solution().reverseBits(n2))
