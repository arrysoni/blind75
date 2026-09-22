"""
Longest Substring Without Repeating Characters
Medium
Topics
Company Tags
Hints
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.


Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.


Example 2:

Input: s = "xxxx"

Output: 1

Constraints:

0 <= s.length <= 50,000
s may consist of printable ASCII characters.

"""

class Solution:
    def lengthOfLongestSubstring(self, s):

        left = 0
        charSet = set()
        res = 0

        for right in range(len(s)):

            while (s[right] in charSet):
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            res = max(res, right - left + 1)

        return res

s1 = "zxyzxyz"
print(Solution().lengthOfLongestSubstring(s1))

s2 = "xxx"
print(Solution().lengthOfLongestSubstring(s2))