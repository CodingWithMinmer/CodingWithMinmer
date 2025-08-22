#pragma once

#include <cassert>
#include <queue>

// VARIANT: What if you had to return a resulting array of the averages of each subarray of size, "size"?
std::vector<int> compute_running_sum_variant_346(std::vector<int>& nums, int size)
{
    std::vector<int> result;
    int window_sum = 0;
    for (int right = 0; right < nums.size(); right++) {
        window_sum += nums[right];

        int left = right - size;
        if (left >= 0)
            window_sum -=nums[left];

        if (right >= size - 1)
            result.push_back(window_sum / size);
    }

    return result;
}

void compute_running_sum_variant_346() {
    std::vector<int> nums = {5, 2, 8, 14, 3};
    int k = 3;
    std::vector<int> expected = {5, 8, 8};
    assert(expected == compute_running_sum_variant_346(nums, k));

    nums = {6};
    k = 1;
    expected = {6};
    assert(expected == compute_running_sum_variant_346(nums, k));

    nums = {1, 2, 3};
    k = 1;
    expected = {1, 2, 3};
    assert(expected == compute_running_sum_variant_346(nums, k));

    nums = {2, 4, 6, 8, 10, 12};
    k = 2;
    expected = {3, 5, 7, 9, 11};
    assert(expected == compute_running_sum_variant_346(nums, k));

    nums = {2, 4, 6, 8, 10, 12};
    k = 6;
    expected = {(2+4+6+8+10+12)/6};
    assert(expected == compute_running_sum_variant_346(nums, k));

    nums = {1, 2, 3, 4, 5};
    k = 4;
    expected = {2, 3};
    assert(expected == compute_running_sum_variant_346(nums, k));

    nums = {1, 2, 1, 2};
    k = 2;
    expected = {1, 1, 1};
    assert(expected == compute_running_sum_variant_346(nums, k));
}