#pragma once

#include <vector>

std::vector<int> searchRange(std::vector<int>& nums, int target) {
    if (nums.empty())
        return {-1, -1};
    if (target < nums[0] || target > nums[nums.size() - 1])
        return {-1, -1};
    std::vector<int> result(2);

    int left = 0;
    int right = nums.size() - 1;
    while (left <= right) {
        int mid = ((right - left) / 2) + left;

        if (nums[mid] >= target)
            right = mid - 1;
        else
            left = mid + 1;
    }
    if (nums[left] != target)
        return {-1, -1};
    result[0] = left;

    left = 0;
    right = nums.size() - 1;
    while (left <= right) {
        int mid = ((right - left) / 2) + left;

        if (nums[mid] <= target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    result[1] = right;

    return result;
}