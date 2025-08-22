from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.top = None
        self.bottom = None


class SkipList:
    def search_closest(self, root: Optional["Node"], target: int) -> Optional["Node"]:
        if root is None:
            return None
        if root.val == target:
            return root

        c = root
        while c.bottom is not None:
            while c.next is not None and c.next.val <= target:
                c = c.next
                if c.val == target:
                    return c
            c = c.bottom

        while c.next is not None and c.next.val <= target:
            c = c.next
        return c
