def findValleyElement(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right - left) // 2 + left

        if (mid == len(nums) - 1 or nums[mid + 1] > nums[mid]) and (
            mid == 0 or nums[mid - 1] > nums[mid]
        ):
            return mid

        if nums[mid + 1] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Unreachable


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    assert findValleyElement(nums) == 0  # Left pos infinity yields valley

    nums = [1, 2, 3, 5, 3, 4, 3, 1, 6]
    assert findValleyElement(nums) == 4

    nums = [3, 2, 3, 4, 3, 2]
    assert findValleyElement(nums) == 1

    nums = [1, 2, 3, 4, 3, 2]
    assert findValleyElement(nums) == 0

    nums = [1, 2, 3, 2, 1, 0]
    assert findValleyElement(nums) == 5  # Right pos infinity yields valley

    nums = [1, 2, 3, 2, 1, 6]
    assert findValleyElement(nums) == 4
