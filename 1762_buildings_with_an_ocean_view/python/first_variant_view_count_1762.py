import unittest
from typing import List


def findBuildingViewCount_variant_1762(heights: List[int]) -> int:
    count =0
    n = len(heights)
    prev = None
    for i in range(n-1,-1,-1):
        v = heights[i]
        if prev == None or prev < v:
            count +=1
            prev=  v
    
    return count
    

# --- Unit Test Suite ---
class TestBuildingViewCount(unittest.TestCase):

    def test_building_view_count_case_1(self):
        heights = [4, 2, 3, 1]
        self.assertEqual(3, findBuildingViewCount_variant_1762(heights))

    def test_building_view_count_case_2(self):
        heights = [6, 1, 2, 4, 2, 2, 2, 2, 3, 1]
        self.assertEqual(4, findBuildingViewCount_variant_1762(heights))

    def test_building_view_count_case_3(self):
        heights = [4, 3, 2, 1]
        self.assertEqual(4, findBuildingViewCount_variant_1762(heights))

    def test_building_view_count_case_4(self):
        heights = [1, 3, 2, 4]
        self.assertEqual(1, findBuildingViewCount_variant_1762(heights))

    def test_building_view_count_case_5(self):
        heights = [2, 2, 2, 2, 2, 2, 2]
        self.assertEqual(1, findBuildingViewCount_variant_1762(heights))

    def test_building_view_count_case_6(self):
        heights = [0, 1, 2, 3, 2, 1, 0]
        self.assertEqual(4, findBuildingViewCount_variant_1762(heights))

    def test_building_view_count_case_7(self):
        heights = [1, 2, 3, 4]
        self.assertEqual(1, findBuildingViewCount_variant_1762(heights))

    def test_building_view_count_single_element(self):
        heights = [10]
        self.assertEqual(1, findBuildingViewCount_variant_1762(heights))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)