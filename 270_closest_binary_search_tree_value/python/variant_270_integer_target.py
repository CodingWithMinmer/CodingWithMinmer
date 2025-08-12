from utils.treenode import TreeNode


class Solution_270_Variant:
    def closestValue(self, root: TreeNode, target: int) -> int:
        closet = root.val
        while root:
            closet = min(closet,root.val,key=lambda x: ((abs(target-x),x)))
            root = root.left if root.val > target else root.right
        return closet
            

def test_exact_match():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)

    s = Solution_270_Variant()
    assert s.closestValue(root, 1) == 1
    assert s.closestValue(root, 2) == 2
    assert s.closestValue(root, 3) == 3
    assert s.closestValue(root, 4) == 4
    assert s.closestValue(root, 5) == 5
    print("ExactMatch tests passed!")

def test_greater_target_than_nodes():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    s = Solution_270_Variant()
    assert s.closestValue(root, 8) == 7
    assert s.closestValue(root, 9) == 7
    assert s.closestValue(root, 10) == 7
    assert s.closestValue(root, 9000) == 7
    print("GreaterTargetThanNodes tests passed!")

def test_lower_target_than_nodes():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    s = Solution_270_Variant()
    assert s.closestValue(root, 0) == 1
    assert s.closestValue(root, -1) == 1
    assert s.closestValue(root, -2) == 1
    assert s.closestValue(root, -9000) == 1
    print("LowerTargetThanNodes tests passed!")

def test_in_between_target():
    root = TreeNode(50)
    root.left = TreeNode(22)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(48)
    root.right = TreeNode(9000)

    s = Solution_270_Variant()
    assert s.closestValue(root, 55) == 50
    assert s.closestValue(root, 70) == 50
    assert s.closestValue(root, 1000) == 50
    assert s.closestValue(root, 3000) == 50

    assert s.closestValue(root, 9000) == 9000
    assert s.closestValue(root, 9500) == 9000
    assert s.closestValue(root, 9888) == 9000
    assert s.closestValue(root, 10000) == 9000
    assert s.closestValue(root, 11000) == 9000
    assert s.closestValue(root, 8000) == 9000
    assert s.closestValue(root, 7500) == 9000

    assert s.closestValue(root, 30) == 22
    assert s.closestValue(root, 25) == 22
    assert s.closestValue(root, 21) == 22

    assert s.closestValue(root, 10) == 10
    assert s.closestValue(root, -10) == 10

    # Ties between nodes 48 and 50, so we go with the smaller value, the 48
    assert s.closestValue(root, 49) == 48
    assert s.closestValue(root, 48) == 48
    assert s.closestValue(root, 39) == 48
    print("InBetweenTarget tests passed!")

if __name__ == "__main__":
    test_exact_match()
    test_greater_target_than_nodes()
    test_lower_target_than_nodes()
    test_in_between_target()
    print("\nAll tests passed!")