class Node:
    def __init__(self, val: int) -> None:
        self.neighbors = []
        self.val = val


class Graph:
    def __init__(self) -> None:
        self.roots = []


def dfs_133_variant(node: Node, old_to_new: dict[Node, Node]) -> Node:
    if node in old_to_new:
        return old_to_new[node]

    old_to_new[node] = Node(node.val)

    for neighbor in node.neighbors:
        old_to_new[node].neighbors.append(dfs_133_variant(neighbor, old_to_new))

    return old_to_new[node]


# VARIANT: What if you had to define the data structures yourself and clone
#          the disconnected graph?
# SOURCE: https://youtu.be/6u9iRrDJtuI?si=INQeDk8LGUwx2Uwh&t=896
def clone_graph_133_variant(input: Graph) -> Graph:
    """
    Time Complexity: O(N+E)
    Space Complexity: O(N)
    """
    output = Graph()
    for node in input.roots:
        if not node:
            continue

        old_to_new = {}
        output.roots.append(dfs_133_variant(node, old_to_new))

    return output


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2]

    node4 = Node(4)
    node5 = Node(5)
    node4.neighbors = [node5]
    node5.neighbors = [node4]

    graph = Graph()
    graph.roots = [node1, None, node4]

    def are_graphs_identical(graph1: Graph, graph2: Graph) -> bool:
        def dfs(n1, n2, visited):
            if n1 in visited:
                return visited[n1] == n2
            if n1.val != n2.val or len(n1.neighbors) != len(n2.neighbors):
                return False

            visited[n1] = n2

            # Match neighbors in each fragment by value and structure
            for neighbor1, neighbor2 in zip(n1.neighbors, n2.neighbors):
                if not dfs(neighbor1, neighbor2, visited):
                    return False

            return True

        # Match each fragment of the disconnected graph by value and structure
        for root1, root2 in zip(graph1.roots, graph2.roots):
            if not root1:
                continue

            if not dfs(root1, root2, {}):
                return False

        return True

    assert are_graphs_identical(graph, clone_graph_133_variant(graph)) == True
