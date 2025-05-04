#pragma once

#include <vector>

std::vector<int> findBuildings(std::vector<int>& heights) {
    int n = heights.size();
    std::vector<int> right_view{n - 1};
    int right_max = heights[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        if (heights[i] > right_max) {
            right_view.push_back(i);
            right_max = heights[i];
        }
    }

    std::reverse(right_view.begin(), right_view.end());
    return right_view;
}
