"""
Remove Nth Node From End of List
Medium

Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4], n = 2
Output: [1,2,4]

Example 2:
Input: head = [5], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 2
Output: [2]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Put fast n nodes ahead of slow
        for _ in range(n):
            fast = fast.next

        # Advance both until fast is on the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # slow.next is the nth node from the end
        slow.next = slow.next.next
        return dummy.next


# ---------- Helpers ----------
def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---------- Tests ----------
if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], 2, [1, 2, 4]),   # Example 1
        ([5], 1, []),                   # Example 2
        ([1, 2], 2, [2]),               # Example 3
        ([1, 2], 1, [1]),               # remove tail
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),  # remove head of longer list
    ]

    sol = Solution()
    for values, n, expected in tests:
        head = build_list(values)
        output = to_list(sol.removeNthFromEnd(head, n))
        status = "PASS" if output == expected else "FAIL"
        print(f"{status}: head={values}, n={n} -> {output} (expected {expected})")