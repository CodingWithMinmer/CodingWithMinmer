from typing import List


# LC: https://leetcode.com/problems/move-zeroes/
# SOURCE: https://youtu.be/F6mWUALRTcE?si=_upBJt-U77HccNLt
class Solution_283:
    def move_zeroes(self, nums: List[int]) -> None:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        swap_index = 0
        for i in range((len(nums))):
            if nums[i]:
                nums[i], nums[swap_index] = nums[swap_index], nums[i]
                swap_index += 1

        return nums


if __name__ == "__main__":
    assert Solution_283().move_zeroes([1, 3, 12, 0, 0, 0]) == [
        1,
        3,
        12,
        0,
        0,
        0,
    ]
    assert Solution_283().move_zeroes([0, 1, 0, 3, 12]) == [
        1,
        3,
        12,
        0,
        0,
    ]
    assert Solution_283().move_zeroes([0, 0, 0, 0, 0, 0, 1, 3, 12]) == [
        1,
        3,
        12,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
    assert Solution_283().move_zeroes([]) == []
    assert Solution_283().move_zeroes([0]) == [0]
    assert Solution_283().move_zeroes([0, 0, 0]) == [0, 0, 0]
    assert Solution_283().move_zeroes([1, 0, 3, 0, 12]) == [1, 3, 12, 0, 0]
    assert Solution_283().move_zeroes([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert Solution_283().move_zeroes([0, 0, 3, 4, 5]) == [
        3,
        4,
        5,
        0,
        0,
    ]

    assert Solution_283().move_zeroes([0, 0, 54, 0, -11, 2, 0]) == [
        54,
        -11,
        2,
        0,
        0,
        0,
        0,
    ]
