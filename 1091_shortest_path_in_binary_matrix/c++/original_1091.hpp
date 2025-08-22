#pragma once

#include <vector>
#include <queue>

class Solution_1091 {
    struct cell {
        int row;
        int col;
        int steps;
    };
    std::vector<std::vector<int>> directions = {{-1, 0}, {-1, 1}, {0, 1},
                                                {1, 1},  {1, 0},  {1, -1},
                                                {0, -1}, {-1, -1}};
public:
    int shortestPathBinaryMatrix(std::vector<std::vector<int>>& grid) {
        if (grid[0][0] == 1 || grid[grid.size() - 1][grid[0].size() - 1] == 1)
            return -1;
    
        grid[0][0] = 1;
        std::queue<cell> q;
        q.emplace(cell{0, 0, 1});
        while (!q.empty()) {
            auto [row, col, steps] = q.front();
            q.pop();
    
            if (row == grid.size() - 1 && col == grid[0].size() - 1)
                return steps;
    
            for (int d = 0; d < directions.size(); d++) {
                int new_row = row + directions[d][0];
                int new_col = col + directions[d][1];
                if (new_row < 0 || new_row >= grid.size())
                    continue;
                if (new_col < 0 || new_col >= grid[0].size())
                    continue;
                if (grid[new_row][new_col] == 1)
                    continue;
    
                grid[new_row][new_col] = 1;
                q.emplace(cell{new_row, new_col, steps + 1});
            }
        }
    
        return -1; // Unreachable
    }
};