from typing import Optional

from ...utils.treenode import TreeNode


def get_digits(num: int):
    digits = 0
    while num > 0:
        num = num // 10
        digits += 1
    return digits


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(node: TreeNode, curr_number: int):
            nonlocal root_to_leaf
            if node:
                dig = get_digits(node.val)
                curr_number = curr_number * (10**dig) + node.val
                if not (node.left or node.right):
                    root_to_leaf += curr_number
                preorder(node.left, curr_number)
                preorder(node.right, curr_number)

        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(79, right=TreeNode(111))
    root.right = TreeNode(2)
    assert solution.sumNumbers(root) == 379143
