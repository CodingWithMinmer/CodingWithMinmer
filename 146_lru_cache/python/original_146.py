# LC: https://leetcode.com/problems/lru-cache/
# SOURCE: https://youtu.be/LZgDpjCIHm0?si=Wx1HXUtfEvtjrx--
class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class LRUCache_146:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.key_to_node = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        curr = self.key_to_node[key]
        self.rewire_pointers(curr)
        self.move_to_end(curr)
        return curr.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            curr = self.key_to_node[key]
            self.rewire_pointers(curr)
            del self.key_to_node[key]

        inserted = Node(key, value)
        self.key_to_node[key] = inserted
        self.move_to_end(inserted)

        if len(self.key_to_node) > self.capacity:
            node_to_delete = self.head.right
            self.rewire_pointers(node_to_delete)
            del self.key_to_node[node_to_delete.key]

    def move_to_end(self, curr: Node) -> None:
        previous_end = self.tail.left
        previous_end.right = curr
        curr.left = previous_end
        curr.right = self.tail
        self.tail.left = curr

    def rewire_pointers(self, node: Node) -> None:
        node.left.right = node.right
        node.right.left = node.left


if __name__ == "__main__":
    obj = LRUCache_146(capacity=1)
    assert obj.get(key=9000) == -1

    obj = LRUCache_146(capacity=3)
    obj.put(key=1, value=1)
    obj.put(key=20, value=2)
    obj.put(key=3, value=3)
    assert obj.get(key=1) == 1
    obj.put(key=4, value=4)
    obj.put(key=3, value=5)
    assert obj.get(key=4) == 4
    obj.put(key=5, value=5)
    assert obj.get(key=1) == -1
