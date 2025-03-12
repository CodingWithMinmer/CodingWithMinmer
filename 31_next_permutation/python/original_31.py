class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        valley = None
        for i in range(len(nums) - 1, 0, -1):
            # Iterate from end
            if nums[i - 1] < nums[i]:
                valley = i - 1
                break

        if valley is None:
            nums.reverse()
            return

        next_higher = len(nums) - 1
        while nums[next_higher] <= nums[valley]:
            next_higher -= 1

        nums[valley], nums[next_higher] = nums[next_higher], nums[valley]

        left = valley + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
