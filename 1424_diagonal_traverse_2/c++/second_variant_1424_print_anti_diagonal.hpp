#pragma once

#include <vector>
#include <iostream>

// VARIANT: What if you're given a full matrix and you had to print out the anti-diagonal order?
void helper_1424_second_variant(std::vector<std::vector<int>>& nums, int row, int col) {
    while (row < nums.size() && col >= 0)
        std::cout << nums[row++][col--] << ' ';
    std::cout << '\n';
}

void findAntiDiagonalOrder_1424_second_variant(std::vector<std::vector<int>>& nums) {
    for (int col = 0; col < nums[0].size(); col++)
    helper_1424_second_variant(nums, 0, col);

    for (int row = 1; row < nums.size(); row++) 
    helper_1424_second_variant(nums, row, nums[0].size() - 1);
}