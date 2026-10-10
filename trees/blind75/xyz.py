# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float('-inf')

        def gain(node):
            nonlocal best
            if not node:
                return 0
            # Drop negative branches — taking nothing is better
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)

            # Path that peaks at this node (can use both sides)
            best = max(best, node.val + left + right)

            # Only one side can be extended upward to the parent
            return node.val + max(left, right)

        gain(root)
        return best