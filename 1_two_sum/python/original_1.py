from typing import List, Tuple


# LC: https://leetcode.com/problems/two-sum/
# SOURCE: https://youtu.be/JRaZN8fOlFk?si=8DxvQkYKxYGDRfR1
class Solution_1:
    def two_sum(self, nums: List[int], target: int) -> Tuple:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        complement_to_index = {}
        for i, num in enumerate(nums):
            complement_num = target - num
            if complement_num in complement_to_index:
                return (complement_to_index[complement_num], i)

            complement_to_index[num] = i

        return ()


if __name__ == "__main__":
    assert Solution_1().two_sum([3, 4, 2, 6, 5, 1], 10) == (1, 3)
    assert Solution_1().two_sum([9, 3, 5, 8, 1, 2, 3], 17) == (0, 3)
    assert Solution_1().two_sum([2, 1, 8, 3, 4, 0, 5], 5) == (0, 3)
    assert Solution_1().two_sum([2, 1, 8, 3, 4, 0, 5], 50) == ()
    assert Solution_1().two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert Solution_1().two_sum([3, 2, 7], 9) == (1, 2)
    assert Solution_1().two_sum([3, 2, 7], 6) == ()
    assert Solution_1().two_sum([3, 2, 4], 6) == (1, 2)
    assert Solution_1().two_sum([3, 3], 6) == (0, 1)
    assert Solution_1().two_sum([], 0) == ()
    assert Solution_1().two_sum([1, 1, 1, 1, 1, 1, 1], 2) == (0, 1)
