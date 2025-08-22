from collections import deque
from typing import List


# VARIANT: What if you had to return a list of the anti-diagonal traversal?
# SOURCE: https://youtu.be/URiyTWfIxPo?si=0sTLYh7CVuD4CJra&t=691
class Solution_1424_First_Variant:
    def antidiagonal_traverse_1424(self, nums: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity: O(N)
        Space Complexity: O(√N)
        """
        result = []
        queue = deque([(0, 0)])
        while queue:
            size = len(queue)
            curr_level = []

            for _ in range(len(queue)):
                row, col = queue.popleft()

                curr_level.append(nums[row][col])

                if col + 1 < len(nums[row]):
                    queue.append((row, col + 1))

                if not col and row + 1 < len(nums):
                    queue.append((row + 1, col))

            result.append(curr_level)

        return result


if __name__ == "__main__":
    assert Solution_1424_First_Variant().antidiagonal_traverse_1424(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    ) == [
        [1],
        [2, 4],
        [3, 5, 7],
        [6, 8],
        [9],
    ]
    assert Solution_1424_First_Variant().antidiagonal_traverse_1424(
        [
            [1, 3, 6],
            [2, 5],
            [4, 7],
        ]
    ) == [
        [1],
        [3, 2],
        [6, 5, 4],
        [7],
    ]
    assert Solution_1424_First_Variant().antidiagonal_traverse_1424(
        [
            [1, 2, 3, 4, 5],
            [6, 7],
            [8],
            [9, 10, 11],
            [12, 13, 14, 15, 16],
        ]
    ) == [
        [1],
        [2, 6],
        [3, 7, 8],
        [4, 9],
        [5, 10, 12],
        [11, 13],
        [14],
        [15],
        [16],
    ]
