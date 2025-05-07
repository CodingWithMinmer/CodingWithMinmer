from collections import deque


# VARIANT: What if you had to return a single path? Note it's not necessarily the shortest.
# SOURCE: https://youtu.be/kqwrHrxOpl0?si=HNeDNSFbfjwp0DDH&t=1543
def dfs(grid: list[list[int]], path: list[list[int]], row: int, col: int) -> bool:
    grid[row][col] = 1
    path.append([row, col])

    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return True

    directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
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

        if dfs(grid, path, new_row, new_col):
            return True

    path.pop()
    return False


def dfs_path_binary_matrix(grid: list[list[int]]) -> list[list[int]]:
    """
    Time Complexity: O((N x M) x N)
    Space Complexity: O(N ^ 2)
    """
    if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
        return []

    path = []
    dfs(grid, path, 0, 0)
    return path


if __name__ == "__main__":
    assert dfs_path_binary_matrix(
        [
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
        ]
    ) == [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [3, 2], [3, 3]]
    assert (
        dfs_path_binary_matrix(
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
        dfs_path_binary_matrix(
            [
                [0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ]
        )
        == []
    )
    assert dfs_path_binary_matrix(
        [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0],
        ]
    ) == [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
