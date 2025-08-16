from typing import Optional
from ....utils.treenode import TreeNode

class SolutionVariant:
    def topView(self, root):
        if root is None:
            return []

        map = {}
        def dfs(node, column, row):
            if not node:
                return
            if column not in map or row < map[column][1]:
                map[column] = (node, row)

            dfs(node.left, column - 1, row + 1)
            dfs(node.right, column + 1, row + 1)

        dfs(root, 0, 0)
        result = []
        for column in sorted(map):
            result.append(map[column][0].val)
        return result 