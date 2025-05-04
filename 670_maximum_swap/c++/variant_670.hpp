#pragma once

#include <vector>
#include <string>

// VARIANT: What if you had to build the second largest number?
std::vector<int> get_second_largest_number_670(std::vector<int>& num) {
    if (num.empty() || num.size() == 1)
        return {};

    std::vector<int> freqs(10, 0);
    for (int digit : num)
        freqs[digit]++;

    std::vector<int> largest_num;
    for (int digit = freqs.size() - 1; digit >= 0; digit--)
        for (int times = 0; times < freqs[digit]; times++)
            largest_num.push_back(digit);

    for (int i = largest_num.size() - 1; i > 0; i--) {
        if (largest_num[i] != largest_num[i - 1]) {
            std::swap(largest_num[i], largest_num[i - 1]);
            return largest_num;
        }
    }
    return {};
}
