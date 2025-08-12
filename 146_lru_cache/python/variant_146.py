import unittest

class ListNode:
    def __init__(self,key,val):
        self.key   = key 
        self.val   = val
        self.next  = None
        self.prev  = None
        

class LRUCache_146_Variant:

    def __init__(self):
        self.hash = {}
        self.leftest = ListNode(0,0)
        self.rightest = ListNode(0,0)

        self.leftest.next = self.rightest
        self.rightest.prev = self.leftest


    def get(self, key: int) -> int:
        if not key in self.hash: return -1
        node = self.hash[key]
        self._delete(node)
        self._add(node)
        return node.val

    def _add(self,newNode):
        nxt = self.leftest.next
        self.leftest.next = newNode
        newNode.prev = self.leftest

        nxt.prev= newNode
        newNode.next = nxt

    def _delete(self,node:ListNode):
        prev = node.prev 
        nxt=  node.next
        prev.next = nxt
        nxt.prev= prev
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            self._delete(node)
        
        newNode= ListNode(key,value)
        self.hash[key] = newNode
        self._add(newNode)

 
    def last(self):
        
        return -1 if self.leftest.next == self.rightest else self.leftest.next.val

    def del_(self, key): # Using del_ to avoid conflict with Python's 'del' keyword
        

        if key not in self.hash: return False
        self._delete(self.hash[key])
        del self.hash[key]
        return True


class TestLRUCacheVariant(unittest.TestCase):

    def test_Get_MovesNodeToEnd(self):
        cache = LRUCache_146_Variant()
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        
        self.assertEqual(1, cache.get(1))
        self.assertEqual(1, cache.last())

        self.assertEqual(3, cache.get(3))
        self.assertEqual(3, cache.last())

        self.assertEqual(2, cache.get(2))
        self.assertEqual(2, cache.last())

    def test_Put_MovesNodeToEnd(self):
        cache = LRUCache_146_Variant()
        cache.put(1, 1)
        self.assertEqual(1, cache.last())
        self.assertEqual(1, cache.get(1))

        cache.put(2, 2)
        self.assertEqual(2, cache.get(2))
        self.assertEqual(2, cache.last())

        cache.put(3, 3)
        self.assertEqual(3, cache.get(3))
        self.assertEqual(3, cache.last())

    def test_PutAndGet_DifferentKeyAndValue(self):
        cache = LRUCache_146_Variant()
        cache.put(1, 1000)
        cache.put(2, 2000)
        cache.put(3, 3000)
        
        self.assertEqual(1000, cache.get(1))
        self.assertEqual(1000, cache.last())

        self.assertEqual(3000, cache.get(3))
        self.assertEqual(3000, cache.last())

        self.assertEqual(2000, cache.get(2))
        self.assertEqual(2000, cache.last())

    def test_GetNotFound_ReturnsNegativeOne(self):
        cache = LRUCache_146_Variant()
        self.assertEqual(-1, cache.get(1))
        self.assertEqual(-1, cache.get(1))

        cache.put(1, 1)
        self.assertEqual(-1, cache.get(2))

        cache.put(2, 2)
        self.assertEqual(-1, cache.get(3))

        cache.put(3, 3)
        self.assertEqual(-1, cache.get(4))

        self.assertEqual(-1, cache.get(9000))
        
        self.assertEqual(1, cache.get(1))
        self.assertEqual(1, cache.last())
        self.assertEqual(3, cache.get(3))
        self.assertEqual(3, cache.last())
        self.assertEqual(2, cache.get(2))
        self.assertEqual(2, cache.last())

    def test_Put_CreateAndUpdate(self):
        cache = LRUCache_146_Variant()
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)

        cache.put(1, 1000)
        self.assertEqual(1000, cache.last())

        cache.put(2, 2000)
        self.assertEqual(2000, cache.last())

        cache.put(3, 3000)
        self.assertEqual(3000, cache.last())

    def test_Delete_GetsAndLastsCorrectly(self):
        cache = LRUCache_146_Variant()
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.put(4, 4)
        cache.put(5, 5)
        cache.put(6, 6)
        cache.put(7, 7)
        cache.put(8, 8)

        self.assertTrue(cache.del_(8))
        self.assertEqual(7, cache.last())
        self.assertEqual(7, cache.get(7))

        self.assertTrue(cache.del_(7))
        self.assertEqual(6, cache.last())
        self.assertEqual(6, cache.get(6))

        self.assertTrue(cache.del_(6))
        self.assertEqual(5, cache.last())
        self.assertEqual(5, cache.get(5))

        self.assertTrue(cache.del_(5))
        self.assertEqual(4, cache.last())
        self.assertEqual(4, cache.get(4))

        self.assertTrue(cache.del_(4))
        self.assertEqual(3, cache.last())
        self.assertEqual(3, cache.get(3))

        self.assertTrue(cache.del_(3))
        self.assertEqual(2, cache.last())
        self.assertEqual(2, cache.get(2))

        self.assertTrue(cache.del_(2))
        self.assertEqual(1, cache.last())
        self.assertEqual(1, cache.get(1))

        self.assertTrue(cache.del_(1))
        self.assertEqual(-1, cache.last())
        self.assertEqual(-1, cache.get(1))

    def test_Delete_NotFound_ReturnsFalse(self):
        cache = LRUCache_146_Variant()
        self.assertFalse(cache.del_(9000))

        cache.put(1, 1)
        self.assertFalse(cache.del_(9000))

        cache.put(2, 2)
        self.assertFalse(cache.del_(9000))

        cache.put(3, 3)
        self.assertFalse(cache.del_(9000))

        cache.put(4, 4)
        self.assertFalse(cache.del_(9000))

    def test_Last_NotFound_ReturnsNegativeOne(self):
        cache = LRUCache_146_Variant()
        self.assertEqual(-1, cache.last())
        self.assertEqual(-1, cache.last())

        cache.put(9000, 9000)
        cache.del_(9000)

        self.assertEqual(-1, cache.last())

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)