from typing import Optional


class Solution:
    class Node:
        def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
            self.val = int(x)
            self.next = next
            self.random = random

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        visited = {}

        def dfs(head):
            if head is None:
                return None
            if head in visited:
                return visited[head]
            node = Node(head.val)
            visited[head] = node
            node.next = dfs(head.next)
            node.random = dfs(head.random)
            return node

        return dfs(head)
