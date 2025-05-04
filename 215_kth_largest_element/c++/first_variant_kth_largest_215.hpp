#pragma once

#include <cassert>
#include <vector>
#include <queue>

// VARIANT: What if you had to return the Kth + 1 largest number in an integer array?
int findKthLargest_first_variant_215(std::vector<int>& nums, int k) {
    if (k + 1 > nums.size())
        throw std::out_of_range("k + 1 cannot exceed n.");
        
    k = k + 1;
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    for (auto num : nums) {
        min_heap.push(num);

        if (min_heap.size() > k)
            min_heap.pop();
    }

    return min_heap.top();
}