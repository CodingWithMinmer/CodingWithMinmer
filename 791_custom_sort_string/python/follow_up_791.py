class Solution:
    def customSortString(self, order: list[str], s: str) -> str:
        vector_space = [0] * 26
        for c in s:
            vector_space[ord(c)-ord('a')] +=1 
        result =[]
        for c in order:
            key = ord(c)-ord('a')
            result += [c]*vector_space[key]
            vector_space[key] = 0

        for c in s:
            key = ord(c)-ord('a')
            if vector_space[key] > 0:
                
                result += [c] * vector_space[key]
        return ''.join(result)
       
import unittest

class TestCustomSortString(unittest.TestCase):
    def test_first_variant_valid(self):
        
        order = ['b', 'c', 'a', 'f', 'g']
        s = "abcd"
        self.assertEqual("bcad", Solution().customSortString(order, s))

if __name__ == '__main__':
    unittest.main()