#pragma once

#include <vector>
#include <string>
#include <iostream>

// VARIANT: What if you had to abide by 3 formatting requirements when capturing missing ranges?
std::vector<std::string> findMissingRanges_variant_163(std::vector<int>& nums,
                                        int lower,
                                        int upper) {
    int curr_lower = lower;
    std::vector<std::string> missing_ranges;
    nums.push_back(upper + 1);
    for (int num : nums) {
        if (num - curr_lower > 2)
            missing_ranges.push_back(std::to_string(curr_lower) + '-' + std::to_string(num - 1));
        else if (num - curr_lower == 2) {
            missing_ranges.push_back(std::to_string(curr_lower));
            missing_ranges.push_back(std::to_string(curr_lower + 1));
        }
        else if (num - curr_lower == 1)
            missing_ranges.push_back(std::to_string(curr_lower));

        curr_lower = num + 1;
    }
    
    return missing_ranges;
}