#pragma once

#include <vector>

// VARIANT: What if you had to return the number of occurrences of a target number?
int searchRange_first_variant_34(std::vector<int>& nums, int target) {
    if (nums.empty())
        return 0;
    if (target < nums[0] || target > nums[nums.size() - 1])
        return 0;
    std::vector<int> result(2);
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right) {
        int mid = (right+left)/2;

        if (nums[mid] >= target)
            right = mid - 1;
        else
            left = mid + 1;
    }
    if (nums[left] != target)
        return 0;
    result[0] = left;

    left = 0;
    right = nums.size() - 1;
    while (left <= right) {
        int mid = (right+left)/2;

        if (nums[mid] <= target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    result[1] = right;

    return result[1] - result[0] + 1;
}