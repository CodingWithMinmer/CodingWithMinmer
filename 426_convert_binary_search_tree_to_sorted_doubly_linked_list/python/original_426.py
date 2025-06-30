from typing import List, Optional


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


# LC: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# SOURCE: https://youtu.be/tzp1GYRn19k?si=_ok1KPwllnc3A6zz
class Solution_426:
    def dfs(
        self,
        c: Optional[TreeNode],
        p_ref: List[Optional[TreeNode]],
        head_ref: List[Optional[TreeNode]],
    ):
        if not c:
            return

        self.dfs(c.left, p_ref, head_ref)
        if not p_ref[0]:
            head_ref[0] = c
        else:
            p_ref[0].right = c
            c.left = p_ref[0]
        p_ref[0] = c
        self.dfs(c.right, p_ref, head_ref)

    def tree_to_doubly_list(self, root: Optional[TreeNode]):
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if not root:
            return None

        p_ref = [None]
        head_ref = [None]
        self.dfs(root, p_ref, head_ref)

        head = head_ref[0]
        tail = p_ref[0]
        head.left = tail
        tail.right = head

        return head


if __name__ == "__main__":

    r"""
                4
               / \
              2   5
             / \
            1   3
    """
    root = TreeNode(4)
    node2 = TreeNode(2)
    node5 = TreeNode(5)
    node1 = TreeNode(1)
    node3 = TreeNode(3)

    root.left = node2
    root.right = node5
    node2.left = node1
    node2.right = node3

    assert Solution_426().tree_to_doubly_list(root).val == 1

    # VARIANT: Convert Binary Tree to Circular Doubly Linked List according to its
    #          Inorder Traversal in place.
    # SOURCE: https://youtu.be/tzp1GYRn19k?si=b1WzDJ-Qyb3Ms_ed&t=889
    r"""
                1
               / \
              2   3
             / \   \
            4   5   8
               / \ /
              6  7 9
    """
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node5.left = node6
    node5.right = node7
    node3.right = node8
    node8.left = node9

    assert Solution_426().tree_to_doubly_list(root).val == 4
