from typing import List

class Solution827:
    def __init__(self):
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def label_island(self, grid, id, row, col):
        grid[row][col] = id
        size = 1
        for r_offset, c_offset in self.directions:
            new_row, new_col = row + r_offset, col + c_offset
            if new_row < 0 or new_row >= len(grid):
                continue
            if new_col < 0 or new_col >= len(grid[0]):
                continue
            if grid[new_row][new_col] != 1:
                continue

            size += self.label_island(grid, id, new_row, new_col)

        return size

    def create_island(self, grid, id_to_island_size, row, col):
        visited = set()
        size = 1
        for r_offset, c_offset in self.directions:
            new_row, new_col = row + r_offset, col + c_offset
            if new_row < 0 or new_row >= len(grid):
                continue
            if new_col < 0 or new_col >= len(grid[0]):
                continue
            if grid[new_row][new_col] == 0:
                continue
            if grid[new_row][new_col] in visited:
                continue

            id = grid[new_row][new_col]
            size += id_to_island_size[id]
            visited.add(id)
        
        return size

    def largestIsland(self, grid: List[List[int]]) -> int:
        id_to_island_size = {}
        largest = 0
        id = 2
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    size = self.label_island(grid, id, row, col)
                    largest = max(largest, size)
                    id_to_island_size[id] = size
                    id += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    size = self.create_island(grid, id_to_island_size, row, col)
                    largest = max(largest, size)

        return largest