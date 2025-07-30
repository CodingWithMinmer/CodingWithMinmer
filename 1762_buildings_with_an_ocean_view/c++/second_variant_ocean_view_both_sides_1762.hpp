#pragma once

#include <cassert>
#include <vector>

// VARIANT: What if you had to return all of the buildings that either have an ocean view
// to its left and/or its right? This becomes very similar to Leetcode 42 Trapping Rain Water
std::vector<int> findBuildingViewCount_second_variant_1762(std::vector<int>& heights) {
    int n = heights.size();
    if (n == 1)
        return {0};

    int left = 0, right = n - 1;
    std::vector<int> left_view{left};
    std::vector<int> right_view{right};
    int left_max = heights[left];
    int right_max = heights[right];
    while (left < right) {
        if (left_max < right_max) {
            left++;
            if (heights[left] > left_max && left < right) {
                left_view.push_back(left);
                left_max = heights[left];
            }
        }
        else {
            right--;
            if (heights[right] > right_max && left < right) {
                right_view.push_back(right);
                right_max = heights[right];
            }
        }
    }
    left_view.insert(left_view.end(), right_view.rbegin(), right_view.rend());
    return left_view;
}

void findBuildingViewCount_second_variant_1762() {
    std::vector<int> heights = {1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 2};
    std::vector<int> both_views = findBuildingViewCount_second_variant_1762(heights);
    assert(11 == both_views.size());
    std::vector<int> expected = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    assert(expected == both_views);

    heights = {1, 2, 3, 3, 2, 1};
    both_views = findBuildingViewCount_second_variant_1762(heights);
    assert(6 == both_views.size());
    expected = {0, 1, 2, 3, 4, 5};
    assert(expected == both_views);

    heights = {1, 4, 3, 9, 8, 6};
    both_views = findBuildingViewCount_second_variant_1762(heights);
    assert(5 == both_views.size());
    expected = {0, 1, 3, 4, 5};
    assert(expected == both_views);

    heights = {1, 2, 1, 1, 3, 1, 1, 3, 1, 3, 2, 1};
    both_views = findBuildingViewCount_second_variant_1762(heights);
    assert(6 == both_views.size());
    expected = {0, 1, 4, 9, 10, 11};
    assert(expected == both_views);

    heights = {1, 1, 1, 1};
    both_views = findBuildingViewCount_second_variant_1762(heights);
    assert(2 == both_views.size());
    expected = {0, 3};
    assert(expected == both_views);

    heights = {5};
    both_views = findBuildingViewCount_second_variant_1762(heights);
    assert(1 == both_views.size());
    expected = {0};
    assert(expected == both_views);

    heights = {1, 10};
    both_views = findBuildingViewCount_second_variant_1762(heights);
    assert(2 == both_views.size());
    expected = {0, 1};
    assert(expected == both_views);
}