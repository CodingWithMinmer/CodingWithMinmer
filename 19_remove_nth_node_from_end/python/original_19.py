from utils.ListNode import ListNode


class Solution_19:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head

        r = dummy
        for _ in range(n):
            r = r.next

        l = dummy
        while r.next is not None:
            r = r.next
            l = l.next

        l.next = l.next.next
        return dummy.next
