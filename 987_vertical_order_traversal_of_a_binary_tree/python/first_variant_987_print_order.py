import collections

# --- Node Definition ---
# This class defines the structure of a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- Solution Class ---
# This class contains the logic for performing the vertical traversal.
class Solution987FirstVariant:
    def verticalTraversal(self, root: TreeNode):
        """
        Performs a vertical traversal of a binary tree and prints the nodes
        column by column, sorted by row and then by value for nodes in the same
        row and column.

        Args:
            root (TreeNode): The root of the binary tree.
        """

        res = []
        def dfs(node,r,c):
            if not node:return 

            res.append([c,r,node.val])
            
            dfs(node.left,r+1,c-1)
            dfs(node.right,r+1,c+1)
        dfs(root,0,0)
        res.sort()
        ret = collections.OrderedDict()
        for column,_,value in res:
            
            if column in ret:
                ret[column].append(value)
            else:
                ret[column] = [value]
        return list(ret.values())

        


# --- Example Usage ---
# This function demonstrates how to create a sample binary tree and perform
# the vertical traversal.
def vertical_traversal_987_first_variant_example():
    # Construct the tree as shown in the C++ example:
    #       6
    #      / \
    #     8   7
    #    / \ / \
    #   3  15 10 9
    #    \
    #     1

    root = TreeNode(6)
    root.left = TreeNode(8)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(15)
    root.left.left.right = TreeNode(1)

    root.right = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.left = TreeNode(10)

    s = Solution987FirstVariant()
    print("Vertical Traversal Output:")
    s.verticalTraversal(root)

# --- Run the example if the script is executed directly ---
if __name__ == "__main__":
    vertical_traversal_987_first_variant_example()