#pragma once

#include <unordered_map>
#include <vector>

class Solution_398 {
private:
    std::unordered_map<int, std::vector<int>> num_to_indices;

public:
    Solution_398(std::vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++)
            num_to_indices[nums[i]].push_back(i);
    }

    int pick(int target) {
        int n = num_to_indices[target].size();
        int r = rand() % n; // Remember our math logic
        return num_to_indices[target][r]; // We'll access the target num and return
        // a random index of the number our random generator spit out
    }
};