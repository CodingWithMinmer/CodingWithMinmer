class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def areSame(head1: Node, head2: Node) -> bool:
    p1, p2 = head1, head2
    i = j = 0
    while p1 and p2:
        val1, val2 = p1.val, p2.val
        len1, len2 = len(val1), len(val2)

        while i < len1 and j < len2:
            if val1[i] != val2[j]:
                return False
            i += 1
            j += 1

        if i == len1:
            i = 0
            p1 = p1.next
        if j == len2:
            j = 0
            p2 = p2.next

    return p1 is None and p2 is None