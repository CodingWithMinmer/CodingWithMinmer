#pragma once

#include <vector>

// VARIANT: What if you had to use reservoir sampling to randomly sample K numbers without replacement probability?
std::vector<int> randomPickIndices_first_variant_398(std::vector<int>& nums, int k)
{
    std::vector<int> result(k);
    for (int i = 0; i < k; i++)
        result[i] = nums[i];

    for (int i = k; i < nums.size(); i++) {
        int n = i + 1;
        int r = rand() % n;
        if (r < k)
            result[r] = nums[i];
    }
    
    return result;
}