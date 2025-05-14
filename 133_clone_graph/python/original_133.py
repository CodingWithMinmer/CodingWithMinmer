class Node:
    def __init__(self, val: int) -> None:
        self.neighbors = []
        self.val = val


def dfs_133(node: Node, old_to_new: dict[Node, Node]) -> Node:
    if node in old_to_new:
        return old_to_new[node]

    old_to_new[node] = Node(node.val)

    for neighbor in node.neighbors:
        old_to_new[node].neighbors.append(dfs_133(neighbor, old_to_new))

    return old_to_new[node]


# LC: https://leetcode.com/problems/clone-graph/
# SOURCE: https://youtu.be/6u9iRrDJtuI?si=lqSOmit2SThVsI5L
def clone_graph_133(node: Node) -> Node:
    """
    Time Complexity: O(N+E)
    Space Complexity: O(N)
    """
    if not node:
        return None

    old_to_new = {}
    return dfs_133(node, old_to_new)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2]

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

    assert are_graphs_identical(node1, clone_graph_133(node1)) == True
    assert are_graphs_identical(node2, clone_graph_133(node2)) == True
    assert are_graphs_identical(node3, clone_graph_133(node3)) == True
