"""
You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

Leaf nodes have an integer value.
The root has a string value of either "+", "-", "*", or "/".
The yield of the tree is calculated by applying the mathematical operation to the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    +
  /   \
 7     5

apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree))
Example Output:
12
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def calculate_yield(root):
    a = root.left.val
    b = root.right.val
    op = root.val

    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b
    raise ValueError(f"Unknown operator: {op}")


if __name__ == "__main__":
    apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
    print(calculate_yield(apple_tree))  # 12

    print(calculate_yield(TreeNode("-", TreeNode(7), TreeNode(5))))  # 2
    print(calculate_yield(TreeNode("*", TreeNode(7), TreeNode(5))))  # 35
    print(calculate_yield(TreeNode("/", TreeNode(10), TreeNode(4))))  # 2.5
