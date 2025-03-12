class Solution:
    def previousPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        peak = None
        for i in range(len(nums) - 1, 0, -1):
            # Iterate from end
            if nums[i - 1] > nums[i]:
                peak = i - 1
                break

        if peak is None:
            nums.reverse()
            return

        next_lower = len(nums) - 1
        while nums[next_lower] >= nums[peak]:
            next_lower -= 1

        nums[peak], nums[next_lower] = nums[next_lower], nums[peak]

        left = peak + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    solution = Solution()
    nums = [9, 4, 8, 3, 5, 5, 8, 9]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 5, 3]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 3, 5]
