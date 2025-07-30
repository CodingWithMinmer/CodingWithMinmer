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


if __name__ == "__main__":
    # Valid cases
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    assert solution.countElements(nums, target) == 2
    target = 6
    assert solution.countElements(nums, target) == 0
    nums = [2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12]
    target = 9
    assert solution.countElements(nums, target) == 5
    target = 2
    assert solution.countElements(nums, target) == 2
    target = 3
    assert solution.countElements(nums, target) == 3
    target = 10
    assert solution.countElements(nums, target) == 1
    target = 12
    assert solution.countElements(nums, target) == 2
    nums = [1, 2, 3, 4, 5]
    target = 1
    assert solution.countElements(nums, target) == 1
    target = 2
    assert solution.countElements(nums, target) == 1
    target = 3
    assert solution.countElements(nums, target) == 1
    target = 4
    assert solution.countElements(nums, target) == 1
    target = 5
    assert solution.countElements(nums, target) == 1
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    target = 1
    assert solution.countElements(nums, target) == 9
    nums = [-3, -2, -1, 0, 1, 2, 3]
    target = -3
    assert solution.countElements(nums, target) == 1
    target = -2
    assert solution.countElements(nums, target) == 1
    target = -1
    assert solution.countElements(nums, target) == 1
    target = 0
    assert solution.countElements(nums, target) == 1
    target = 1
    assert solution.countElements(nums, target) == 1
    target = 2
    assert solution.countElements(nums, target) == 1
    target = 3
    assert solution.countElements(nums, target) == 1

    # Target not found cases
    nums = [5, 7, 7, 8, 8, 10]
    target = 9  # Not Found
    assert solution.countElements(nums, target) == 0
    target = 6  # Not Found
    assert solution.countElements(nums, target) == 0
    target = -5  # Too low
    assert solution.countElements(nums, target) == 0
    target = 60  # Too high
    assert solution.countElements(nums, target) == 0

    nums = []  # Empty list
    target = -5  # Empty vector
    assert solution.countElements(nums, target) == 0
    target = 50  # Empty vector
    assert solution.countElements(nums, target) == 0

    nums = [2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12]
    target = 1  # Too low
    assert solution.countElements(nums, target) == 0
    target = 4  # Not found
    assert solution.countElements(nums, target) == 0
    target = 15  # Too high
    assert solution.countElements(nums, target) == 0

    nums = [1, 2, 3, 4, 5]
    target = 0
    assert solution.countElements(nums, target) == 0
    target = 6
    assert solution.countElements(nums, target) == 0
