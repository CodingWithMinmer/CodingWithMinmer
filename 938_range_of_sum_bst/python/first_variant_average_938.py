from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeAverageBST(self, root: Optional[TreeNode], low: int, high: int) -> float:
        result = 0
        count = 0
        stack = [root]
        while stack:
            curr = stack.pop()
            if low <= curr.val <= high:
                result += curr.val
                count += 1
            if curr.right and curr.val < high:
                stack.append(curr.right)
            if curr.left and curr.val > low:
                stack.append(curr.left)
        return result / count


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)

    root.right = TreeNode(15)
    root.right.right = TreeNode(18)

    assert solution.rangeAverageBST(root, 7, 15) == 32.0 / 3.0
    assert solution.rangeAverageBST(root, 0, 9000) == 58.0 / 6.0
    assert solution.rangeAverageBST(root, 7, 7) == 7.0
    assert solution.rangeAverageBST(root, 14, 18) == 33.0 / 2.0
    assert solution.rangeAverageBST(root, 3, 6) == 4.0
