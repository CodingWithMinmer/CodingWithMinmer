from heapq import heappush, heappop


class Solution:
    def findKthSmallest(self, nums: list[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heappush(max_heap, -num)
            if len(max_heap) > k:
                heappop(max_heap)
        return -max_heap[0]


if __name__ == "__main__":
    solution = Solution()
    assert solution.findKthSmallest([2, 10, 8, 3, 7, 9], 2) == 3
    assert solution.findKthSmallest([2, 10, 8, 3, 7, 9], 4) == 8
