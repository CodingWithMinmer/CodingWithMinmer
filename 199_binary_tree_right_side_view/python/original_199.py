from collections import deque
from typing import Optional

from ...utils.treenode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        rightside = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                curr = queue.popleft()
                if i == level_length - 1:
                    rightside.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return rightside
