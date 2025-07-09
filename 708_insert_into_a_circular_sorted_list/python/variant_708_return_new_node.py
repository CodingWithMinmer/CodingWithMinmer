from typing import Optional

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        prev, curr = head, head.next
        while True:
            if prev.val <= insertVal <= curr.val:
                break
            if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
                break

            prev, curr = curr, curr.next
            if prev == head:
                break
        
        prev.next = Node(insertVal, curr)
        return prev.next

class TestSolution:
    def test_happy_path(self):
        head = Node(5)
        head.next = Node(10, Node(10, Node(15, Node(20, head))))
        s = Solution()
        node = s.insert(head, 19)
        assert 19 == node.val
        assert 20 == node.next.val
        assert 5 == node.next.next.val
        assert 10 == node.next.next.next.val
        assert 10 == node.next.next.next.next.val
        assert 15 == node.next.next.next.next.next.val
        assert 19 == node.next.next.next.next.next.next.val

        head = Node(5)
        head.next = Node(10, Node(10, Node(15, Node(20, head))))
        node = s.insert(head, 10)
        assert 10 == node.val
        assert 10 == node.next.val
        assert 10 == node.next.next.val
        assert 15 == node.next.next.next.val
        assert 20 == node.next.next.next.next.val
        assert 5 == node.next.next.next.next.next.val
        assert 10 == node.next.next.next.next.next.next.val
    def test_out_of_range(self):
        head = Node(666)
        head.next = Node(9000, Node(420, head))
        s = Solution()
        node = s.insert(head, 9500)
        assert 9500 == node.val
        assert 420 == node.next.val
        assert 666 == node.next.next.val
        assert 9000 == node.next.next.next.val
        assert 9500 == node.next.next.next.next.val

        head = Node(666)
        head.next = Node(9000, Node(420, head))
        node = s.insert(head, 10)
        assert 10 == node.val
        assert 420 == node.next.val
        assert 666 == node.next.next.val
        assert 9000 == node.next.next.next.val
        assert 10 == node.next.next.next.next.val
    def test_null_head(self):
        s = Solution()
        head = s.insert(None, 9000)
        assert 9000 == head.val
        assert head == head.next
    def test_all_duplicates(self):
        head = Node(7)
        head.next = Node(7, Node(7, head))
        s = Solution()
        node = s.insert(head, 1)
        assert 1 == node.val
        assert 7 == node.next.val
        assert 7 == node.next.next.val
        assert 7 == node.next.next.next.val
        assert 1 == node.next.next.next.next.val