from typing import Optional

from ...utils.treenode import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(node: TreeNode, curr_number: int):
            nonlocal root_to_leaf
            if node:
                curr_number = curr_number * 10 + node.val
                if not (node.left or node.right):
                    root_to_leaf += curr_number

                preorder(node.left, curr_number)
                preorder(node.right, curr_number)

        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
