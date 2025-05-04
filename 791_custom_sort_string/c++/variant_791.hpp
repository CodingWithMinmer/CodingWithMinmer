#pragma once

#include <string>
#include <unordered_map>

// VARIANT: What if you had to optimize the time complexity of your solution?
std::string customSortString_variant_791(std::vector<char>& order, std::string s) {
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