import unittest,random
def randomPickIndex_second_variant_398(nums: list[int]) -> int:
    """
    Mock implementation for the second variant: randomly picks an index of the maximum number.
    """
    maxVal = float('-inf')
    maxIndex = -1 
    n = 0
    for i in range(len(nums)):
        curVal = nums[i]
        if curVal > maxVal:
            n = 1
            maxVal = curVal
            maxIndex = i
        elif curVal == maxVal:
            n += 1
            r = int(random.random() % n)
            if r ==0:
                maxIndex = i

    return maxIndex
        
    

class TestRandomPickIndexSecondVariant(unittest.TestCase):
    """
    Tests for the second variant function: randomPickIndex_second_variant_398.
    """

    def test_happy_case(self):
        """
        Tests picking the index of the maximum number from a list with duplicates.
        """
        nums = [11, 11, 2, 30, 6, 30, 30, 2, 62, 62]
        # The maximum value is 62, found at indices 8 and 9.
        expected_indices = {8, 9}

        for _ in range(1000):
            picked_index = randomPickIndex_second_variant_398(nums)
            self.assertIn(picked_index, expected_indices) 
            self.assertEqual(nums[picked_index], 62) 

    def test_negative_numbers(self):
        """
        Tests picking the index of the maximum number from a list including negatives.
        """
        nums = [11, 11, 2, 30, 6, 30, 30, 2, 62, 62, -1, -2, -3, -4]
        # 62 is still the maximum value
        expected_indices = {8, 9}

        for _ in range(1000):
            picked_index = randomPickIndex_second_variant_398(nums)
            self.assertIn(picked_index, expected_indices)
            self.assertEqual(nums[picked_index], 62)

    def test_all_duplicates(self):
        """
        Tests picking the index of the maximum number when all elements are identical.
        """
        nums = [1, 1, 1, 1, 1]
        expected_indices = {0, 1, 2, 3, 4} # Any index is valid as all are max

        for _ in range(1000):
            picked_index = randomPickIndex_second_variant_398(nums)
            self.assertIn(picked_index, expected_indices)
            self.assertEqual(nums[picked_index], 1)

    def test_one_element(self):
        """
        Tests picking the index of the maximum number from a single-element list.
        """
        nums = [9000]
        expected_indices = {0}

        for _ in range(1000):
            picked_index = randomPickIndex_second_variant_398(nums)
            self.assertIn(picked_index, expected_indices)
            self.assertEqual(nums[picked_index], 9000)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
