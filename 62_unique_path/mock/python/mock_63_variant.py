# VARIANT: What if you had to return all the paths but there could be obstacles in the matrix?
def get_unique_paths_with_obstacles(grid):
    result = []
    n = len(grid)

    def backtrack(path, row, col):
        if row >= n or col >= n or grid[row][col] == 1:
            return
        if row == n - 1 and col == n - 1:
            result.append(path)

        backtrack(path + 'R', row, col + 1)
        backtrack(path + 'D', row + 1, col)

    backtrack('', 0, 0)
    return result