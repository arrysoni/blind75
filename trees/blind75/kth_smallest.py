"""
Kth Smallest Integer in BST
Medium

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3], k = 1
Output: 1

Example 2:
Input: root = [4,3,5,2,null], k = 4
Output: 5

Constraints:
1 <= k <= The number of nodes in the tree <= 10,000.
0 <= Node.val <= 10,000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):

        values = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            # visit node here: values arrive smallest to largest
            values.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return values[k-1]

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
        # (tree, k, expected)
        ([2, 1, 3], 1, 1),                              # Example 1
        ([4, 3, 5, 2, None], 4, 5),                     # Example 2
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),         # middle of the tree
        ([5, 3, 6, 2, 4, None, None, 1], 1, 1),         # smallest (deepest left)
        ([5, 3, 6, 2, 4, None, None, 1], 6, 6),         # largest (k = n)
        ([1], 1, 1),                                    # single node
        ([3, 2, None, 1], 2, 2),                        # left-skewed
        ([1, None, 2, None, 3], 3, 3),                  # right-skewed
    ]
    for values, k, expected in tests:
        result = s.kthSmallest(build_tree(values), k)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {values}, k={k} -> {result} (expected {expected})")