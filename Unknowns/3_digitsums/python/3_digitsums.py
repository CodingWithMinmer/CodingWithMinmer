import heapq,unittest

class kth_smallest_digit_sums:
    def compute(self, num):
        totalSum = 0
        while num:
            totalSum+= num % 10
            num //= 10
        return totalSum

    def kth_smallest_digit_sums(self, nums, k):
        max_heap = []
        result = []
        for num in nums:
            curDigit = self.compute(num)
            heapq.heappush(max_heap,(-curDigit,num))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        for _ in range(len(max_heap)):
            result.append(heapq.heappop(max_heap)[-1])
        return result
            
    
class TestUnknownDigitSums(unittest.TestCase):


    def test_single_digits_no_math(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        s = kth_smallest_digit_sums()
        
        self.assertEqual([1], s.kth_smallest_digit_sums(nums, 1))
        self.assertEqual([2, 1], s.kth_smallest_digit_sums(nums, 2))
        self.assertEqual([3, 2, 1], s.kth_smallest_digit_sums(nums, 3))
        self.assertEqual([4, 3, 2, 1], s.kth_smallest_digit_sums(nums, 4))
        self.assertEqual([5, 4, 3, 2, 1], s.kth_smallest_digit_sums(nums, 5))

    def test_multi_digit_numbers_preserves_og_number(self):
        nums = [9, 52, 11111111, 99, 123]
        s = kth_smallest_digit_sums()
        
        self.assertEqual([123], s.kth_smallest_digit_sums(nums, 1))
        self.assertEqual([52, 123], s.kth_smallest_digit_sums(nums, 2))
        self.assertEqual([11111111, 52, 123], s.kth_smallest_digit_sums(nums, 3))
        self.assertEqual([9, 11111111, 52, 123], s.kth_smallest_digit_sums(nums, 4))
        self.assertEqual([99, 9, 11111111, 52, 123], s.kth_smallest_digit_sums(nums, 5))

        nums = [6, 36, 22222, 101, 80]

        expected = [80, 6, 101] # The test is for 80 (sum 8), 6 (sum 6), 101 (sum 2)

        self.assertEqual(expected, s.kth_smallest_digit_sums(nums, 3))



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
