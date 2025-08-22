import unittest

def countMonotonicSequences(nums):
    dir = -1
    count = 0
    is_flat = False
    for i in range(1,len(nums)):
        if nums[i] > nums[i - 1]:
            if dir == 0 or dir == -1:
                count += 1
            if is_flat and dir == 1:
                is_flat = False
                count += 2
            if is_flat:
                is_flat = False
                count += 1
            dir = 1
        elif nums[i] < nums[i - 1]:
            if dir == 1 or dir == -1:
                count += 1
            if is_flat and dir == 0:
                is_flat = False
                count += 2
            if is_flat:
                is_flat = False
                count += 1
            dir = 0
        else:
            is_flat = True
    
    if is_flat:
        count += 1

    return count

class TestCountMonotonicSequences(unittest.TestCase):

    def test_unchanging_terrain(self):
        nums1 = [5, 5, 5, 5, 5]
        self.assertEqual(countMonotonicSequences(nums1), 1)

        nums1 = [1000]
        self.assertEqual(countMonotonicSequences(nums1), 0)

    def test_strictly_increasing(self):
        nums1 = [1, 3, 5, 10]
        self.assertEqual(countMonotonicSequences(nums1), 1)

        nums1 = [1, 9]
        self.assertEqual(countMonotonicSequences(nums1), 1)

        nums1 = [10, 16, 20, 25, 50, 69, 420]
        self.assertEqual(countMonotonicSequences(nums1), 1)

        nums1 = [0, 9]
        self.assertEqual(countMonotonicSequences(nums1), 1)

    def test_strictly_decreasing(self):
        nums1 = [10, 5, 3, 1]
        self.assertEqual(countMonotonicSequences(nums1), 1)

        nums1 = [9, 4, 3, 2, 1]
        self.assertEqual(countMonotonicSequences(nums1), 1)

        nums1 = [100, 1]
        self.assertEqual(countMonotonicSequences(nums1), 1)

    def test_unchanging_strictly_increasing(self):
        nums1 = [6, 6, 6, 9, 10, 11, 12]  # Unchanging to Strictly increasing
        self.assertEqual(countMonotonicSequences(nums1), 2)

        nums1 = [10, 11, 12, 12, 12, 12]  # Strictly increasing to Unchanging
        self.assertEqual(countMonotonicSequences(nums1), 2)

    def test_unchanging_strictly_decreasing(self):
        nums1 = [6, 6, 6, 5, 4, 3, 2, 1]  # Unchanging to Strictly decreasing
        self.assertEqual(countMonotonicSequences(nums1), 2)

        nums1 = [5, 4, 3, 2, 2, 2, 2, 2]  # Strictly decreasing to Unchanging
        self.assertEqual(countMonotonicSequences(nums1), 2)

    def test_only_strictly_increasing_decreasing(self):
        nums1 = [4, 5, 6, 5, 4, 5, 6, 7, 8, 3, 1, 10]
        self.assertEqual(countMonotonicSequences(nums1), 5)

        nums1 = [10, 9, 5, 7, 10, 2, 10, 2, 10, 15, 16]
        self.assertEqual(countMonotonicSequences(nums1), 6)

        nums1 = [1, 2, 1, 2, 1, 2, 1, 2]
        self.assertEqual(countMonotonicSequences(nums1), 7)

    def test_hybrid(self):
        # Unchanging to Dec to Unchanging to Increasing to Unchanging
        nums1 = [6, 6, 6, 5, 4, 3, 2, 1, 1, 22, 22]
        self.assertEqual(countMonotonicSequences(nums1), 5)

        nums1 = [1, 2, 3, 4, 4, 4, 3, 2, 1]
        self.assertEqual(countMonotonicSequences(nums1), 3)

        nums1 = [1, 1, 2, 2, 1, 1, 3, 3, 5, 5, 1, 5, 1, 5, 5, 5, 1]
        self.assertEqual(countMonotonicSequences(nums1), 15)

        nums1 = [10, 9, 8, 8, 8, 8, 6, 4, 4, 4, 4, 4, 4, 1, 2, 1, 2, 2]
        self.assertEqual(countMonotonicSequences(nums1), 9)

        nums1 = [1, 2, 3, 2, 1, 1]
        self.assertEqual(countMonotonicSequences(nums1), 3)
        
if __name__ == '__main__':
    unittest.main()

