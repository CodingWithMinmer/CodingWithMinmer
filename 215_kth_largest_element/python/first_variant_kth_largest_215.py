from heapq import heappop, heappush


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


if __name__ == "__main__":
    solution = Solution()
    # Distinct elements in nums
    nums = [1, 2, 3, 4, 5]
    k = 0
    assert solution.findKthPluseOneLargest(nums, k) == 5
    k = 1
    assert solution.findKthPluseOneLargest(nums, k) == 4
    k = 2
    assert solution.findKthPluseOneLargest(nums, k) == 3
    k = 3
    assert solution.findKthPluseOneLargest(nums, k) == 2
    k = 4
    assert solution.findKthPluseOneLargest(nums, k) == 1

    nums = [1]
    k = 0
    assert solution.findKthPluseOneLargest(nums, k) == 1

    # Out of range indices
    nums = [1, 2, 3, 4, 5]
    try:
        solution.findKthPluseOneLargest(nums, 5)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass
    try:
        solution.findKthPluseOneLargest(nums, 50)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass

    nums = [1]
    k = 1
    try:
        solution.findKthPluseOneLargest(nums, k)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass

    # Edge Case: Empty list
    nums = []
    k = 0
    try:
        solution.findKthPluseOneLargest(nums, k)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass

    k = 1
    try:
        solution.findKthPluseOneLargest(nums, k)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass

    k = 2
    try:
        solution.findKthPluseOneLargest(nums, k)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass
