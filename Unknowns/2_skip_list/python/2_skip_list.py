from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.top = None
        self.bottom = None

class SkipList:
    def search(self, root: Optional['Node'], target: int) -> bool:
        if root is None:
            return False
        if root.val == target:
            return True
        
        c = root
        while c is not None:
            while c.next is not None and c.next.val <= target:
                c = c.next
                if c.val == target:
                    return True
            c = c.bottom

        return False