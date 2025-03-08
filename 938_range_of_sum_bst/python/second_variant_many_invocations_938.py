from typing import Optional
from itertools import accumulate
from bisect import bisect_left

from ...utils.treenode import TreeNode


class Solution:
    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        self.inorder(root)
        self.prefix_sums = list(accumulate(self.values))

    def inorder(self, root: TreeNode):
        if not root:
            return
        self.inorder(root.left)
        self.values.append(root.val)
        self.inorder(root.right)

    def rangeSumBST(self, low: int, high: int) -> int:
        left = bisect_left(self.values, low)
        right = bisect_left(self.values, high)
        if left == 0:
            return self.prefix_sums[right]
        return self.prefix_sums[right] - self.prefix_sums[left - 1]
