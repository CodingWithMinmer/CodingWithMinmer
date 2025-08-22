from typing import List


def longestOnes_1004_python(nums: List[int], k: int) -> int:
    max_ = 0
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1

        while k < 0:
            if nums[left] == 0:
                k += 1
            left += 1

        max_ = max(max_, right - left + 1)
    return max_
