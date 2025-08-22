#pragma once

#include <string>
#include <vector>

// VARIANT: What happens if Meta once again announces their hatred for maps, and you had
// to use a list instead? Ideally, it's an array on the stack, not a vector like what I did. Don't be like me.
std::string customSortString_follow_up_791(std::string order, std::string s) {
    std::vector<int> freqs(26, 0);
    for (char ch : s)
        freqs[ch - 'a']++;

    std::string result;
    for (char ch : order) {
        result += std::string(freqs[ch - 'a'], ch);
        freqs[ch - 'a'] = 0;
    }

    for (int i = 0; i < freqs.size(); i++)
        result += std::string(freqs[i], i + 'a');

    return result;
}