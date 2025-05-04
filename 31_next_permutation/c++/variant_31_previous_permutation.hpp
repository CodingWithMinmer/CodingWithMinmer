#pragma once

#include <vector>

// VARIANT: What if you had to find the previous permutation?
void prevPermutation_31(std::vector<int>& nums) {
    int peak = -1;
    for (int i = nums.size() - 2; i >= 0; i--) {
        int num = nums[i];
        int num_after = nums[i + 1];

        if (num > num_after) {
            peak = i;
            break;
        }
    }
    if (peak == -1) {
        std::reverse(nums.begin(), nums.end());
        return;
    }

    int next_lower = nums.size() - 1;
    while (nums[next_lower] >= nums[peak])
        next_lower--;

    std::swap(nums[peak], nums[next_lower]);
    std::reverse(nums.begin() + peak + 1, nums.end());
}

void prevPermutation_31() {
    std::vector<int> nums = {3, 2, 1};
    std::vector<int> expected = {3, 1, 2};
    prevPermutation_31(nums);
    assert(expected == nums);

    nums = {1, 2, 3};
    expected = {3, 2, 1};
    prevPermutation_31(nums);
    assert(expected == nums);

    nums = {9, 6, 5, 4, 3, 2};
    expected = {9, 6, 5, 4, 2, 3};
    prevPermutation_31(nums);
    assert(expected == nums);

    nums = {4, 5, 1, 1, 3, 7};
    expected = {4, 3, 7, 5, 1, 1};
    prevPermutation_31(nums);
    assert(expected == nums);
}