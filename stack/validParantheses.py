"""
Valid Parentheses
Easy

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:
1 <= s.length <= 1000
"""


class Solution:
    def isValid(self, s):

        stack = []
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if (char in brackets):
                stack.append(brackets[char])
            elif (not stack or stack.pop() != char):
                return False

        return not stack


s1 = "[]"
print(Solution().isValid(s1))

s2 = "([{}])"
print(Solution().isValid(s2))

s3 = "[(])"
print(Solution().isValid(s3))
