#pragma once

#include <vector>
#include <queue>

// VARIANT: What happens if you have to return the path of a shortest path?
class Solution_1091_First_Variant {
    struct cell {
        int row;
        int col;
        std::vector<std::vector<int>> path;
    };
    std::vector<std::vector<int>> directions = {{-1, 0}, {-1, 1}, {0, 1},
                                                {1, 1},  {1, 0},  {1, -1},
                                                {0, -1}, {-1, -1}};
public:
    std::vector<std::vector<int>> shortestPathBinaryMatrix(std::vector<std::vector<int>>& grid) {
        if (grid[0][0] == 1 || grid[grid.size() - 1][grid[0].size() - 1] == 1)
            return {};

        grid[0][0] = 1;
        std::queue<cell> q;
        q.emplace(cell{0, 0, {{0, 0}}});
        while (!q.empty()) {
            auto [row, col, path] = q.front();
            q.pop();

            if (row == grid.size() - 1 && col == grid[0].size() - 1)
                return path;

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
                auto path_copy = path;
                path_copy.push_back({new_row, new_col});
                q.emplace(cell{new_row, new_col, path_copy});
            }
        }
        
        return {}; // Unreachable
    }
};
