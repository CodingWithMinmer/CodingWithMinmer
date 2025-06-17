#pragma once

#include <vector>
#include <unordered_set>

// VARIANT: What if you had to create an island that doesn't touch any other existing islands?
class Solution827Variant {
    std::vector<std::vector<int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    bool borders_land(std::vector<std::vector<int>>& grid,
                int row,
                int col) {
        for (auto& direction : directions) {
            int new_row = row + direction[0];
            int new_col = col + direction[1];
            if (new_row < 0 || new_row >= grid.size())
                continue;
            if (new_col < 0 || new_col >= grid[0].size())
                continue;
            if (grid[new_row][new_col] == 0)
                continue;

            return true; // must be a 1 that is in-bounds!
        }

        return false;
    }
    int create_island(std::vector<std::vector<int>>& grid,
            std::vector<std::vector<bool>>& visited,
            int row,
            int col) {
        visited[row][col] = true;
        int count = 1;
        for (auto& direction : directions) {
            int new_row = row + direction[0];
            int new_col = col + direction[1];
            if (new_row < 0 || new_row >= grid.size())
                continue;
            if (new_col < 0 || new_col >= grid[0].size())
                continue;
            if (visited[new_row][new_col])
                continue;
            if (borders_land(grid, new_row, new_col))
                continue;

            count += create_island(grid, visited, new_row, new_col);
        }

        return count;
    }
public:
    int largestIsland(std::vector<std::vector<int>>& grid) {
        std::vector<std::vector<bool>> visited(grid.size(), std::vector<bool>(grid[0].size(), false));
        int largest = 0;
        for (int row = 0; row < grid.size(); row++) {
            for (int col = 0; col < grid[0].size(); col++) {
                if (grid[row][col] == 1)
                    continue;
                if (visited[row][col])
                    continue;
                if (borders_land(grid, row, col))
                    continue;

                largest = std::max(largest, create_island(grid, visited, row, col));
            }
        }

        return largest;
    }
};