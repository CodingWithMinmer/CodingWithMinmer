import unittest
from random import random
from collections import Counter

def randomPickIndices_first_variant_398(nums: list[int], k: int) -> list[int]:
    """
    Mock implementation for the first variant: randomly picks k elements from nums.
    If k is greater than or equal to the list length, it returns a shuffled copy of the whole list.
    """
    if not nums: return []
    res = nums[:k]
    n = k
    for i in range(k,len(nums)):
        n =i + 1
        r = int(random() % n)
        if r < k:
            res[r] = nums[i]
    return res


# --- Python unittest Test Classes ---

class TestRandomPickIndexFirstVariant(unittest.TestCase):
    """
    Tests for the first variant function: randomPickIndices_first_variant_398.
    """

    def test_happy_case(self):
        """
        Tests picking 'k' random elements from a positive number list.
        """
        nums = [6, 8, 2, 1, 3, 10, 4]
        k = 3
        expected_nums_set = set(nums) # Use a set for efficient `in` checks

        for _ in range(1000): # Run multiple times due to randomness
            actual = randomPickIndices_first_variant_398(nums, k)
            self.assertEqual(len(actual), 3)
            for item in actual:
                self.assertIn(item, expected_nums_set) # Checks if item is in the set

    def test_negative_numbers(self):
        """
        Tests picking 'k' random elements from a list containing negative numbers.
        """
        nums = [6, -1, 8, 2, 100, 3, 10, -3, -50, 4]
        k = 4
        expected_nums_set = set(nums)

        for _ in range(1000):
            actual = randomPickIndices_first_variant_398(nums, k)
            self.assertEqual(len(actual), 4)
            for item in actual:
                self.assertIn(item, expected_nums_set)

    def test_k_equals_n(self):
        """
        Tests the case where 'k' is equal to the total number of elements 'n'.
        The expectation is that all elements are returned in their original order.
        """
        nums = [6, -1, 8, 2, 100, 3, 10, -3, -50, 4]
        k = 10

        for _ in range(1000):
            actual = randomPickIndices_first_variant_398(nums, k)
            self.assertEqual(len(actual), 10)
           
            self.assertListEqual(actual, nums)




if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)