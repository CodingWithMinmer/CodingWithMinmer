#pragma once
#include <string>
#include <vector>
#include <unordered_map>

// VARIANT: What if you had to right shift a given string by a given rotational factor?
class Solution_249_Variant {
public:
    std::string rotationalCipher(std::string string, int rotation_factor) {
        if (rotation_factor == 0)
            return string;

        std::string result;
        for (char ch : string) {
            if (std::islower(ch)) {
                result.push_back((ch - 'a' + rotation_factor) % 26 + 'a');
            }
            else if (std::isupper(ch)) {
                result.push_back((ch - 'A' + rotation_factor) % 26 + 'A');
            }
            else if (std::isdigit(ch)) {
                result.push_back((ch - '0' + rotation_factor) % 10 + '0');
            }
            else {
                result.push_back(ch);
            }
        }

        return result;
    }
};