#pragma once

#include <vector>

class Solution_528 {
    std::vector<int> prefix_sums;

public:
    Solution_528(std::vector<int>& w) {
        for (int weight : w) {
            if (prefix_sums.empty())
                prefix_sums.push_back(weight);
            else
                prefix_sums.push_back(weight + prefix_sums.back());
        }
    }

    int pickIndex() {
        int roll = rand() % prefix_sums.back();
        int left = 0;
        int right = prefix_sums.size() - 1;
        while (left <= right) {
            int mid = ((right - left) / 2) + left;

            if (roll < prefix_sums[mid])
                right = mid - 1;
            else
                left = mid + 1;
        }
        return left;
    }
};
