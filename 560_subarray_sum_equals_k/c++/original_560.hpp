#pragma once

#include <vector>
#include <unordered_map>

int subarraySum(std::vector<int>& nums, int k) {
    int count = 0;
    int curr_prefix_sum = 0;
    std::unordered_map<int, int> prefix_sum_to_freq;
    prefix_sum_to_freq[0] = 1;
    for (int num : nums) {
        curr_prefix_sum += num;

        if (prefix_sum_to_freq.contains(curr_prefix_sum - k))
            count += prefix_sum_to_freq[curr_prefix_sum - k];
            
        prefix_sum_to_freq[curr_prefix_sum]++;
    }

    return count;
}