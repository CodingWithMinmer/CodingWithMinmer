from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# VARIANT: What if you were given all the nodes as a part of a list/vector, 
#          and no longer the root node?
# Source: https://youtu.be/iaOceNnKIQQ?si=gHn2QoQ4nRBB2JXU&t=713
def least_common_ancestor(nodes: List[TreeNode], p: TreeNode | None, q: TreeNode | None) -> TreeNode:
    """
    Time Complexity: O(N), where 'N' is the number of nodes in the binary tree
    Space Complexity: O(N)
    """

    child_to_parent = {}
    for node in nodes:
        if node.left:
            child_to_parent[node.left] = node
        if node.right:
            child_to_parent[node.right] = node

    node_one = p
    node_two = q

    while node_one != node_two:
        node_one = child_to_parent[node_one] if node_one in child_to_parent else q
        node_two = child_to_parent[node_two] if node_two in child_to_parent else p

    return node_one

if __name__ == "__main__":
    """
                1
               / \
              2   3
             / \
            4   5
                 \
                  6
                   \
                    7
                
    """
    # Create all nodes
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)


    # Set relationships (left, right)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node5.right = node6
    node6.right = node7

    nodes = [node1, node2, node4, node5, node6, node7, node3]
    assert least_common_ancestor(nodes, node4, node7) == node2
    assert least_common_ancestor(nodes, node3, node3) == node3
    assert least_common_ancestor(nodes, node5, node6) == node5
    assert least_common_ancestor(nodes, node5, node7) == node5
    assert least_common_ancestor(nodes, node1, node2) == node1