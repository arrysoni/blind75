"""
Palindrome Linked List
Easy

You are given the head of a singly linked list, return true if it is a palindrome or false otherwise.

A palindrome is a sequence that reads the same forward and backward.

Example 1:
Input: head = [1,2,3,2,1]
Output: true

Example 2:
Input: head = [2,2]
Output: true

Example 3:
Input: head = [2,1]
Output: false

Constraints:
1 <= Length of the list <= 100,000.
0 <= Node.val <= 9
Follow up: Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        if not head:
            return True

        # Find the middle using slow & fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare left and right sides
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


def build(vals):
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


head1 = build([1, 2, 3, 2, 1])
print(Solution().isPalindrome(head1))   # True

head2 = build([2, 2])
print(Solution().isPalindrome(head2))   # True

head3 = build([2, 1])
print(Solution().isPalindrome(head3))   # False
