import collections

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None 

def lowestCommonAncestor_second_variant_1650(nodes, p, q):
    childToParent = {}
    for node in nodes:
        if node.left:
            childToParent[node.left] = node
        if node.right:
            childToParent[node.right] = node
    pStart = p
    qStart = q
    while p != q:
        if childToParent.get(p):
            p = childToParent[p]
        else:
            p = qStart
        
        if childToParent.get(q):
            q = childToParent[q]
        else:
            q = pStart

    return p    
        
    


def test_lowestCommonAncestor_second_variant_1650():
    # Tree construction
    root = Node(1)
    
    node_2 = Node(2)
    root.left = node_2
    node_2.parent = root

    node_4 = Node(4)
    node_2.left = node_4
    node_4.parent = node_2

    node_5 = Node(5)
    node_2.right = node_5
    node_5.parent = node_2

    node_6 = Node(6)
    node_5.right = node_6
    node_6.parent = node_5

    node_7 = Node(7)
    node_6.left = node_7
    node_7.parent = node_6

    node_3 = Node(3)
    root.right = node_3
    node_3.parent = root

    nodes = [root, node_2, node_4, node_5, node_6, node_7, node_3] 

    # Assertions
    assert lowestCommonAncestor_second_variant_1650(nodes, node_4, node_7) == node_2, "Test Case 1 Failed: different subtrees"
    assert lowestCommonAncestor_second_variant_1650(nodes, node_3, node_3) == node_3, "Test Case 2 Failed: same node" # Note: Original C++ comment says "not allowed as LC input due to constraints". For this specific problem (1650), p and q can be the same node, and the LCA is the node itself.
    assert lowestCommonAncestor_second_variant_1650(nodes, node_5, node_6) == node_5, "Test Case 3 Failed: same subtree and answer is p"
    assert lowestCommonAncestor_second_variant_1650(nodes, node_5, node_7) == node_5, "Test Case 4 Failed: same subtree"
    assert lowestCommonAncestor_second_variant_1650(nodes, root, node_3) == root, "Test Case 5 Failed: root and a child"

    print("All tests passed!")

if __name__ == '__main__':
    test_lowestCommonAncestor_second_variant_1650()