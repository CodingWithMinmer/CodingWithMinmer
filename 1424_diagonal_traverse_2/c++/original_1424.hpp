#pragma once

#include <vector>
#include <queue>

std::vector<int> findDiagonalOrder_1424(std::vector<std::vector<int>>& nums) {
    std::vector<int> result;
    std::queue<std::pair<int, int>> q;
    q.emplace(std::pair{0, 0});
    while (!q.empty()) {
        auto [row, col] = q.front();
        q.pop();

        result.push_back(nums[row][col]);

        if (col == 0 && row + 1 < nums.size())
            q.emplace(std::pair{row + 1, col});

        if (col + 1 < nums[row].size())
            q.emplace(std::pair{row, col + 1});
    }

    return result;
}