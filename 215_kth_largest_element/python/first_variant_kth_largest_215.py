from heapq import heappush, heappop


class Solution:
    def findKthPluseOneLargest(self, nums: list[int], k: int) -> int:
        if k + 1 > len(nums):
            return 0
        k = k + 1
        min_heap = []
        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)
        return min_heap[0]
