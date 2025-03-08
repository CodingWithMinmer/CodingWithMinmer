class Solution:
    def countElements(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if target > nums[-1] or target < nums[0]:
            return 0

        def upper(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        def lower(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        first = lower(nums, target)
        if nums[first] != target:
            return 0
        last = upper(nums, target)
        return last - first + 1
