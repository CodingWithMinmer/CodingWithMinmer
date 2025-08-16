from typing import Optional
from ....utils.treenode import TreeNode

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        map = {}
        def dfs(node, level):
            if not node:
                return
            if level not in map:
                map[level] = node

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)

        result = []
        for _, node in map.items():
            result.append(node.val)
        return result