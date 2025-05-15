from collections import deque


# LC: https://leetcode.com/problems/diagonal-traverse-ii/
# SOURCE: https://youtu.be/URiyTWfIxPo?si=-0HC_3h4WAjtAHtl
def diagonal_traverse_1424(nums: list[list[int]]) -> list[int]:
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
    assert diagonal_traverse_1424([[1, 3, 6], [2, 5], [4, 7]]) == list(range(1, 8))
