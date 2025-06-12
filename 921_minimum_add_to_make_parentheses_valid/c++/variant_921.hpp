#pragma once

#include <string>
#include <assert.h>
#include <iostream>

// VARIANT: What if you had to return the parentheses string itself after the minimum adds?
std::string minAddToMakeValid_variant(std::string s) {
    std::string result;
    int extra_open_parentheses = 0;
    for (char ch : s) {
        if (ch == '(') {
            extra_open_parentheses++;
        }
        else if (ch == ')') {
            if (extra_open_parentheses == 0) {
                result.push_back('(');
                result.push_back(')');
                continue;
            }
            extra_open_parentheses--;
        }
        result.push_back(ch);
    }
    result += std::string(extra_open_parentheses, ')');
    return result;
}

void minAddToMakeValid_variant() {
    std::string s = ")))";
    assert("()()()" ==  minAddToMakeValid_variant(s));

    s = "(((";
    assert("((()))" ==  minAddToMakeValid_variant(s));

    s = "";
    assert("" ==  minAddToMakeValid_variant(s));

    s = "(())";
    assert("(())" ==  minAddToMakeValid_variant(s));

    s = ")))(((";
    assert("()()()((()))" ==  minAddToMakeValid_variant(s));

    s = "abcxyz";
    assert("abcxyz" ==  minAddToMakeValid_variant(s));

    s = "(()()))((";
    assert("(()())()(())" ==  minAddToMakeValid_variant(s));

    s = "((a)()))((xyz";
    assert("((a)())()((xyz))" ==  minAddToMakeValid_variant(s));
}