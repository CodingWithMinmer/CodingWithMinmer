from utils.ListNode import ListNode


class Solution_19_Variant:
    def removeIthFromBeginning(self, head, n):
        dummy = ListNode()
        dummy.next = head

        i = dummy
        for _ in range(n):
            if i.next is None:
                return dummy.next
            i = i.next

        if i.next is None:
            return dummy.next

        i.next = i.next.next
        return dummy.next
