#pragma once

#include <cassert>
#include <vector>
#include <unordered_set>

// VARIANT: What if you had to return T/F if you find at least one pair of numbers that add up to the target?
bool twoSum_first_variant(std::vector<int>& nums, int target) {
    std::unordered_set<int> complements;
    for (auto num : nums) {
        int complement_num = target - num;
        if (complements.contains(complement_num))
            return true;

        complements.insert(num);
    }

    return false;
}

void twoSum_first_variant() {
    std::vector<int> nums = {2, 1, 8, 3, 4, 0, 5};
    int target = 5;
    assert(true == twoSum_first_variant(nums, target));

    nums = {2, 1, 8, 3, 4, 0, 5};
    target = 50;
    assert(false == twoSum_first_variant(nums, target));

    nums = {2, 7, 11, 15};
    target = 9;
    assert(true == twoSum_first_variant(nums, target));

    nums = {3, 2, 7};
    target = 6; 
    assert(false == twoSum_first_variant(nums, target));

    nums = {3, 3};
    target = 6;
    assert(true == twoSum_first_variant(nums, target));

    nums = {};
    target = 0;
    assert(false == twoSum_first_variant(nums, target));

    nums = {1, 1, 1, 1, 1, 1, 1};
    target = 2;
    assert(true == twoSum_first_variant(nums, target));
}