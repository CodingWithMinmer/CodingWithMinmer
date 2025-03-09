from ...utils.treenode import TreeNode
    
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        root_to_leaf = 0
        positive = True
        def preorder(node: TreeNode, curr_num: int):
            nonlocal root_to_leaf
            nonlocal positive
            if node:
                positive = False if node.val < 0 else True
                curr_num = curr_num * 10 + abs(node.val)
                if node.left is None or node.right is None:
                    root_to_leaf += curr_num if positive else -curr_num
                    positive = True
                
                preorder(node.left, curr_num)
                preorder(node.right, curr_num)

        preorder(root, 0)

        return root_to_leaf


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1, left=TreeNode(-2), right=TreeNode(3))
    assert solution.sumNumbers(root) == 1