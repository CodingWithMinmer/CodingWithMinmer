from typing import Dict, Optional

class Node:
    def __init__(self, val: int) -> None:
        self.neighbors = []
        self.val = val


# LC: https://leetcode.com/problems/clone-graph/
# SOURCE: https://youtu.be/6u9iRrDJtuI?si=lqSOmit2SThVsI5L
class Solution_133:
    def dfs(
        self, node: Optional[Node], old_to_new: Dict[Optional[Node], Optional[Node]]
    ) -> Optional[Node]:
        if node in old_to_new:
            return old_to_new[node]

        old_to_new[node] = Node(node.val)

        for neighbor in node.neighbors:
            old_to_new[node].neighbors.append(self.dfs(neighbor, old_to_new))

        return old_to_new[node]

    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
        """
        Time Complexity: O(N+E)
        Space Complexity: O(N)
        """
        if not node:
            return None

        old_to_new = {}
        return self.dfs(node, old_to_new)


if __name__ == "__main__":
    def are_graphs_identical(node1: Node, node2: Node) -> bool:
        def dfs(n1, n2, visited):
            if n1 in visited:
                return visited[n1] == n2
            if n1.val != n2.val or len(n1.neighbors) != len(n2.neighbors):
                return False

            visited[n1] = n2

            # Match neighbors by value and structure
            for neighbor1, neighbor2 in zip(n1.neighbors, n2.neighbors):
                if not dfs(neighbor1, neighbor2, visited):
                    return False

            return True

        return dfs(node1, node2, {})

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2]

    assert are_graphs_identical(node1, Solution_133().clone_graph(node1)) == True
    assert are_graphs_identical(node2, Solution_133().clone_graph(node2)) == True
    assert are_graphs_identical(node3, Solution_133().clone_graph(node3)) == True

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    assert are_graphs_identical(node1, Solution_133().clone_graph(node1)) == True
    assert are_graphs_identical(node2, Solution_133().clone_graph(node2)) == True
    assert are_graphs_identical(node3, Solution_133().clone_graph(node3)) == True
    assert are_graphs_identical(node4, Solution_133().clone_graph(node4)) == True
