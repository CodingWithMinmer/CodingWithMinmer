#pragma once

#include <cassert>
#include <vector>

// VARIANT: What if you had to optimize the space complexity in the case you're only given
// positive integers in the array?
bool subarraySum_second_variant_560(std::vector<int>& nums, int k) {
    int left = 0;
    int sum = 0;
    for (int right = 0; right < nums.size(); right++) {
        sum += nums[right];

        while (sum > k) {
            sum -= nums[left];
            left++;
        }

        if (sum == k)
            return true;
    }

    return false;
}

void subarraySum_second_variant_560() {
    // Below testcases were provided here: https://leetcode.com/discuss/interview-question/algorithms/124820/continuous-sequence-against-target-number
    std::vector<int> nums = {23, 5, 4, 7, 2, 11};
    int k = 20;
    assert(true == subarraySum_second_variant_560(nums, k));

    nums = {1, 3, 5, 23, 2};
    k = 8;
    assert(true == subarraySum_second_variant_560(nums, k));

    nums = {1, 3, 5, 23, 2};
    k = 7;
    assert(false == subarraySum_second_variant_560(nums, k));
    ////////////////////////////////////////////////////////////////////////

    nums = {4, 2, 5, 2, 6, 1};
    k = 9;
    assert(true == subarraySum_second_variant_560(nums, k));

    nums = {1, 2, 3, 4, 5, 6, 7};
    k = 100;
    assert(false == subarraySum_second_variant_560(nums, k));

    nums = {100, 101, 102, 103};
    k = 2;
    assert(false == subarraySum_second_variant_560(nums, k));
}