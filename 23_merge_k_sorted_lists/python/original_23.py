import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class element:
    def __init__(self, node: Optional[ListNode]):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


# LC: https://leetcode.com/problems/merge-k-sorted-lists/
# SOURCE: https://youtu.be/ewjDj_s1HVU?si=rOp3ylCviTY6h8U2
class Solution_23:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Time Complexity: O(N.log k)
        Space Complexity: O(k)
        """
        min_pq = []

        for l in lists:
            if l:
                heapq.heappush(min_pq, element(l))

        dummy = ListNode(-1)
        current = dummy
        while min_pq:
            heap_node = heapq.heappop(min_pq)
            current.next = heap_node.node
            current = current.next
            if current.next:
                heapq.heappush(min_pq, element(current.next))

        return dummy.next


if __name__ == "__main__":

    def test(lists: List[Optional[ListNode]]):
        node = Solution_23().mergeKLists(lists)
        result = []
        while node:
            result.append(node.val)
            node = node.next

        return result

    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(3)
    l2.next = ListNode(5)
    l2.next.next = ListNode(10)

    l3 = ListNode(6)
    l4 = ListNode(7)

    assert test([l1, l2, l3, l4]) == [1, 2, 3, 4, 5, 6, 7, 10]

    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)
    assert test([l1, l2, l3]) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert test([]) == []
    assert test([[]]) == []
