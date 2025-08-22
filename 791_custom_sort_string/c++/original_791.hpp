#pragma once

#include <string>
#include <unordered_set>

std::string customSortString_791_brute_force(std::string order, std::string s) {
    std::string result;
    for (char o_ch : order) {
        for (char ch : s) {
            if (ch == o_ch)
                result.push_back(ch);
        }
    }

    std::unordered_set<char> order_set(order.begin(), order.end());
    for (char ch : s) {
        if (!order_set.contains(ch))
            result.push_back(ch);
    }

    return result;
}

std::string customSortString_791(std::string order, std::string s) {
    std::unordered_map<char, int> freqs;
    for (char ch : s)
        freqs[ch]++;

    std::string result;
    for (char ch : order) {
        result += std::string(freqs[ch], ch);
        freqs.erase(ch);
    }

    for (auto [ch, freq] : freqs)
        result += std::string(freq, ch);

    return result;
}

