from typing import Optional
from ....utils.treenode import TreeNode

class SolutionVariantFollowup:
    def topView(self, root):
        if root is None:
            return []

        map = {}
        min_col, max_col = 0, 0
        def dfs(node, column, row):
            nonlocal min_col, max_col
            if not node:
                return

            min_col = min(min_col, column)
            max_col = max(max_col, column)
                
            if column not in map or row < map[column][1]:
                map[column] = (node, row)

            dfs(node.left, column - 1, row + 1)
            dfs(node.right, column + 1, row + 1)

        dfs(root, 0, 0)
        result = []
        for column in range(min_col, max_col + 1):
            result.append(map[column][0].val)
        return result