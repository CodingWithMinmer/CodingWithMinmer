class TreeNode:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        parent = {root: None}
        stack = [root]
        while p not in parent or q not in parent:
            node = stack.pop()
            for child in node.children:
                parent[child] = node
                stack.append(child)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q


if __name__ == "__main__":
    # Tree structure:
    #       1
    #    /  |  \
    #   3   2   4
    #  / \
    # 5   6
    root1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    root1.children = [node3, node2, node4]
    node3.children = [node5, node6]
    solution = Solution()
    assert solution.lowestCommonAncestor(root1, node5, node2) == root1
    assert solution.lowestCommonAncestor(root1, node5, node6) == node3

    # Test Case 2: More complex tree
    # Tree structure:
    #        10
    #     /  |  \  \
    #    5   1   7  8
    #   / \  |      |
    #  2  4  3      9
    #    /
    #   6
    root2 = TreeNode(10)
    node5_2 = TreeNode(5)
    node1 = TreeNode(1)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node2_2 = TreeNode(2)
    node4_2 = TreeNode(4)
    node3_2 = TreeNode(3)
    node9 = TreeNode(9)
    node6_2 = TreeNode(6)

    root2.children = [node5_2, node1, node7, node8]
    node5_2.children = [node2_2, node4_2]
    node1.children = [node3_2]
    node8.children = [node9]
    node4_2.children = [node6_2]
    assert solution.lowestCommonAncestor(root2, node6_2, node3_2) == root2
    assert solution.lowestCommonAncestor(root2, node6_2, node2_2) == node5_2
