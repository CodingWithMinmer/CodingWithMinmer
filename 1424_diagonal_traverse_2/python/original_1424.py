from collections import deque
from typing import List


# LC: https://leetcode.com/problems/diagonal-traverse-ii/
# SOURCE: https://youtu.be/URiyTWfIxPo?si=-0HC_3h4WAjtAHtl
class Solution_1424:
    def diagonal_traverse_1424(self, nums: List[List[int]]) -> List[int]:
        """
        Time Complexity: O(N)
        Space Complexity: O(√N)
        """
        result = []
        queue = deque([(0, 0)])
        while queue:
            row, col = queue.popleft()

            result.append(nums[row][col])

            if not col and row + 1 < len(nums):
                queue.append((row + 1, col))

            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))

        return result


if __name__ == "__main__":
    assert Solution_1424().diagonal_traverse_1424(
        [
            [1, 3, 6],
            [2, 5],
            [4, 7],
        ]
    ) == list(range(1, 8))
    assert Solution_1424().diagonal_traverse_1424(
        [
            [1, 2, 3, 4, 5],
            [6, 7],
            [8],
            [9, 10, 11],
            [12, 13, 14, 15, 16],
        ]
    ) == [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]
    assert Solution_1424().diagonal_traverse_1424(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    ) == [1, 4, 2, 7, 5, 3, 8, 6, 9]
