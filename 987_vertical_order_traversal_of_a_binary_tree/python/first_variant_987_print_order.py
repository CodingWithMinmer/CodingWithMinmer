from collections import deque


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


# VARIANT: What if you had to print the order of nodes?
# SOURCE: https://youtu.be/m19-r7hswx0?si=Jus1k2PFZVfeUn-v&t=1682
class Solution_987_First_Variant:
    def level_order_traversal(
        self, root: TreeNode, col_to_node_and_row: dict[int, tuple[TreeNode, int]]
    ):
        leftmost_col = rightmost_col = 0
        queue = deque([(0, 0, root)])

        while queue:
            row, col, node = queue.popleft()

            if col not in col_to_node_and_row:
                col_to_node_and_row[col] = [(node, row)]
            else:
                col_to_node_and_row[col].append((node, row))

            leftmost_col = min(leftmost_col, col)
            rightmost_col = max(rightmost_col, col)

            if node.left:
                queue.append((row + 1, col - 1, node.left))

            if node.right:
                queue.append((row + 1, col + 1, node.right))

        return (leftmost_col, rightmost_col)

    def vertical_traversal(self, root: TreeNode) -> list[list[int]]:
        """
        Time Complexity: O (N.log(N/C)), where C is the number of columns
        Space Complexity: O(N)
        """
        col_to_node_and_row = {}
        leftmost_col, rightmost_col = self.level_order_traversal(
            root, col_to_node_and_row
        )

        for col in range(leftmost_col, rightmost_col + 1):
            curr_col = sorted(col_to_node_and_row[col], key=lambda x: (x[1], x[0].val))

            for node in curr_col:
                print(node[0].val, end=" ")
            print()


if __name__ == "__main__":
    print(
        r"""
                    16
                   /  \
                  8    7
                 / \  / \
                3  15 10 9
                 \
                  1
    
    """
    )
    root = TreeNode(16)
    node8 = TreeNode(8)
    node7 = TreeNode(7)
    node3 = TreeNode(3)
    node15 = TreeNode(15)
    node10 = TreeNode(10)
    node9 = TreeNode(9)
    node1 = TreeNode(1)

    root.left = node8
    root.right = node7
    node8.left = node3
    node8.right = node15
    node7.left = node10
    node7.right = node9
    node3.right = node1

    Solution_987_First_Variant().vertical_traversal(root)

    print("-" * 100)
    print(
        r"""
                    3
                   / \
                  9   20
                     /  \
                   15    7
                 
    """
    )
    root = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)

    root.left = node9
    root.right = node20
    node20.left = node15
    node20.right = node7

    Solution_987_First_Variant().vertical_traversal(root)
