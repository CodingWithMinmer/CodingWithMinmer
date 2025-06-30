from typing import Optional
import math


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


# VARIANT: What if the target parameter was given as an integer, not a
#          float?
# SOURCE: https://youtu.be/atHrOx3ibas?si=2cQehGMjBrBeDYwU&t=1157
class Solution_270:
    def closest_value(self, root: Optional[TreeNode], target: int):
        """
        Time Complexity: O(h), where: h is the height of the BST
        Space Complexity: O(1)
        """
        closest_distance = result = math.inf

        while root:
            distance = abs(root.val - target)
            if (distance < closest_distance) or (
                (distance == closest_distance) and (root.val < result)
            ):
                closest_distance = distance
                result = root.val

            if not distance:
                return root.val

            if root.val < target:
                root = root.right
            else:
                root = root.left

        return result


if __name__ == "__main__":
    r"""
                4
               / \
              2   6
             / \ / \
            1  3 5  7
    """
    root = TreeNode(4)
    node2 = TreeNode(2)
    node6 = TreeNode(6)
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node7 = TreeNode(7)

    root.left = node2
    root.right = node6
    node2.left = node1
    node2.right = node3
    node6.left = node5
    node6.right = node7

    assert Solution_270().closest_value(root=root, target=4) == 4
    assert Solution_270().closest_value(root=root, target=3) == 3

    """
        1
    """

    root = TreeNode(1)
    assert Solution_270().closest_value(root=root, target=3) == 1
