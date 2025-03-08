from typing import Optional

from ...utils.treenode import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        stack = [root]
        while stack:
            curr = stack.pop()
            if low <= curr.val <= high:
                result += curr.val
            if curr.right and curr.val < high:
                stack.append(curr.right)
            if curr.left and curr.val > low:
                stack.append(curr.left)
        return result
