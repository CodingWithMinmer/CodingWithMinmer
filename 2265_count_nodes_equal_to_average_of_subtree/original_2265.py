class Solution:
    def __init__(self):
        self.count = 0

    def postorder(self, currNode):
        if currNode is None:
            return 0, 0 

        leftSum, leftNodes  = self.postorder(currNode.left)
        rightSum, rightNodes = self.postorder(currNode.right)

        sum  = leftSum + rightSum + currNode.val
        nodes  = leftNodes + rightNodes + 1
        if sum // nodes  == currNode.val:
            self.count += 1

        return sum, nodes

    def averageOfSubtree(self, root):
        self.postorder(root)
        return self.count