from collections import deque


# VARIANT: What if you had to return a list of the anti-diagonal traversal?
# SOURCE: https://youtu.be/URiyTWfIxPo?si=0sTLYh7CVuD4CJra&t=691
def antidiagonal_traverse_1424_first_variant(nums: list[list[int]]) -> list[list[int]]:
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
    assert antidiagonal_traverse_1424_first_variant([[1, 3, 6], [2, 5], [4, 7]]) == [
        [1],
        [3, 2],
        [6, 5, 4],
        [7],
    ]
