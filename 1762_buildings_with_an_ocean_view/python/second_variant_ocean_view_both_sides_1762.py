import unittest
from typing import List

def findBuildingViewCount_second_variant_1762(heights: List[int]) -> List[int]:
    left = 0
    right = len(heights)-1
    leftmax= heights[left]
    rightmax= heights[right]
    left_view = [left]
    right_view = [right]
    while left < right:
        if leftmax < rightmax:
            left +=1
            if leftmax < heights[left] and left < right:
                leftmax = heights[left]
                left_view.append(left)

        else:
            right -=1
            if rightmax < heights[right] and left < right:
                rightmax = heights[right]
                right_view.append(right)
    return left_view + right_view[::-1]

# --- Unit Test Suite ---
class TestBuildingViewCountSecondVariant(unittest.TestCase):

    def test_variant_2_case_1(self):
        heights = [1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 2]
        both_views = findBuildingViewCount_second_variant_1762(heights)
        self.assertEqual(11, len(both_views))
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expected, both_views)

    def test_variant_2_case_2(self):
        heights = [1, 2, 3, 3, 2, 1]
        both_views = findBuildingViewCount_second_variant_1762(heights)
        self.assertEqual(6, len(both_views))
        expected = [0, 1, 2, 3, 4, 5]
        self.assertEqual(expected, both_views)

    def test_variant_2_case_3(self):
        heights = [1, 4, 3, 9, 8, 6]
        both_views = findBuildingViewCount_second_variant_1762(heights)
        self.assertEqual(5, len(both_views))
        expected = [0, 1, 3, 4, 5]
        self.assertEqual(expected, both_views)

    def test_variant_2_case_4(self):
        heights = [1, 2, 1, 1, 3, 1, 1, 3, 1, 3, 2, 1]
        both_views = findBuildingViewCount_second_variant_1762(heights)
        self.assertEqual(6, len(both_views))
        expected = [0, 1, 4, 9, 10, 11] 
        self.assertEqual(expected, both_views)

    def test_variant_2_case_5(self):
        heights = [1, 1, 1, 1]
        both_views = findBuildingViewCount_second_variant_1762(heights)
        self.assertEqual(2, len(both_views))
        expected = [0, 3] # Assuming first and last are visible if all are same height
        self.assertEqual(expected, both_views)

    def test_variant_2_single_element(self):
        heights = [5]
        both_views = findBuildingViewCount_second_variant_1762(heights)
        self.assertEqual(1, len(both_views))
        expected = [0]
        self.assertEqual(expected, both_views)

    def test_variant_2_two_elements(self):
        heights = [1, 10]
        both_views = findBuildingViewCount_second_variant_1762(heights)
        self.assertEqual(2, len(both_views))
        expected = [0, 1]
        self.assertEqual(expected, both_views)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)