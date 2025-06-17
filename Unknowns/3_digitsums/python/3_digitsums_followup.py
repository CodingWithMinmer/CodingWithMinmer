import heapq

# FOLLOW-UP: What if the order in the output array mattered? It should be sorted in ascending order
# In the case of a tiebreak (of equal digit sums), prioritize the number with the lower index
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
            heapq.heappush(max_heap, (-digit_sum, -index, num))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        result = []
        while max_heap:
            _, _, num = heapq.heappop(max_heap)
            result.append(num)
        result.reverse()
        return result