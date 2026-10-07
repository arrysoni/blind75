"""
Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: 3

Example 2:
Input: root = []
Output: 0

Constraints:
0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def build_tree(values):
    """Build a binary tree from a LeetCode-style level-order list (None = missing node)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 2, 3, None, None, 4], 3),
        ([], 0),
        ([1], 1),
        ([1, 2, None, 3, None, 4], 4),        # left-skewed
        ([3, 9, 20, None, None, 15, 7], 3),
    ]

    for values, expected in tests:
        result = sol.maxDepth(build_tree(values))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}  input={values}  output={result}  expected={expected}")