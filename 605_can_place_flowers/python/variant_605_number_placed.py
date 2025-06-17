from typing import List
import unittest

class Solution_605_Variant:
    def placeFlowers(self, flowerbed: list[int]) -> int:
        placed = 0
        n = len(flowerbed)
        for i in range(n):
            left_pointer = 0 if i == 0 else flowerbed[i-1]
            right_pointer = 0 if i == n-1 else flowerbed[i+1]
            if flowerbed[i] == right_pointer == left_pointer:
                placed +=1
                flowerbed[i] = 1
                i +=2
            elif flowerbed[i]:
                i +=2
            else:
                i +=3
        return placed

        


class TestCanPlaceFlowersVariantNumbersPlaced(unittest.TestCase):

    def setUp(self):
        self.s = Solution_605_Variant()

    def test_all_zeroes(self):
        self.assertEqual(self.s.placeFlowers([0]), 1)
        self.assertEqual(self.s.placeFlowers([0, 0]), 1)
        self.assertEqual(self.s.placeFlowers([0, 0, 0]), 2)
        self.assertEqual(self.s.placeFlowers([0, 0, 0, 0]), 2)
        self.assertEqual(self.s.placeFlowers([0, 0, 0, 0, 0]), 3)
        self.assertEqual(self.s.placeFlowers([0, 0, 0, 0, 0, 0]), 3)

    def test_as_many_ones_as_possible(self):
        self.assertEqual(self.s.placeFlowers([1]), 0)
        self.assertEqual(self.s.placeFlowers([0, 1]), 0)
        self.assertEqual(self.s.placeFlowers([1, 0]), 0)
        self.assertEqual(self.s.placeFlowers([1, 0, 1]), 0)
        self.assertEqual(self.s.placeFlowers([0, 1, 0]), 0)
        self.assertEqual(self.s.placeFlowers([1, 0, 1, 0]), 0)
        self.assertEqual(self.s.placeFlowers([0, 1, 0, 1]), 0)
        self.assertEqual(self.s.placeFlowers([1, 0, 1, 0, 1, 0]), 0)
        self.assertEqual(self.s.placeFlowers([0, 1, 0, 1, 0, 1]), 0)

    def test_hybrid(self):
        self.assertEqual(self.s.placeFlowers([1, 0, 0, 0, 0, 0]), 2)
        self.assertEqual(self.s.placeFlowers([1, 0, 1, 0, 0, 0]), 1)
        self.assertEqual(self.s.placeFlowers([0, 1, 0, 0, 0, 0, 0, 0, 0]), 3)
        self.assertEqual(self.s.placeFlowers([0, 1, 0, 0, 1, 0, 0, 0, 0]), 2)
        self.assertEqual(self.s.placeFlowers([0, 1, 0, 0, 1, 0, 0, 0, 1]), 1)
        self.assertEqual(self.s.placeFlowers([1, 0, 0, 0, 0, 0, 0, 0, 1]), 3)
        self.assertEqual(self.s.placeFlowers([1, 0, 0, 0, 1, 0, 0, 0, 1]), 2)
    
    def edgeCase(self):
        self.assertEqual(self.s.placeFlowers([0, 1, 0, 0, 0, 0, 0, 0],4))

if __name__ == '__main__':
    unittest.main()   