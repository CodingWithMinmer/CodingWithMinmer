#pragma once

#include <vector>

int findPeakElement(std::vector<int>& nums) {
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right) {
        int mid = (right - left) / 2 + left;

        if ((mid == nums.size() - 1 || nums[mid + 1] < nums[mid]) &&
            (mid == 0 || nums[mid - 1] < nums[mid]))
            return mid;

        if (nums[mid + 1] > nums[mid])
            left = mid + 1;
        else if (nums[mid - 1] > nums[mid])
            right = mid - 1;
    }

    return -1; // Unreachable
}