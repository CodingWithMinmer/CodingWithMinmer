class Solution:
    def subarraySumExistsPositiveNums(self, nums: list[int], k: int) -> bool:
        left, right = 0, 0
        window_sum = 0
        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum > k:
                window_sum -= nums[left]
                left += 1

            if window_sum == k:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 2)
    assert solution.subarraySumExistsPositiveNums([1, 2, 3], 3)

    # SubarraySum_SecondVariant True
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 2) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3], 3) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 1, 1, 1], 5) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 1, 1, 1], 9) == True
    assert solution.subarraySumExistsPositiveNums([5], 5) == True
    assert solution.subarraySumExistsPositiveNums([5], 10) == False
    assert solution.subarraySumExistsPositiveNums([23, 5, 4, 7, 2, 11], 20) == True
    assert solution.subarraySumExistsPositiveNums([1, 3, 5, 23, 2], 8) == True
    assert solution.subarraySumExistsPositiveNums([4, 2, 5, 2, 6, 1], 9) == True
    assert solution.subarraySumExistsPositiveNums([1, 1, 1, 1, 1, 1], 1) == True
    assert solution.subarraySumExistsPositiveNums([1], 1) == True

    # SubarraySum_SecondVariant False
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 4) == False
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 4, 5, 6, 7], 100) == False
    assert solution.subarraySumExistsPositiveNums([100, 101, 102, 103], 2) == False
    assert solution.subarraySumExistsPositiveNums([1, 3, 5, 23, 2], 7) == False
