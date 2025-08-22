#pragma once

#include <vector>

class SparseVector {
public:
    std::vector<std::pair<int, int>> index_to_num;

    SparseVector(std::vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0)
                index_to_num.push_back(std::pair{i, nums[i]});
        }
    }

    int dotProduct(SparseVector& vec) {
        int sum = 0;
        int i = 0;
        int j = 0;
        while (i < index_to_num.size() && j < vec.index_to_num.size()) {
            if (index_to_num[i].first == vec.index_to_num[j].first) {
                sum += index_to_num[i].second * vec.index_to_num[j].second;
                i++;
                j++;
            }
            else if (index_to_num[i].first > vec.index_to_num[j].first)
                j++;
            else
                i++;
        }

        return sum;
    }
};