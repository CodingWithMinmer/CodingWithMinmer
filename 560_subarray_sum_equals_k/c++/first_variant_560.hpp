#pragma once

#include <vector>
#include <unordered_set>

// VARIANT: What if you had to return true or false if there exists at least one
// subarray that equals K?
bool subarraySum_first_variant_560(std::vector<int>& nums, int k) {
    int curr_prefix_sum = 0;
    std::unordered_set<int> prefix_sums;
    prefix_sums.insert(0);
    for (int num : nums) {
        curr_prefix_sum += num;

        if (prefix_sums.contains(curr_prefix_sum - k))
            return true;

        prefix_sums.insert(curr_prefix_sum);
    }

    return false;
}