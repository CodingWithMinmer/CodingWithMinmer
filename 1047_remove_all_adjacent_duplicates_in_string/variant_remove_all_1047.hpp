#pragma once

#include <cassert>
#include <string>
#include <vector>

// VARIANT: What if you had to remove all adjacent duplicates as you iterate
// left-to-right?
struct letter {
    char val;
    int freq;
};
std::string remove_all_adjacent_duplicates_variant_1047(std::string& s) {
    std::vector<letter> letters;
    for (char ch : s) {
        if (letters.empty()) {
            letters.push_back(letter{ch, 1});
            continue;
        }
        if (letters.back().val == ch) {
            letters.back().freq++;
            continue;
        }

        if (letters.back().freq > 1)
            letters.pop_back();

        if (letters.empty() || letters.back().val != ch)
            letters.push_back(letter{ch, 1});
        else if (letters.back().val == ch)
            letters.back().freq++;
    }
    if (!letters.empty() && letters.back().freq > 1)
        letters.pop_back();

    std::string result;
    for (auto [val, _] : letters)
        result += val;
    return result;
}

void remove_all_adjacent_duplicates_variant_1047() {
    std::string s = "azxxxzy";
    assert("ay" == remove_all_adjacent_duplicates_variant_1047(s));

    s = "abbaxx";
    assert(remove_all_adjacent_duplicates_variant_1047(s).empty());

    s = "aabbccdd";
    assert(remove_all_adjacent_duplicates_variant_1047(s).empty());

    s = "aaabbaad";
    assert("d" == remove_all_adjacent_duplicates_variant_1047(s));

    s = "abcdefg";
    assert("abcdefg" == remove_all_adjacent_duplicates_variant_1047(s));

    s = "abbcddeff";
    assert("ace" == remove_all_adjacent_duplicates_variant_1047(s));

    s = "abcdeffedcba";
    assert(remove_all_adjacent_duplicates_variant_1047(s).empty());

    s = "aabccddeeffbbbbbbbbbf";
    assert("f" == remove_all_adjacent_duplicates_variant_1047(s));

    s = "abbbacca"; // Cannot pick and choose duplicates in the middle to delete first
    assert("a" == remove_all_adjacent_duplicates_variant_1047(s));

    s = "abccba";
    assert("" == remove_all_adjacent_duplicates_variant_1047(s));

    s = "abbbacxdd";
    assert("cx" == remove_all_adjacent_duplicates_variant_1047(s));
}
