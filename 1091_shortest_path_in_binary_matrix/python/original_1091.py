from collections import deque


# LC: https://leetcode.com/problems/shortest-path-in-binary-matrix/
# SOURCE: https://youtu.be/kqwrHrxOpl0?si=U28i-ukzz6ojoAzq
def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    """
    Time Complexity: O(N x M)
    Space Complexity: O(N)
    """
    if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
        return -1

    directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
    grid[0][0] = 1
    queue = deque([[0, 0, 1]])  # [row, column, steps]
    while queue:
        row, col, steps = queue.pop()

        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return steps

        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if (
                new_row < 0
                or new_row >= len(grid)
                or new_col < 0
                or new_col >= len(grid[0])
                or grid[new_row][new_col] == 1
            ):
                continue

            grid[new_row][new_col] = 1
            queue.append([new_row, new_col, steps + 1])

    return -1  # unreachable


if __name__ == "__main__":
    assert (
        shortest_path_binary_matrix(
            [
                [0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
            ]
        )
        == 5
    )
    assert (
        shortest_path_binary_matrix(
            [
                [1, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
            ]
        )
        == -1
    )
    assert (
        shortest_path_binary_matrix(
            [
                [0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ]
        )
        == -1
    )
    assert (
        shortest_path_binary_matrix(
            [
                [0, 0, 0],
                [1, 1, 0],
                [1, 1, 0],
            ]
        )
        == 4
    )
