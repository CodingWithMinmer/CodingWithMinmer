from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_inc = True
        is_dec = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                is_dec = False
            if nums[i] < nums[i - 1]:
                is_inc = False

            if not is_inc and not is_dec:
                return False
        return True

