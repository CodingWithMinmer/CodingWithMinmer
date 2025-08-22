#pragma once

#include <vector>

int longestOnes_1004(std::vector<int>& nums, int k) {
    int max = 0;
    int left = 0;
    for (int right = 0; right < nums.size(); right++) {
        if (nums[right] == 0) {
            k--;
        }

        while (k < 0) {
            if (nums[left] == 0) {
                k++;
            }
            left++;
        }

        max = std::max(max, right - left + 1);
    }

    return max;
}