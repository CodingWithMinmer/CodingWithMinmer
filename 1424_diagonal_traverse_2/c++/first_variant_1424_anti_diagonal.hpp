#pragma once

#include <vector>
#include <queue>

// VARIANT: What if you had to return a list of the anti-diagonal traversal?
std::vector<std::vector<int>> findAntiDiagonalOrder_1424_first_variant(std::vector<std::vector<int>>& nums) {
    std::vector<std::vector<int>> result;
    std::queue<std::pair<int, int>> q;
    q.emplace(std::pair{0, 0});
    while (!q.empty()) {
        int size = q.size();
        std::vector<int> curr_level;
        for (int i = 0; i < size; i++) {
            auto [row, col] = q.front();
            q.pop();

            curr_level.push_back(nums[row][col]);

            if (col + 1 < nums[row].size())
                q.emplace(std::pair{row, col + 1});
            if (col == 0 && row + 1 < nums.size())
                q.emplace(std::pair{row + 1, col});
        }
        result.push_back(curr_level);
    }

    return result;
}