"""
Counting Bits
Easy

Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 4
Output: [0,1,1,2,1]

Explanation:
0 --> 0 (0)
1 --> 1 (1)
2 --> 10 (1)
3 --> 11 (2)
4 --> 100 (1)

5 --> 101 (2)
6 --> 110 (2)
7 --> 111 (3)
8 --> 1000 (1)

9 --> 1001 (2)
10 --> 1010 (2)
11 --> 1011 (3)
12 --> 1100 (2)

Constraints:
0 <= n <= 1000
"""


class Solution:
    def countBits(self, n):

        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp


n1 = 4
print(Solution().countBits(n1))

n2 = 5
print(Solution().countBits(n2))
