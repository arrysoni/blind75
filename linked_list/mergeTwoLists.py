"""
Merge Two Sorted Linked Lists
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:
Input: list1 = [], list2 = []
Output: []

Constraints:
0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build(vals):
    """Turn a Python list like [1, 2, 4] into a linked list."""
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def show(head, stop=None):
    """Draw a linked list as '1 -> 2 -> 4'. Stops after `stop` if given."""
    parts = []
    while head:
        parts.append(str(head.val))
        if head is stop:
            break
        head = head.next
    return " -> ".join(parts) if parts else "(empty)"


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        temp = dummy
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp.next = curr1
                curr1 = curr1.next
            else:
                temp.next = curr2
                curr2 = curr2.next
            temp = temp.next

        if curr1:
            temp.next = curr1
        if curr2:
            temp.next = curr2

        return dummy.next

tests = [
    ([1, 2, 4], [1, 3, 5]),
    ([], [1, 2]),
    ([], []),
]

for a, b in tests:
    print("=" * 40)
    print(f"list1: {show(build(a))}")
    print(f"list2: {show(build(b))}")
    result = Solution().mergeTwoLists(build(a), build(b))
    print(f"RESULT: {show(result)}")
        


        