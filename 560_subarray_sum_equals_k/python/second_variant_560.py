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
