import heapq,unittest

class KthSmallestDigitSumsFollowup:
    def compute(self, num):
        digit_sum = 0
        while num != 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum
    
    def kth_smallest_digit_sums(self, nums, k):
        max_heap = []

        for index, num in enumerate(nums):
            digit_sum = self.compute(num)
            heapq.heappush(max_heap,(-digit_sum,-index,num))

            if len(max_heap)>k:
                heapq.heappop(max_heap)

        result = []
        while max_heap:
            _, _, num = heapq.heappop(max_heap)
            result.append(num)
        result.reverse()
        return result
    
class TestUnknownDigitSums(unittest.TestCase):
    # # --- Tests for KthSmallestDigitSumsFollowup (Tiebreaker) ---

    def test_tiebreaker(self):
        nums = [9, 222, 402, 99, 123]
        s = KthSmallestDigitSumsFollowup()

        self.assertEqual([222], s.kth_smallest_digit_sums(nums, 1))
        self.assertEqual([222, 402], s.kth_smallest_digit_sums(nums, 2))
        self.assertEqual([222, 402, 123], s.kth_smallest_digit_sums(nums, 3))
        self.assertEqual([222, 402, 123, 9], s.kth_smallest_digit_sums(nums, 4)) # 6,6,6,9
        self.assertEqual([222, 402, 123, 9, 99], s.kth_smallest_digit_sums(nums, 5))

        nums = [111, 84, 21, 12, 3, 56, 2001, 10000]
        
        expected = [10000, 111, 21]
        self.assertEqual(expected, s.kth_smallest_digit_sums(nums, 3))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
