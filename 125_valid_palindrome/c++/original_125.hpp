#pramga once

#include <string>

bool isPalindrome_125(std::string s) {
    int left = 0;
    int right = s.length() - 1;
    while (left < right) {
        while (!std::isalnum(s[left]) && left < right)
            left++;
        while (!std::isalnum(s[right]) && left < right)
            right--;

        if (std::tolower(s[left]) != std::tolower(s[right]))
            return false;

        left++;
        right--;
    }

    return true;
}