from typing import Optional


class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def getPlaces(num: int):
            if not num:
                return 10

            places = 1
            while num > 0:
                num = num // 10
                places *= 10
            return places

        def preorder(node: Solution.TreeNode, curr_number: int):
            nonlocal root_to_leaf
            if node:
                places = getPlaces(node.val)
                curr_number = (curr_number * places) + node.val
                if not (node.left or node.right):
                    root_to_leaf += curr_number
                preorder(node.left, curr_number)
                preorder(node.right, curr_number)

        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf


if __name__ == "__main__":
    solution = Solution()
    root = Solution.TreeNode(3)
    root.left = Solution.TreeNode(79, right=Solution.TreeNode(111))
    root.right = Solution.TreeNode(2)
    assert solution.sumNumbers(root) == 379143

    root = Solution.TreeNode(1)
    root.left = Solution.TreeNode(2)
    root.left.left = Solution.TreeNode(90)
    root.right = Solution.TreeNode(42)
    root.right.left = Solution.TreeNode(511)
    assert solution.sumNumbers(root) == 1290 + 142511

    root = Solution.TreeNode(1)
    root.left = Solution.TreeNode(2)
    root.left.left = Solution.TreeNode(912)
    root.left.left.left = Solution.TreeNode(3)
    root.left.left.right = Solution.TreeNode(4)
    root.right = Solution.TreeNode(46)
    root.right.left = Solution.TreeNode(5)
    root.right.right = Solution.TreeNode(61)
    assert solution.sumNumbers(root) == 129123 + 129124 + 1465 + 14661

    root = Solution.TreeNode(1)
    root.left = Solution.TreeNode(2)
    root.right = Solution.TreeNode(3)
    assert solution.sumNumbers(root) == 12 + 13

    root = Solution.TreeNode(10)
    root.left = Solution.TreeNode(200)
    root.right = Solution.TreeNode(3000)
    assert solution.sumNumbers(root) == 10200 + 103000

    root = Solution.TreeNode(10)
    root.left = Solution.TreeNode(0)
    root.right = Solution.TreeNode(0)
    assert solution.sumNumbers(root) == 200

    root = None
    assert solution.sumNumbers(root) == 0
