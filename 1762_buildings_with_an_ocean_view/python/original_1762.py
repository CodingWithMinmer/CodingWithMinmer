from typing import List

# LC: https://leetcode.com/problems/buildings-with-an-ocean-view/
# SOURCE: https://youtu.be/tbkzCFlKNWU?si=FgL2YWvfTnaIpnrK
def find_buildings(heights: List[int]) -> List[int]:
    """
        Time Complexity: O(n)
        Space Complexity: O(1)
    """

    n = len(heights)-1
    right_view = [n]
    right_max = heights[n]
    for i in range(n-1, -1, -1):
        if heights[i] > right_max:
            right_view.append(i)
            right_max = heights[i]

    right_view.reverse()
    return right_view

if __name__ == "__main__":
    assert findBuildings([10, 6, 3, 3, 8, 7]) == [0, 4, 5]
