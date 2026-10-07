"""
Same Binary Tree
Easy

Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [4,7], q = [4,null,7]
Output: false

Example 3:
Input: p = [1,2,3], q = [1,3,2]
Output: false

Constraints:
0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    """Build a binary tree from a LeetCode-style level-order list."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        # left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        # right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    s = Solution()

    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    print(s.isSameTree(p1, q1))  # True

    p2 = build_tree([4, 7])
    q2 = build_tree([4, None, 7])
    print(s.isSameTree(p2, q2))  # False

    p3 = build_tree([1, 2, 3])
    q3 = build_tree([1, 3, 2])
    print(s.isSameTree(p3, q3))  # False

