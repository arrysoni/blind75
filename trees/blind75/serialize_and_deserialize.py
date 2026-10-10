"""
Serialize and Deserialize Binary Tree
Hard

Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in the tree <= 10,000.
-1000 <= Node.val <= 1000
"""

import sys
from collections import deque
 
# A skewed tree of 10,000 nodes would exceed Python's default recursion limit (1000)
sys.setrecursionlimit(100_000)
 
 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
 
class Codec:
 
    # Encodes a tree to a single string.
    def serialize(self, root):
        res = []
 
        def dfs(node):
            if not node:
                res.append('N')
                return
 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
 
        dfs(root)
        return ",".join(res)
 
    # Decodes your encoded data to tree.
    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
 
        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
 
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
 
        return dfs()
 
 
# ---------- Helpers for running locally (LeetCode/NeetCode does this for you) ----------
 
def build_tree(values):
    """Build a tree from a level-order list like [1,2,3,None,None,4,5]."""
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
    """Convert a tree back to a level-order list so it can be printed and compared."""
    if not root:
        return []
 
    res = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
 
    # Trim trailing Nones to match the LeetCode format
    while res and res[-1] is None:
        res.pop()
    return res
 
 
if __name__ == "__main__":
    tests = [
        [1, 2, 3, None, None, 4, 5],
        [],
        [-1000],                          # single node, min value
        [1, None, 2, None, 3],            # right-skewed
        [10, -5, 20, None, 7, 15],        # negatives and multi-digit values
    ]
 
    codec = Codec()
    for values in tests:
        root = build_tree(values)                 # list -> tree
        data = codec.serialize(root)              # tree -> string
        restored = codec.deserialize(data)        # string -> tree
        output = tree_to_list(restored)           # tree -> list (for printing)
 
        status = "PASS" if output == values else "FAIL"
        print(f"{status}  input={values}")
        print(f"      serialized:   '{data}'")
        print(f"      deserialized: {output}\n")
 