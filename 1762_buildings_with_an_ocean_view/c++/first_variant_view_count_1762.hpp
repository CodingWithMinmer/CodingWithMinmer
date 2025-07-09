#pragma once

#include <cassert>
#include <vector>

// VARIANT: What if you had to return the number of buildings with an ocean view?
int findBuildingViewCount_variant_1762(std::vector<int>& heights) {
    int n = heights.size();
    int count = 1;
    int right_max = heights[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        if (heights[i] > right_max) {
            count++;
            right_max = heights[i];
        }
    }

    return count;
}

void findBuildingViewCount_variant_1762() {
    std::vector<int> heights = {4, 2, 3, 1};
    assert(3 == findBuildingViewCount_variant_1762(heights));

    heights = {6, 1, 2, 4, 2, 2, 2, 2, 3, 1};
    assert(4 == findBuildingViewCount_variant_1762(heights));

    heights = {4, 3, 2, 1};
    assert(4 == findBuildingViewCount_variant_1762(heights));

    heights = {1, 3, 2, 4};
    assert(1 == findBuildingViewCount_variant_1762(heights));

    heights = {2, 2, 2, 2, 2, 2, 2};
    assert(1 == findBuildingViewCount_variant_1762(heights));

    heights = {0, 1, 2, 3, 2, 1, 0};
    assert(4 == findBuildingViewCount_variant_1762(heights));

    heights = {1, 2, 3, 4};
    assert(1 == findBuildingViewCount_variant_1762(heights));

    heights = {10};
    assert(1 == findBuildingViewCount_variant_1762(heights));
}