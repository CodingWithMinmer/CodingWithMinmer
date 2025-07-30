#pragma once

#include <vector>
#include <queue>

int findKthLargest_215(std::vector<int>& nums, int k) {
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    for (auto num : nums) {
        min_heap.push(num);

        if (min_heap.size() > k)
            min_heap.pop();
    }

    return min_heap.top();
}