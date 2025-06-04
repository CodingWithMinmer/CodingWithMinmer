# VARIANT: What if you had to print all the paths using backtracking? No DP.
def print_unique_paths(n):
    def backtrack(path, row, col):
        if row >= n or col >= n:
            return
        if row == n - 1 and col == n - 1:
            print(path)
            return

        backtrack(path + 'R', row, col + 1)
        backtrack(path + 'D', row + 1, col)

    backtrack('', 0, 0)

# VARIANT: What if you had to return all the paths? No DP.
def get_unique_paths(n):
    result = []

    def backtrack(path, row, col):
        if row >= n or col >= n:
            return
        if row == n - 1 and col == n - 1:
            result.append(path)
            return

        backtrack(path + 'R', row, col + 1)
        backtrack(path + 'D', row + 1, col)

    backtrack('', 0, 0)
    return result