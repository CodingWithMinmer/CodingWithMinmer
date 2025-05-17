from typing import Optional

class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.left = None
        self.right = None


# VARIANT: implement two more functions: the delete(key) and last() functions
# SOURCE: https://youtu.be/LZgDpjCIHm0?si=esN2nsCc88qBBnic&t=964
class LRUCache_146_Variant:
    def __init__(self) -> None:
        self.key_to_node = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, key: int) -> int:
        """
        Time Complexity: O(1)
        """
        if key not in self.key_to_node:
            return -1

        curr = self.key_to_node[key]
        self.rewire_pointers(curr)
        self.move_to_end(curr)
        return curr.val

    def put(self, key: int, value: int) -> None:
        """
        Time Complexity: O(1)
        """
        if key in self.key_to_node:
            curr = self.key_to_node[key]
            self.rewire_pointers(curr)
            del self.key_to_node[key]

        inserted = Node(key, value)
        self.key_to_node[key] = inserted
        self.move_to_end(inserted)

    def delete(self, key: int) -> bool:
        """
        Time Complexity: O(1)
        """
        if key not in self.key_to_node:
            return False

        remove = self.key_to_node[key]
        self.rewire_pointers(remove)
        del self.key_to_node[key]
        return True

    def last(self) -> Optional[Node]:
        """
        Time Complexity: O(1)
        """
        if self.tail.left == self.head:
            return -1

        return self.tail.left

    def move_to_end(self, curr: Optional[Node]) -> None:
        previous_end = self.tail.left
        previous_end.right = curr
        curr.left = previous_end
        curr.right = self.tail
        self.tail.left = curr

    def rewire_pointers(self, node: Optional[Node]) -> None:
        node.left.right = node.right
        node.right.left = node.left


if __name__ == "__main__":
    obj = LRUCache_146_Variant()
    assert obj.get(key=9000) == -1
    assert obj.last() == -1

    obj = LRUCache_146_Variant()
    obj.put(key=1, value=1)
    obj.put(key=20, value=2)
    obj.put(key=3, value=3)
    assert obj.get(key=1) == 1
    obj.put(key=4, value=4)
    obj.put(key=3, value=5)
    assert obj.get(key=4) == 4
    obj.put(key=5, value=5)
    assert obj.get(key=1) == 1

    obj = LRUCache_146_Variant()
    obj.put(key=1, value=1)
    obj.put(key=2, value=2)
    assert obj.get(key=1) == 1
    obj.put(key=3, value=3)
    assert obj.get(key=2) == 2
    obj.put(key=4, value=4)
    assert obj.get(key=1) == 1
    assert obj.get(key=3) == 3
    assert obj.get(key=4) == 4

    obj = LRUCache_146_Variant()
    obj.put(key=5, value=5)
    obj.put(key=3, value=30)
    obj.put(key=4, value=4)
    obj.put(key=9000, value=9000)
    assert obj.last().val == 9000
    assert obj.get(key=4) == 4
    assert obj.last().val == 4
    assert obj.delete(key=9000) == True
    assert obj.delete(key=9000) == False
    assert obj.delete(key=5) == True
    assert obj.delete(key=4) == True
    assert obj.delete(key=3) == True

    obj = LRUCache_146_Variant()
    obj.put(key=4, value=4)
    obj.put(key=5, value=5)
    obj.put(key=3, value=30)
    assert obj.last().val == 30
    assert obj.delete(key=5) == True
    assert obj.delete(key=4) == True
    assert obj.delete(key=3) == True
    assert obj.last() == -1
