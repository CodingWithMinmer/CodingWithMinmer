#pragma once
#include <string>
#include <vector>
#include <unordered_map>

class Solution_249 {
    std::string shift(std::string string) {
        std::string key;
        int left_shifts = string[0] - 'a';
        for (char ch : string) {
            int encoded_char = ch - left_shifts + 26;
            if (encoded_char > 122)
                encoded_char -= 26;
            key.push_back(static_cast<char>(encoded_char));
        }
        return key;
    }
public:
    std::vector<std::vector<std::string>> groupStrings(std::vector<std::string>& strings) {
        std::unordered_map<std::string, std::vector<std::string>> shifted_to_originals;
        for (auto& string : strings) {
            auto shifted = shift(string);
            shifted_to_originals[shifted].push_back(string);
        }

        std::vector<std::vector<std::string>> result;
        for (auto [_, originals] : shifted_to_originals)
            result.push_back(originals);
        return result;
    }
};