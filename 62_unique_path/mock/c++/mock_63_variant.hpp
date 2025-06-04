#pragma once
#include <string>
#include <iostream>
#include <vector>

// VARIANT: What if you had to return all the paths but there could be obstacles in the matrix?
class Solution63Variant_Obstacles {
public:
    void backtrack(std::vector<std::vector<int>>& grid,
        std::vector<std::string>& result, 
        std::string& path, 
        int n,
        int row, 
        int col) {
        if (row >= n || col >= n || grid[row][col] == 1)
            return;
        if (row == n - 1 && col == n - 1) {
            result.push_back(path);
            return;
        }

        path.push_back('R');
        backtrack(grid, result, path, n, row, col + 1);
        path.pop_back();

        path.push_back('D');
        backtrack(grid, result, path, n, row + 1, col);
        path.pop_back();
    }

    std::vector<std::string> get_unique_paths_with_obstacles(std::vector<std::vector<int>>& grid) {
        std::string path;
        int n = grid.size();
        std::vector<std::string> result;
        backtrack(grid, result, path, n, 0, 0);
        return result;
    }
};