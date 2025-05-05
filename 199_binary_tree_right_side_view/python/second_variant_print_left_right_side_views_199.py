from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leftRightSideViewVariantPrint(self, root: Optional[TreeNode]):
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

        for left_value in left_side[-1:0:-1]:
            print(left_value)
        for right_value in right_side:
            print(right_value)


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
    solution.leftRightSideViewVariantPrint(root1)  # Should print 5, 2, 1, 3, 4 in order
    print("-")
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
    solution.leftRightSideViewVariantPrint(root2)  # Should print 4, 2, 1, 3, 5 in order
    print("-")

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
    solution.leftRightSideViewVariantPrint(root1)  # Expected output: 5 2 1 3 4
    print("-")

    root2 = TreeNode(1)
    solution.leftRightSideViewVariantPrint(root2)  # Expected output: 1
    print("-")

    root3 = None
    solution.leftRightSideViewVariantPrint(root3)  # Expected output: (nothing)
    print("-")

    # Tree structure:
    #       1
    #      /
    #     2
    #    /
    #   3
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    solution.leftRightSideViewVariantPrint(root4)  # Expected output: 3 2 1 2 3
