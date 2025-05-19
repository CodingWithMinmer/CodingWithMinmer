class Solution:
    def has_valid_subarray(self, nums: list[int], target: int) -> bool:
        left = 0
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]

            while sum > target:
                sum -= nums[left]
                left += 1

            if sum == target:
                return True

        return False
    
if __name__ == "__main__":
    solution = Solution()
    assert solution.has_valid_subarray([1, 1, 1], 2)
    assert solution.has_valid_subarray([1, 2, 3], 3)
    # SubarraySum_SecondVariant True
    assert solution.has_valid_subarray([1, 1, 1], 2) == True
    assert solution.has_valid_subarray([1, 2, 3], 3) == True
    assert solution.has_valid_subarray([1, 2, 3, 1, 1, 1], 5) == True
    assert solution.has_valid_subarray([1, 2, 3, 1, 1, 1], 9) == True
    assert solution.has_valid_subarray([5], 5) == True
    assert solution.has_valid_subarray([5], 10) == False
    assert solution.has_valid_subarray([23, 5, 4, 7, 2, 11], 20) == True
    assert solution.has_valid_subarray([1, 3, 5, 23, 2], 8) == True
    assert solution.has_valid_subarray([4, 2, 5, 2, 6, 1], 9) == True
    assert solution.has_valid_subarray([1, 1, 1, 1, 1, 1], 1) == True
    assert solution.has_valid_subarray([1], 1) == True

    # SubarraySum_SecondVariant False
    assert solution.has_valid_subarray([1, 1, 1], 4) == False
    assert solution.has_valid_subarray([1, 2, 3, 4, 5, 6, 7], 100) == False
    assert solution.has_valid_subarray([100, 101, 102, 103], 2) == False
    assert solution.has_valid_subarray([1, 3, 5, 23, 2], 7) == False
