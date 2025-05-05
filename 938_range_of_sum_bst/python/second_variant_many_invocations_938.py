from bisect import bisect_left
from itertools import accumulate
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, root):
        self.vals = []
        self.prefix_sums = []
        self.inorder(root)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.vals.append(root.val)
        if not self.prefix_sums:
            self.prefix_sums.append(root.val)
        else:
            self.prefix_sums.append(self.prefix_sums[-1] + root.val)
        self.inorder(root.right)

    def find_right_boundary(self, left, right, upper):
        while left <= right:
            mid = (right - left) // 2 + left
            if self.vals[mid] <= upper:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def find_left_boundary(self, left, right, lower):
        while left <= right:
            mid = (right - left) // 2 + left
            if self.vals[mid] >= lower:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def calculate(self, lower, upper):
        right_boundary = self.find_right_boundary(0, len(self.vals) - 1, upper)
        left_boundary = self.find_left_boundary(0, len(self.vals) - 1, lower)

        if left_boundary == 0:
            return self.prefix_sums[right_boundary]

        return self.prefix_sums[right_boundary] - self.prefix_sums[left_boundary - 1]


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(1)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(6)

    root.right = TreeNode(15)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(18)

    solution = Solution(root)
    assert solution.calculate(5, 16) == 56
    assert solution.calculate(0, 9000) == 1 + 3 + 5 + 6 + 7 + 10 + 13 + 15 + 18
    assert solution.calculate(7, 7) == 7
    assert solution.calculate(14, 18) == 33
    assert solution.calculate(3, 6) == 14
