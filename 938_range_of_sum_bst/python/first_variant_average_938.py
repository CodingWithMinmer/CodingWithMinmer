from typing import Optional

from ...utils.treenode import TreeNode


class Solution:
    def rangeAverageBST(self, root: Optional[TreeNode], low: int, high: int) -> float:
        result = 0
        count = 0
        stack = [root]
        while stack:
            curr = stack.pop()
            if low <= curr.val <= high:
                result += curr.val
                count += 1
            if curr.right and curr.val < high:
                stack.append(curr.right)
            if curr.left and curr.val > low:
                stack.append(curr.left)
        return result / count
