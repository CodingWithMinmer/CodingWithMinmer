#pragma once

#include <cassert>
#include <vector>
#include <queue>

// VARIANT: What if you had to find the Kth smallest number in an integer array?
int findKthSmallest_215(std::vector<int>& nums, int k) {
    std::priority_queue<int> max_heap;
    for (auto num : nums) {
        max_heap.push(num);

        if (max_heap.size() > k)
            max_heap.pop();
    }

    return max_heap.top();
}

void findKthSmallest_215() {
    std::vector<int> nums = {3, 8, 4, 1, 10};
    int k = 3;
    assert(4 == findKthSmallest_215(nums, k));
    k = 1;
    assert(1 == findKthSmallest_215(nums, k));
    k = 2;
    assert(3 == findKthSmallest_215(nums, k));
    k = 4;
    assert(8 == findKthSmallest_215(nums, k));
    k = 5;
    assert(10 == findKthSmallest_215(nums, k));

    nums = {1, 1, 1, 1, 2};
    k = 1;
    assert(1 == findKthSmallest_215(nums, k));
    k = 2;
    assert(1 == findKthSmallest_215(nums, k));
    k = 3;
    assert(1 == findKthSmallest_215(nums, k));
    k = 4;
    assert(1 == findKthSmallest_215(nums, k));
    k = 5;
    assert(2 == findKthSmallest_215(nums, k));

    nums = {3, 2, 3, 1, 2, 4, 5, 5, 6};
    k = 4;
    assert(3 == findKthSmallest_215(nums, k));

    nums = {-1, -5, -2, -3, -4};
    k = 1;
    assert(-5 == findKthSmallest_215(nums, k));
    k = 2;
    assert(-4 == findKthSmallest_215(nums, k));
    k = 3;
    assert(-3 == findKthSmallest_215(nums, k));
    k = 4;
    assert(-2 == findKthSmallest_215(nums, k));
    k = 5;
    assert(-1 == findKthSmallest_215(nums, k));
}