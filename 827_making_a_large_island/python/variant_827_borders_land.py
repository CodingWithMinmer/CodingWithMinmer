from typing import List
import pytest


class Solution827Variant:
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
    



class TestMakingLargeIslandVariant:

    def setup_method(self):
        self.s = Solution827Variant()

    def test_no_land_makes_largest_of_matrix(self):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        assert self.s.largestIsland(grid) == 20

        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        assert self.s.largestIsland(grid) == 16

        grid = [
            [0],
            [0],
            [0],
            [0],
            [0]
        ]
        assert self.s.largestIsland(grid) == 5

        grid = [[0]]
        assert self.s.largestIsland(grid) == 1

    def test_all_land_makes_zero_area_island(self):
        grid = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        assert self.s.largestIsland(grid) == 0

        grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        assert self.s.largestIsland(grid) == 0

        grid = [
            [1],
            [1],
            [1],
            [1],
            [1]
        ]
        assert self.s.largestIsland(grid) == 0

        grid = [[1]]
        assert self.s.largestIsland(grid) == 0

    def test_hybrid_land_water_still_cannot_create_island(self):
        grid = [
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
        ]
        assert self.s.largestIsland(grid) == 0

        grid = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]
        assert self.s.largestIsland(grid) == 0

        grid = [
            [1],
            [0],
            [1],
            [0],
            [1]
        ]
        assert self.s.largestIsland(grid) == 0

        grid = [
            [0, 0, 0, 1, 1],
            [1, 1, 0, 1, 1],
            [0, 1, 0, 1, 1],
            [0, 1, 0, 0, 0],
        ]
        assert self.s.largestIsland(grid) == 0

    def test_hybrid_creates_island(self):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1],
        ]
        assert self.s.largestIsland(grid) == 9

        grid = [
            [0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
        ]
        assert self.s.largestIsland(grid) == 10

        grid = [
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ]
        assert self.s.largestIsland(grid) == 8

        grid = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        assert self.s.largestIsland(grid) == 10

        grid = [
            [0],
            [0],
            [0],
            [1],
            [1]
        ]
        assert self.s.largestIsland(grid) == 2