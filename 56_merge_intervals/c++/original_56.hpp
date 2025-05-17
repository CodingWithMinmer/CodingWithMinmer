#pragma once

#include <vector>


std::vector<std::vector<int>> merge_56(std::vector<std::vector<int>>& intervals) {
    std::sort(intervals.begin(), intervals.end(), [](std::vector<int>& a, std::vector<int>& b) {
        return a[0] < b[0];
    });

    std::vector<std::vector<int>> result;
    for (auto curr_interval : intervals) {
        if (result.empty() || curr_interval[0] > result.back()[1])
            result.push_back(curr_interval);
        else
            result.back()[1] = std::max(curr_interval[1], result.back()[1]);
    }

    return result;
}