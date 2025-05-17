from typing import List


# VARIANT: Return the number of buildings with an ocean view instead of their
#          indices
# SOURCE: https://youtu.be/tbkzCFlKNWU?si=nlapFdFirst_VpKq9plGBe&t=449
class Solution_1762_First_Variant:
    def find_buildings_view_count(self, heights: List[int]) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        count = 1
        n = len(heights) - 1
        right_max = heights[n]
        for i in range(n - 1, -1, -1):
            if heights[i] > right_max:
                count += 1
                right_max = heights[i]

        return count


if __name__ == "__main__":
    assert Solution_1762_First_Variant().find_buildings_view_count([4, 2, 3, 1]) == 3
    assert (
        Solution_1762_First_Variant().find_buildings_view_count([10, 6, 3, 3, 8, 7])
        == 3
    )
    assert Solution_1762_First_Variant().find_buildings_view_count([3]) == 1
    assert (
        Solution_1762_First_Variant().find_buildings_view_count([2, 5, 3, 10, 9, 8])
        == 3
    )
