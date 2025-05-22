#pragma once

#include <vector>
#include <queue>

class Kth_Smallest_DigitSums {
    int compute(int num) {
        int digit_sum = 0;
        while (num != 0) {
            digit_sum += num % 10;
            num /= 10;
        }
        return digit_sum;
    }
public:
    std::vector<int> kthSmallestDigitSums(std::vector<int> nums, int k) {
        std::priority_queue<std::pair<int, int>> max_heap;
        for (auto num : nums) {
            int digit_sum = compute(num);
            max_heap.push({digit_sum, num});
            if (max_heap.size() > k)
                max_heap.pop();
        }
        
        std::vector<int> result;
        while (!max_heap.empty()) {
            result.push_back(max_heap.top().second);
            max_heap.pop();
        }
        return result;
    }
};