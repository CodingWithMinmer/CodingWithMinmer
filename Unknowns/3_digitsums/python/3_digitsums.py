import heapq

class KthSmallestDigitSums:
    def compute(self, num):
        digit_sum = 0
        while num != 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def kth_smallest_digit_sums(self, nums, k):
        max_heap = []

        for num in nums:
            digit_sum = self.compute(num)
            heapq.heappush(max_heap, (-digit_sum, num))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        result = []
        while max_heap:
            _, num = heapq.heappop(max_heap)
            result.append(num)
        return result