#pragma once

#include <vector>

void nextPermutation_31(std::vector<int>& nums) {
    int valley = -1;
    for (int i = nums.size() - 2; i >= 0; i--) {
        int num = nums[i];
        int num_after = nums[i + 1];

        if (num < num_after) {
            valley = i;
            break;
        }
    }
    if (valley == -1) {
        std::reverse(nums.begin(), nums.end());
        return;
    }

    int next_higher = nums.size() - 1;
    while (nums[next_higher] <= nums[valley])
        next_higher--;

    std::swap(nums[valley], nums[next_higher]);
    std::reverse(nums.begin() + valley + 1, nums.end());
}