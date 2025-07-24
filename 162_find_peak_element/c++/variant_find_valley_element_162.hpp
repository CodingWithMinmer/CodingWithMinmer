#pragma once

#include <cassert>
#include <vector>

// VARIANT: What if you had to find the valley element, no longer a peak element?
int FindValleyElement(std::vector<int>& nums) {
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right) {
        int mid = (right - left) / 2 + left;

        if ((mid == nums.size() - 1 || nums[mid + 1] > nums[mid]) &&
            (mid == 0 || nums[mid - 1] > nums[mid]))
            return mid;

        if (nums[mid + 1] < nums[mid])
            left = mid + 1;
        else
            right = mid - 1;
    }

    return -1; // Unreachable
}

void FindValleyElement() {
    std::vector<int> nums = {1, 2, 3, 1}; // Left pos infinity yields valley
    assert(0 == FindValleyElement(nums));

    nums = {1, 2, 3, 5, 3, 4, 3, 1, 6};
    assert(4 == FindValleyElement(nums));

    nums = {3, 2, 3, 4, 3, 2};
    assert(1 == FindValleyElement(nums));

    nums = {1, 2, 3, 4, 3, 2};
    assert(0 == FindValleyElement(nums));

    nums = {1, 2, 3, 2, 1, 0};
    assert(5 == FindValleyElement(nums)); // Right pos infinity yields valley

    nums = {1, 2, 3, 2, 1, 6};
    assert(4 == FindValleyElement(nums));
}