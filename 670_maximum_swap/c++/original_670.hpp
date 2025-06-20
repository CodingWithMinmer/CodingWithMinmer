#pragma once

#include <vector>
#include <string>

int maximumSwap_670(int num) {
    std::string num_str = std::to_string(num);
    std::array<int, 10> rightmost_index;
    rightmost_index.fill(-1);
    for (int i = 0; i < num_str.size(); i++)
        rightmost_index[num_str[i] - '0'] = i;

    for (int i = 0; i < num_str.size(); i++) {
        for (int j = 9; j > num_str[i] - '0'; j--) {
            if (rightmost_index[j] > i) {
                std::swap(num_str[i], num_str[rightmost_index[j]]);
                return std::stoi(num_str);
            }
        }
    }

    return num;
}