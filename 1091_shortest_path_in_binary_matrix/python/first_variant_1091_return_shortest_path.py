from collections import deque


# VARIANT: What happens if you have to return the path of a shortest path?
# SOURCE: https://youtu.be/kqwrHrxOpl0?si=HRWt35IkzIedvBYW&t=1100
def shortest_path_binary_matrix(grid: list[list[int]]) -> list[list[int]]:
    """
    Time Complexity: O((N x M) x N)
    Space Complexity: O(N ^ 2)
    """
    if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
        return []

    directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
    grid[0][0] = 1
    queue = deque([[0, 0, [[0, 0]]]])  # [row, column, path]
    while queue:
        row, col, path = queue.pop()

        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return path

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

            queue.append([new_row, new_col, path + [[new_row, new_col]]])

    return []  # unreachable


if __name__ == "__main__":
    assert shortest_path_binary_matrix(
        [
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
        ]
    ) == [[0, 0], [1, 1], [2, 1], [3, 2], [3, 3]]
    assert (
        shortest_path_binary_matrix(
            [
                [1, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
            ]
        )
        == []
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
        == []
    )
    assert shortest_path_binary_matrix(
        [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0],
        ]
    ) == [[0, 0], [0, 1], [1, 2], [2, 2]]
