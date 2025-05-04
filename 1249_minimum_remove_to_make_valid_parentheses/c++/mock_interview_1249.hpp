#pragma once

#include <cassert>
#include <string>
#include <unordered_map>
#include <iostream>

// VARIANT: What if you were given different types of parentheses?
// Each type of parenthesis is balanced independently of the others.
// Otherwise, this might explode into a DP problem and Meta swear to never ask 
// Dynamic programming. They'd never lie, right?
std::string delete_least_parentheses(std::string& s) {
    std::unordered_map<char, char> mapping = {
        {')', '('},
        {']', '['},
        {'}', '{'}
    };
    std::unordered_map<char, int> extra_opens;
    std::unordered_map<char, int> total_opens;
    std::string temp;
    for (char ch : s) {
        if (mapping.contains(ch)) { // Closing parentheses
            if (extra_opens[mapping[ch]] == 0)
                continue;
            extra_opens[mapping[ch]]--;
            temp.push_back(ch);
        }
        else if (std::isalnum(ch)) { // 'a' or '3'
            temp.push_back(ch);
        }
        else { // Opening parentheses
            extra_opens[ch]++;
            total_opens[ch]++;
            temp.push_back(ch);
        }
    }

    std::unordered_map<char, int> keep;
    for (auto [open, _] : total_opens) {
        keep[open] = total_opens[open] - extra_opens[open];
    }
    std::string result;
    for (char ch : temp) {
        if (total_opens.contains(ch)) { // Opening parentheses
            if (keep[ch] == 0)
                continue;
            keep[ch]--;
            result.push_back(ch);
        }
        else {
            result.push_back(ch);
        }
    }
    return result;
}

void delete_least_parentheses() {
    std::string s = "[lee(t(c)o))))d[[e)(({{}}}";
    assert(delete_least_parentheses(s) == "lee(t(c)o)de{{}}");

    s = "(()))))minmer((((()([][[{{}";
    assert(delete_least_parentheses(s) == "(())minmer()[]{}");

    s = "(()))()";
    assert(delete_least_parentheses(s) == "(())()");

    s = "{[({)]}}";
    assert(delete_least_parentheses(s) == "{[({)]}}");

    s = ")))";
    assert(delete_least_parentheses(s).empty());

    s = "((((";
    assert(delete_least_parentheses(s).empty());

    s = "({({([}";
    assert(delete_least_parentheses(s) == "{}");

    s = "([)]";
    assert(delete_least_parentheses(s) == "([)]");

    s = "([)";
    assert(delete_least_parentheses(s) == "()");

    s = "))((ab()c)(";
    assert(delete_least_parentheses(s) == "((ab)c)");

    s = "((ab((()))c)(";
    assert(delete_least_parentheses(s) == "((ab(()))c)");
}
