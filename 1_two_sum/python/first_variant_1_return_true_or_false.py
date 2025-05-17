from typing import List


# VARIANT: What if you had to return T/F if you find at least one pair of
#          numbers that add up to the target?
# SOURCE: https://youtu.be/JRaZN8fOlFk?si=F7Q9bAJGyf3NVw2I&t=707
class Solution_1_First_Variant:
    def two_sum_first_variant(self, nums: List[int], target: int) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        complements = set()
        for i, num in enumerate(nums):
            complement_num = target - num
            if complement_num in complements:
                return True

            complements.add(num)

        return False


if __name__ == "__main__":
    assert (
        Solution_1_First_Variant().two_sum_first_variant([3, 4, 2, 6, 5, 1], 10) == True
    )
    assert (
        Solution_1_First_Variant().two_sum_first_variant([9, 3, 5, 8, 1, 2, 3], 17)
        == True
    )
    assert (
        Solution_1_First_Variant().two_sum_first_variant([2, 1, 8, 3, 4, 0, 5], 5)
        == True
    )
    assert (
        Solution_1_First_Variant().two_sum_first_variant([2, 1, 8, 3, 4, 0, 5], 50)
        == False
    )
    assert Solution_1_First_Variant().two_sum_first_variant([2, 7, 11, 15], 9) == True
    assert Solution_1_First_Variant().two_sum_first_variant([3, 2, 7], 9) == True
    assert Solution_1_First_Variant().two_sum_first_variant([3, 2, 7], 6) == False
    assert Solution_1_First_Variant().two_sum_first_variant([3, 2, 4], 6) == True
    assert Solution_1_First_Variant().two_sum_first_variant([3, 3], 6) == True
    assert Solution_1_First_Variant().two_sum_first_variant([], 0) == False
    assert (
        Solution_1_First_Variant().two_sum_first_variant([1, 1, 1, 1, 1, 1, 1], 2)
        == True
    )
