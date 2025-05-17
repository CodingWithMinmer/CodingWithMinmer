from typing import List


# VARIANT: The buildings are on an island i.e. the ocean is both to the left
#          and right sides of the buildings.
# SOURCE: https://youtu.be/tbkzCFlKNWU?si=vCKcgiQfzdVyVsfE&t=626
class Solution_1762_Second_Variant:
    def find_buildings_both_sides_variant(self, heights: List[int]) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n), in the case when all the buildings have a view
        """

        n = len(heights) - 1
        left_view = [0]
        if not n:
            return left_view

        left, right = 0, n
        left_max, right_max = heights[left], heights[right]
        left_view, right_view = [left], [right]
        while left < right:
            if left_max < right_max:
                left += 1
                if heights[left] > left_max:
                    left_view.append(left)
                    left_max = heights[left]
            else:
                right -= 1
                if heights[right] > right_max and left < right:
                    right_view.append(right)
                    right_max = heights[right]

        right_view.reverse()
        return left_view + right_view


if __name__ == "__main__":
    assert Solution_1762_Second_Variant().find_buildings_both_sides_variant(
        [4, 2, 3, 1]
    ) == [0, 2, 3]
    assert Solution_1762_Second_Variant().find_buildings_both_sides_variant(
        [10, 6, 3, 3, 8, 7]
    ) == [0, 4, 5]
    assert Solution_1762_Second_Variant().find_buildings_both_sides_variant([3]) == [0]
    assert Solution_1762_Second_Variant().find_buildings_both_sides_variant(
        [2, 5, 3, 10, 9, 8]
    ) == [0, 1, 3, 4, 5]
