"""
Binary Tree Maximum Path Sum (Hard)

Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
A path does not need to include the root, and a node can't appear in it more than once.

Example 1: root = [1,2,3]                        -> 6   (2 -> 1 -> 3)
Example 2: root = [-15,10,20,null,null,15,5,-5]  -> 40  (15 -> 20 -> 5)

Constraints: 1 <= nodes <= 30000, -1000 <= Node.val <= 1000
"""

import sys
from collections import deque

# A skewed tree of 30,000 nodes would exceed Python's default recursion limit (1000)
sys.setrecursionlimit(100_000)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Excluding -ve nums: drop a child branch if its best path sum is negative
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Compute Path Sum w/ Split
            # This line also decides if a straight path or bent path is better!
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return best straight-down path from this node (no split) for the parent to extend
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]


def build_tree(values):
    """Build a tree from a LeetCode-style level-order list (None = missing node)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    tests = [
        ([1, 2, 3], 6),
        ([-15, 10, 20, None, None, 15, 5, -5], 40),
        ([-3], -3),                      # single negative node
        ([-1, -2, -3], -1),              # all negatives: best is the single largest node
        ([2, -1], 2),                    # negative child gets dropped
    ]

    sol = Solution()
    for values, expected in tests:
        result = sol.maxPathSum(build_tree(values))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}  input={values}  output={result}  expected={expected}")