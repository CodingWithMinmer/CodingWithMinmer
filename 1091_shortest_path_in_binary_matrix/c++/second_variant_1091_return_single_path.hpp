#pragma once

#include <vector>

// VARIANT: What if you had to return a single path? Note it's not necessarily the shortest.
class Solution_1091_Second_Variant
{
    bool dfs_1091(std::vector<std::vector<int>>& grid, std::vector<std::vector<int>>& path, int row, int col) {
        grid[row][col] = 1;
        path.push_back({row, col});

        if (row == grid.size() - 1 && col == grid[0].size() - 1)
            return true;

        for (int d = 0; d < directions.size(); d++) {
            int new_row = row + directions[d][0];
            int new_col = col + directions[d][1];
            if (new_row < 0 || new_row >= grid.size())
                continue;
            if (new_col < 0 || new_col >= grid[0].size())
                continue;
            if (grid[new_row][new_col] == 1)
                continue;

            if (dfs_1091(grid, path, new_row, new_col))
                return true;
        }

        path.pop_back();
        return false;
    }
    std::vector<std::vector<int>> directions = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1},  {1, 0},  {1, -1}, {0, -1}, {-1, -1}};

public:
    std::vector<std::vector<int>> pathBinaryMatrix(std::vector<std::vector<int>>& grid)
    {
        if (grid[0][0] == 1 || grid[grid.size() - 1][grid[0].size() - 1] == 1)
            return {};

        std::vector<std::vector<int>> path;
        dfs_1091(grid, path, 0, 0);
        return path;
    }
};