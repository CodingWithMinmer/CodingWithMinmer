from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leftRightSideViewVariant(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        left_side = []
        right_side = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()

                if i == 0:
                    left_side.append(node.val)
                if size == i + 1:
                    right_side.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        result = []
        result.extend(reversed(left_side))
        result.extend(right_side[1:])
        return result


if __name__ == "__main__":
    solution = Solution()
    # Test Case 1: Based on the example in the problem
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    /     \
    #   5       4
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(5)
    root1.right.right = TreeNode(4)
    assert solution.leftRightSideViewVariant(root1) == [5, 2, 1, 3, 4]
    # Test Case 2: Based on the second example
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    assert solution.leftRightSideViewVariant(root2) == [4, 2, 1, 3, 5]

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.right = TreeNode(7)
    root1.right.left = TreeNode(6)
    root1.right.right.left = TreeNode(8)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    assert solution.leftRightSideViewVariant(root1) == [8, 4, 2, 1, 3, 7, 8]

    root2 = TreeNode(1)
    assert solution.leftRightSideViewVariant(root2) == [1]

    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    assert solution.leftRightSideViewVariant(root3) == [3, 2, 1, 2, 3]

    root4 = None
    assert solution.leftRightSideViewVariant(root4) == []

    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)
    root5.right.left = TreeNode(5)
    root5.right.left.right = TreeNode(6)
    root5.right.left.right.right = TreeNode(7)
    root5.left.right = TreeNode(4)
    assert solution.leftRightSideViewVariant(root5) == [7, 6, 4, 2, 1, 3, 5, 6, 7]
