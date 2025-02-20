#pragma once

#include <vector>

int randomPickIndex_second_variant_398(std::vector<int>& nums)
{
    int max_number = INT_MIN;
    int picked_index = -1;
    int n = 0;
    for (int i = 0; i < nums.size(); i++) {
        int curr_num = nums[i];
        if (curr_num < max_number)
            continue;

        if (curr_num > max_number) {
            max_number = curr_num;
            picked_index = i;
            n = 1;
        }
        else if (curr_num == max_number) {
            n++;
            int r = rand() % n;
            if (r == 0)
                picked_index = i;
        }
    }
    return picked_index;
}