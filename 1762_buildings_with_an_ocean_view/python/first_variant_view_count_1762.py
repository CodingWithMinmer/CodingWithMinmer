from typing import List

# VARIANT: Return the number of buildings with an ocean view instead of their
#          indices
# SOURCE: https://youtu.be/tbkzCFlKNWU?si=nlapFdVpKq9plGBe&t=449
def findBuildings(heights: List[int]) -> List[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    count = 1
    n = len(heights)-1
    right_max = heights[n]
    for i in range(n-1, -1, -1):
        if heights[i] > right_max:
            count += 1
            right_max = heights[i]

    return count

if __name__ == "__main__":
    assert findBuildings([10, 6, 3, 3, 8, 7]) == 3
