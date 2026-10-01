"""
Valid Anagram
Easy

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.


Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Example 3:
Input: s = "x", t = "x"
Output: true

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            count[char] = count.get(char, 0) - 1

        for value in count.values():
            if value != 0:
                return False

        return True


s1 = "racecar"
t1 = "carrace"
print(Solution().isAnagram(s1, t1))

s2 = "jar"
t2 = "jam"
print(Solution().isAnagram(s2, t2))

s3 = "x"
t3 = "x"
print(Solution().isAnagram(s3, t3))
