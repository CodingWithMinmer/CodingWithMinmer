class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

# LC: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
# SOURCE: https://youtu.be/iaOceNnKIQQ?si=7DxL8DYk6jPmiVa3
def least_common_ancestor(p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Time Complexity: O(h), where 'h' is the height of the binary tree, which in
                     the worst case is equal to the number of nodes in a
                     skewed tree
    Space Complexity: O(1)
    """

    node_one = p
    node_two = q

    while node_one != node_two:
        node_one = node_one.parent if node_one.parent else q
        node_two = node_two.parent if node_two.parent else p

    return node_one

if __name__ == "__main__":
    """
                0
               /
              1
             / \
            2   3
           /     \
          4       5
           \
            6
                
    """
    # Create all nodes
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    # Set relationships (left, right, parent)
    node0.left = node1
    node1.parent = node0

    node1.left = node2
    node2.parent = node1

    node1.right = node3
    node3.parent = node1

    node2.left = node4
    node4.parent = node2

    node3.right = node5
    node5.parent = node3

    node4.right = node6
    node6.parent = node4

    assert least_common_ancestor(node0, node1) == node0
    assert least_common_ancestor(node4, node5) == node1
    assert least_common_ancestor(node5, node6) == node1