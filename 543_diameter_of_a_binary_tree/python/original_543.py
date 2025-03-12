from ...utils.treenode import TreeNode

def getDiameter(root: TreeNode | None):
    diameter = 0
    def longestPath(root: TreeNode | None):
        nonlocal diameter
        if not root:
            return 0
        right = longestPath(root.right)
        left = longestPath(root.left)
        diameter = max(diameter, left + right)
        return max(left, right) + 1
    longestPath(root)
    return diameter