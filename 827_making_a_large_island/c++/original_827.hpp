#pragma once

#include <vector>
#include <unordered_set>

class Solution827 {
    std::vector<std::vector<int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    int label_island(std::vector<std::vector<int>>& grid, int id,
                       int row, int col) {
        grid[row][col] = id;
        int count = 1;
        for (auto& direction : directions) {
            int new_row = row + direction[0];
            int new_col = col + direction[1];
            if (new_row < 0 || new_row >= grid.size())
                continue;
            if (new_col < 0 || new_col >= grid[0].size())
                continue;
            if (grid[new_row][new_col] != 1)
                continue;

            count += label_island(grid, id, new_row, new_col);
        }

        return count;
    }

    int create_island(std::vector<std::vector<int>>& grid,
                      std::unordered_map<int, int>& id_to_island_size,
                      int row, int col) { 
        std::unordered_set<int> visited; 
        int size = 1;
        for (auto& direction : directions) {
            int new_row = row + direction[0];
            int new_col = col + direction[1];
            if (new_row < 0 || new_row >= grid.size())
                continue;
            if (new_col < 0 || new_col >= grid[0].size())
                continue;
            if (grid[new_row][new_col] == 0)
                continue;
            if (visited.contains(grid[new_row][new_col]))
                continue;

            int id = grid[new_row][new_col];
            size += id_to_island_size[id];
            visited.insert(id);
        }

        return size;
    }

public:
    int largestIsland(std::vector<std::vector<int>>& grid) {
        int largest = 0;
        std::unordered_map<int, int> id_to_island_size;
        int id = 2;
        for (int row = 0; row < grid.size(); row++)
            for (int col = 0; col < grid[0].size(); col++)
                if (grid[row][col] == 1) {
                    int size = label_island(grid, id, row, col);
                    id_to_island_size[id] = size;
                    id++;
                    largest = std::max(largest, size);
                }

        for (int row = 0; row < grid.size(); row++)
            for (int col = 0; col < grid[0].size(); col++)
                if (grid[row][col] == 0)
                    largest = std::max(largest, create_island(grid, id_to_island_size, row, col));

        return largest;
    }
};