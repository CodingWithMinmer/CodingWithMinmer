from typing import List
import pytest


class Solution827Variant:
    def __init__(self):
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


    def border_island(self,grid,r,c):
        for dr,dc in self.directions:
            nr,nc = dr+r,dc+c
            if -1 < nr < self.m and -1 < nc < self.n  and grid[nr][nc] == 1:
                return True
        return False
    
    def islandCounter(self,grid,r,c):
        self.visited.add((r,c))
        size = 1
        for dr,dc in self.directions:
            nr,nc = dr+r,dc+c
            if -1 < nr < self.m and -1 < nc < self.n and not (nr,nc) in self.visited and not self.border_island(grid,nr,nc) and grid[nr][nc] == 0: 
                size += self.islandCounter(grid,nr,nc)
        return size


    def largestIsland(self, grid: List[List[int]]) -> int:
        self.m,self.n = len(grid),len(grid[0])
        self.visited = set()
        largest = 0
        for i in range(self.m):
            for j in range(self.n):
                if -1 < i < self.m and -1 < j < self.n and grid[i][j] == 0 and not (i,j) in self.visited  and not self.border_island(grid,i,j):
                    largest = max(largest,self.islandCounter(grid,i,j))
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