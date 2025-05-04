#pragma once

#include <vector>

// VARIANT: What if you had to return the number of unique elements in an integer array?
// Note this must be done in K LOG N time complexity (unless the input has all unique integers)
int countUniqueElements_second_variant_34(std::vector<int>& nums) {
    int count = 0;
    int i = 0;
    while (i < nums.size()) {
        int target = nums[i];
        int left = i;
        int right = nums.size() - 1;
        while (left <= right) {
            int mid = (left+right)/2;
            if (nums[mid] <= target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        count++;
        i = right + 1;
    }

    return count;
}