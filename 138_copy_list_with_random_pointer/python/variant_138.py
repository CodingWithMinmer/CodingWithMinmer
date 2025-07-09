from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: "Optional[Node]") -> "Optional[NodeCopy]":
        visited = {}

        def dfs(root) -> "Optional[NodeCopy]":
            if root is None:
                return None
            if root in visited:
                return visited[root]
            copy = NodeCopy(root.val)
            visited[root] = copy
            copy.left = dfs(root.left)
            copy.right = dfs(root.right)
            copy.random = dfs(root.random)
            return copy

        return dfs(root)
