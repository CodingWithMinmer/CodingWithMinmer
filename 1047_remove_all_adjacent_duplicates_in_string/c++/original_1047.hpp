#pragma once

#include <string>

std::string removeDuplicates(std::string s) {
    std::string result;
    for (char ch : s) {
        if (result.empty() || result.back() != ch)
            result.push_back(ch);
        else
            result.pop_back();
    }
    return result;
}