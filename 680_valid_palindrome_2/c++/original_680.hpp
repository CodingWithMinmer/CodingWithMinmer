#pragma once

#include <string>

bool check_remaining_680(std::string& s, int left, int right) {
    while (left < right) {
        if (s[left] == s[right]) {
            left++;
            right--;
            continue;
        }
        return false;
    }

    return true;
}
bool validPalindrome_680(std::string s) {
    int left = 0;
    int right = s.size() - 1;
    while (left < right) {
        if (s[left] == s[right]) {
            left++;
            right--;
            continue;
        }
        return check_remaining_680(s, left + 1, right) ||
            check_remaining_680(s, left, right - 1);
    }

    return true;
}