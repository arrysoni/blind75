"""
Palindromic Substrings
Medium

Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.

Example 1:
Input: s = "abc"
Output: 3
Explanation: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i+1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            res += 1
            l -= 1
            r += 1
        return res

s1 = "abc"
print(Solution().countSubstrings(s1))

s2 = "aaa"
print(Solution().countSubstrings(s2))

s3 = "racecar"
print(Solution().countSubstrings(s3))