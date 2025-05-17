from typing import List


# VARIANT: What if you're given a full matrix and you had to print out the
#          anti-diagonal order?
# SOURCE: https://youtu.be/URiyTWfIxPo?si=ka5vVIOIDWoUVH_X&t=1347
class Solution_1424_Second_Variant:
    def antidiagonal_traverse_1424(self, nums: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        for col in range(len(nums[0])):
            self.helper_1424_second_variant(nums, 0, col)

        for row in range(1, len(nums)):
            self.helper_1424_second_variant(nums, row, len(nums[0]) - 1)

    def helper_1424_second_variant(
        self, nums: List[List[int]], row: int, col: int
    ) -> None:
        while row < len(nums) and col >= 0:
            print(nums[row][col], end=" ")
            row += 1
            col -= 1

        print()


if __name__ == "__main__":
    Solution_1424_Second_Variant().antidiagonal_traverse_1424(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )
    print("-" * 100)
    Solution_1424_Second_Variant().antidiagonal_traverse_1424(
        [
            [1],
            [2],
            [3],
        ]
    )
    print("-" * 100)
    Solution_1424_Second_Variant().antidiagonal_traverse_1424(
        [
            [9, 8, 6],
            [7, 5, 3],
            [4, 2, 1],
        ]
    )
