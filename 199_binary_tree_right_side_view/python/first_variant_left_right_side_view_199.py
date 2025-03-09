from ...utils.treenode import TreeNode
from typing import Optional
from collections import deque


class Solution:
    def leftRightSideViewVariant(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        leftside = []
        rightside = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                curr = queue.popleft()
                if i == 0:
                    leftside.append(curr.val)
                if i == level_length - 1 and level_length != 1:
                    rightside.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return leftside[::-1] + rightside


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
