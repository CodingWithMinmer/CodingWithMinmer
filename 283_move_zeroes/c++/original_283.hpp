#pragma once

#include <vector>

void moveZeroes(std::vector<int>& nums) {
    int swap_index = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            std::swap(nums[i], nums[swap_index]);
            swap_index++;
        }
    }
}