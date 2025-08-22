#pragma once

#include <vector>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> complement_to_index;
    for (int i = 0; i < nums.size(); i++) {
        int complement_num = target - nums[i];
        if (complement_to_index.contains(complement_num))
            return {i, complement_to_index[complement_num]};

        complement_to_index[nums[i]] = i;
    }

    return {};
}