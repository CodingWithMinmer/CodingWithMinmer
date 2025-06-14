from typing import List

class Solution827:
    def __init__(self):
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def borders_land(self, grid, row, col):
        for r_offset, c_offset in self.directions:
            new_row, new_col = row + r_offset, col + c_offset
            if new_row < 0 or new_row >= len(grid):
                continue
            if new_col < 0 or new_col >= len(grid[0]):
                continue
            if grid[new_row][new_col] == 0:
                continue

            return True
        return False

    def create_island(self, grid, visited, row, col):
        visited[row][col] = True
        size = 1
        for r_offset, c_offset in self.directions:
            new_row, new_col = row + r_offset, col + c_offset
            if new_row < 0 or new_row >= len(grid):
                continue
            if new_col < 0 or new_col >= len(grid[0]):
                continue
            if visited[new_row][new_col]:
                continue
            if self.borders_land(grid, new_row, new_col):
                continue
            size += self.create_island(grid, visited, new_row, new_col)
        return size
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        largest = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    continue
                if visited[row][col]:
                    continue
                if self.borders_land(grid, row, col):
                    continue
                largest = max(largest, self.create_island(grid, visited, row, col))
        
        return largest