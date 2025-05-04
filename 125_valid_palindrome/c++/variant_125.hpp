#pragma once

#include <cassert>
#include <string>
#include <unordered_set>

// VARIANT: What if you could only consider a limited set of characters as a part of
// a potential palindrome?
bool isPalindrome_variant_125(std::string& s, std::vector<char>& include) {
    std::unordered_set<char> included_set(include.begin(), include.end());
    int left = 0;
    int right = s.size() - 1;
    while (left < right) {
        while (!included_set.contains(s[left]) && left < right) {
            left++;
        }
        while (!included_set.contains(s[right]) && left < right) {
            right--;
        }

        if (s[left] != s[right])
            return false;

        left++;
        right--;
    }

    return true;
}

void isPalindrome_variant_125() {
    std::string s = "yo banana boy!";
    std::vector<char> include = {'y', 'o', 'b', 'a', 'n'};
    assert(true == isPalindrome_variant_125(s, include));

    s = "Yo, banana boY!";
    include = {'Y', 'o', 'b', 'a', 'n'};
    assert(true == isPalindrome_variant_125(s, include));

    s = "a b c d e d c b a";
    include = {'a', ' ', 'b', 'c', 'd', 'e'};
    assert(true == isPalindrome_variant_125(s, include));

    s = "a b c d e d c b a";
    include = {'a', 'b', 'c', 'd', 'e'};
    assert(true == isPalindrome_variant_125(s, include));

    s = "a b c d e d c b a";
    include = {'a', 'b', 'e'};
    assert(true == isPalindrome_variant_125(s, include));

    s = "Wow";
    include = {'W', 'o', 'w'};
    assert(false == isPalindrome_variant_125(s, include));

    s = "WwoWWWWWWWWWWWWWow";
    include = {'o', 'w'};
    assert(true == isPalindrome_variant_125(s, include));

    s = "__________________";
    include = {'1', '2'};
    assert(true == isPalindrome_variant_125(s, include));

    s = "________133__________";
    include = {'1', '3'};
    assert(false == isPalindrome_variant_125(s, include));

    s = "____1____133_______________";
    include = {'1', '3', '_'};
    assert(false == isPalindrome_variant_125(s, include));

    s = "";
    include = {'1', '3', '_'};
    assert(true == isPalindrome_variant_125(s, include));

    s = "";
    include = {};
    assert(true == isPalindrome_variant_125(s, include));

    s = "MadaM";
    include = {};
    assert(true == isPalindrome_variant_125(s, include));

    s = "MadaM";
    include = {'z', 'M', 'd'};
    assert(true == isPalindrome_variant_125(s, include));

    s = "MadaMM";
    include = {'z', 'M', 'd'};
    assert(false == isPalindrome_variant_125(s, include));

    s = "racecarX";
    include = {'r', 'X'};
    assert(false == isPalindrome_variant_125(s, include));
}