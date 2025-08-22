#pragma once

#include <cassert>
#include <vector>

// VARIANT: What if you had to move zeroes to the front, not the back?
void move_zeroes_to_front(std::vector<int>& nums) {
    int swap_index = nums.size() - 1;
    for (int i = nums.size() - 1; i >= 0; i--) {
        if (nums[i] != 0) {
            std::swap(nums[i], nums[swap_index]);
            swap_index--;
        }
    }
}

void move_zeroes_to_front() {
    std::vector<int> nums = {1, 3, 12, 0, 0, 0};
    move_zeroes_to_front(nums);
    std::vector<int> expected = {0, 0, 0, 1, 3, 12};
    assert(nums == expected);

    nums = {0, 1, 0, 3, 12, 0};
    move_zeroes_to_front(nums);
    expected = {0, 0, 0, 1, 3, 12};
    assert(nums == expected);

    nums = {1, 3, 12, 0, 0, 0, 0, 0, 0};
    move_zeroes_to_front(nums);
    expected = {0, 0, 0, 0, 0, 0, 1, 3, 12};
    assert(nums == expected);

    nums = {};
    move_zeroes_to_front(nums);
    assert(nums.empty());

    nums = {0};
    move_zeroes_to_front(nums);
    expected = {0};
    assert(nums == expected);

    nums = {0, 0, 0};
    move_zeroes_to_front(nums);
    expected = {0, 0, 0};
    assert(nums == expected);

    nums = {1, 0, 3, 0, 12};
    move_zeroes_to_front(nums);
    expected = {0, 0, 1, 3, 12};
    assert(nums == expected);

    nums = {1, 2, 3, 4, 5};
    move_zeroes_to_front(nums);
    expected = {1, 2, 3, 4, 5};
    assert(nums == expected);

    nums = {0, 0, 3, 4, 5};
    move_zeroes_to_front(nums);
    expected = {0, 0, 3, 4, 5};
    assert(nums == expected);
}