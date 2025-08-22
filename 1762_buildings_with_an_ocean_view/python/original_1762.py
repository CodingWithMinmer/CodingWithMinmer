from typing import List


# LC: https://leetcode.com/problems/buildings-with-an-ocean-view/
# SOURCE: https://youtu.be/tbkzCFlKNWU?si=FgL2YWvfTnaIpnrK
class Solution_1762:
    def find_buildings(self, heights: List[int]) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(heights) - 1
        right_view = [n]
        right_max = heights[n]
        for i in range(n - 1, -1, -1):
            if heights[i] > right_max:
                right_view.append(i)
                right_max = heights[i]

        right_view.reverse()
        return right_view


if __name__ == "__main__":
    assert Solution_1762().find_buildings([4, 2, 3, 1]) == [0, 2, 3]
    assert Solution_1762().find_buildings([10, 6, 3, 3, 8, 7]) == [0, 4, 5]
    assert Solution_1762().find_buildings([3]) == [0]
    assert Solution_1762().find_buildings([2, 5, 3, 10, 9, 8]) == [3, 4, 5]
