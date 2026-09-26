"""
Reverse Linked List
Easy

Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:
Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:
Input: head = []
Output: []

Constraints:
0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# build 0 -> 1 -> 2 -> 3
head = None
for v in reversed([0, 1, 2, 3]):
    head = ListNode(v, head)

new_head = Solution().reverseList(head)

# walk the list and collect values
vals = []
while new_head:
    vals.append(new_head.val)
    new_head = new_head.next

print(vals)  # [3, 2, 1, 0]
