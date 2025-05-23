from typing import List


# VARIANT: What if you had to move zeroes to the front, not the back?
# SOURCE: https://youtu.be/F6mWUALRTcE?si=m63kTod0OJeE9Izv&t=316
class Solution_283_Variant:
    def move_zeroes(self, nums: List[int]) -> None:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        swap_index = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i]:
                nums[i], nums[swap_index] = nums[swap_index], nums[i]
                swap_index -= 1

        return nums


if __name__ == "__main__":
    assert Solution_283_Variant().move_zeroes([1, 3, 12, 0, 0, 0]) == [
        0,
        0,
        0,
        1,
        3,
        12,
    ]
    assert Solution_283_Variant().move_zeroes([0, 1, 0, 3, 12]) == [0, 0, 1, 3, 12]
    assert Solution_283_Variant().move_zeroes([1, 3, 12, 0, 0, 0, 0, 0, 0]) == [
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        3,
        12,
    ]
    assert Solution_283_Variant().move_zeroes([]) == []
    assert Solution_283_Variant().move_zeroes([0]) == [0]
    assert Solution_283_Variant().move_zeroes([0, 0, 0]) == [0, 0, 0]
    assert Solution_283_Variant().move_zeroes([1, 0, 3, 0, 12]) == [0, 0, 1, 3, 12]
    assert Solution_283_Variant().move_zeroes([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert Solution_283_Variant().move_zeroes([0, 0, 3, 4, 5]) == [0, 0, 3, 4, 5]

    assert Solution_283_Variant().move_zeroes([0, 0, 54, 0, -11, 2, 0]) == [
        0,
        0,
        0,
        0,
        54,
        -11,
        2,
    ]
