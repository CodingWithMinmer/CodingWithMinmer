class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node, curr_sum, num_negatives):
            if node is None:
                return 0

            curr_sum = (curr_sum * 10) + abs(node.val)
            if node.val < 0:
                num_negatives += 1

            if node.left is None and node.right is None:
                sign = -1 if num_negatives % 2 == 1 else 1
                return curr_sum * sign

            left_sum = helper(node.left, curr_sum, num_negatives)
            right_sum = helper(node.right, curr_sum, num_negatives)

            return left_sum + right_sum

        return helper(root, 0, 0)


if __name__ == "__main__":
    solution = Solution()
    root = Solution.TreeNode(1, left=Solution.TreeNode(-2), right=Solution.TreeNode(3))
    assert solution.sumNumbers(root) == 1

    root = Solution.TreeNode(
        -1,
        left=Solution.TreeNode(-2, left=Solution.TreeNode(-9)),
        right=Solution.TreeNode(4, left=Solution.TreeNode(-5)),
    )
    assert solution.sumNumbers(root) == -129 + 145

    root = Solution.TreeNode(
        -1,
        left=Solution.TreeNode(
            -2,
            left=Solution.TreeNode(
                -9, left=Solution.TreeNode(3), right=Solution.TreeNode(-3)
            ),
        ),
        right=Solution.TreeNode(
            4, left=Solution.TreeNode(-5), right=Solution.TreeNode(6)
        ),
    )
    assert solution.sumNumbers(root) == -1293 + 1293 + 145 + -146

    root = Solution.TreeNode(1, left=Solution.TreeNode(2), right=Solution.TreeNode(3))
    assert solution.sumNumbers(root) == 12 + 13

    root = Solution.TreeNode(
        -1, left=Solution.TreeNode(-2), right=Solution.TreeNode(-3)
    )
    assert solution.sumNumbers(root) == 12 + 13

    root = Solution.TreeNode(-1, left=Solution.TreeNode(-2, left=Solution.TreeNode(-3)))
    assert solution.sumNumbers(root) == -123

    root = None
    assert solution.sumNumbers(root) == 0
