class SolutionVariant:
    def postorder(self, currNode):
        if currNode is None:
            return 0, 0

        leftSum, leftNodes = self.postorder(currNode.left)
        rightSum, rightNodes = self.postorder(currNode.right)
        if leftNodes == -1 or rightNodes == -1:
            return -1, -1
        
        sum = leftSum + rightSum + currNode.val
        nodes = leftNodes + rightNodes + 1
        if sum // nodes != currNode.val:
            return -1, -1

        return sum, nodes
    
    def isSubtreeAverage(self, root):
        _, result = self.postorder(root)
        return result != -1