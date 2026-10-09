"""
Construct Binary Tree from Preorder and Inorder Traversal
Medium

You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:
Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
Output: [1,2,3,null,null,null,4]

Example 2:
Input: preorder = [1], inorder = [1]
Output: [1]

Constraints:
1 <= inorder.length <= 2001.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000
"""

import sys
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        index = {val: i for i, val in enumerate(inorder)}   # value -> inorder position
        self.pre = 0                                         # next root in preorder

        def build(left, right):          # build the subtree from inorder[left..right]
            if left > right:
                return None

            root_val = preorder[self.pre]
            self.pre += 1
            root = TreeNode(root_val)

            mid = index[root_val]
            root.left = build(left, mid - 1)    # must build left before right
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)


# ---------- Helpers for local testing ----------

def build_tree(values):
    """Level-order list -> tree. None marks a missing child."""
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


def tree_to_list(root):
    """Tree -> level-order list, trailing Nones trimmed."""
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def preorder_of(root):
    return [root.val] + preorder_of(root.left) + preorder_of(root.right) if root else []


def inorder_of(root):
    return inorder_of(root.left) + [root.val] + inorder_of(root.right) if root else []


if __name__ == "__main__":
    sys.setrecursionlimit(10000)   # skewed trees recurse ~n deep
    s = Solution()

    tests = [
        # (preorder, inorder, expected level-order)
        ([1, 2, 3, 4], [2, 1, 3, 4], [1, 2, 3, None, None, None, 4]),    # Example 1
        ([1], [1], [1]),                                                 # Example 2
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([3, 2, 1], [1, 2, 3], [3, 2, None, 1]),                         # left-skewed
        ([1, 2, 3], [1, 2, 3], [1, None, 2, None, 3]),                   # right-skewed
        ([0, -1, 1], [-1, 0, 1], [0, -1, 1]),                            # negatives
    ]
    for pre, ino, expected in tests:
        result = tree_to_list(s.buildTree(pre, ino))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: pre={pre}, in={ino} -> {result} (expected {expected})")

    # Big skewed tree, like the one that timed out on LeetCode
    n = 2000
    pre = list(range(n, 0, -1))
    ino = list(range(1, n + 1))
    root = s.buildTree(pre, ino)
    ok = preorder_of(root) == pre and inorder_of(root) == ino
    print(f"{'PASS' if ok else 'FAIL'}: skewed tree with {n} nodes")