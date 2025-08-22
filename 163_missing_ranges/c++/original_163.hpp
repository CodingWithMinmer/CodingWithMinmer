#pragma once

#include <vector>

std::vector<std::vector<int>> findMissingRanges(std::vector<int>& nums, int lower, int upper) {
    if (nums.empty())
        return {{lower, upper}};

    std::vector<std::vector<int>> missing_ranges;
    if (lower < nums[0])
        missing_ranges.push_back({lower, nums[0] - 1});

    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] - nums[i - 1] - 1 == 0)
            continue;
        missing_ranges.push_back({nums[i - 1] + 1, nums[i] - 1});
    }

    if (upper > nums[nums.size() - 1])
        missing_ranges.push_back({nums[nums.size() - 1] + 1, upper});

    return missing_ranges;
}