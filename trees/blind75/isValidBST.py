"""
Valid Binary Search Tree
Medium

Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [1,2,3]
Output: false
Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.

Constraints:
1 <= The number of nodes in the tree <= 10000.
-1000000000 <= Node.val <= 1000000000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        
        def dfs(node, low, high):

            if not node:
                return True
            
            if not (low < node.val < high):
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))


def build_tree(values):
    """Build a tree from a LeetCode-style list, e.g. [5,4,6,None,None,3,7]."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
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
    s = Solution()
    tests = [
        ([2, 1, 3], True),
        ([1, 2, 3], False),
        ([5, 4, 6, None, None, 3, 7], False),   # the tricky one
        ([2, 2, 2], False),                      # duplicates
        ([1], True),
    ]
    for values, expected in tests:
        result = s.isValidBST(build_tree(values))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {values} -> {result} (expected {expected})")