"""
Linked List Cycle Detection
Easy

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:
Input: head = [1,2,3,4], index = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], index = -1
Output: false

Constraints:
0 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


labels = {}  # node -> its index, so prints can say "3 (idx 2)"


def build(vals, index):
    """Build a list from vals; if index != -1, point the tail at nodes[index]."""
    labels.clear()
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i, node in enumerate(nodes):
        labels[node] = i
        if i < len(nodes) - 1:
            node.next = nodes[i + 1]
    if index != -1:
        nodes[-1].next = nodes[index]
    return nodes[0]


def label(node):
    return "None" if node is None else f"{node.val} (idx {labels[node]})"


def show(head):
    """Draw the list without looping forever on a cycle."""
    parts, seen = [], set()
    while head:
        if head in seen:
            parts.append(f"back to idx {labels[head]}")
            break
        seen.add(head)
        parts.append(str(head.val))
        head = head.next
    return " -> ".join(parts) if parts else "(empty)"


class Solution:
    def hasCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if (slow is fast):
                return True

        return False


tests = [
    ([1, 2, 3, 4], 1),
    ([1, 2], -1),
    ([], -1),
]

for vals, index in tests:
    print("=" * 40)
    head = build(vals, index)
    print(f"list: {show(head)}")
    print(f"RESULT: {Solution().hasCycle(head)}")
