def findPeakElement_python(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right - left) // 2 + left

        if (mid == len(nums) - 1 or nums[mid + 1] < nums[mid]) and (
            mid == 0 or nums[mid - 1] < nums[mid]
        ):
            return mid

        if nums[mid + 1] > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Unreachable
