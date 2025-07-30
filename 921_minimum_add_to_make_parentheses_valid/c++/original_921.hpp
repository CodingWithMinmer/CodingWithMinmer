#pragma once

#include <string>
#include <assert.h>

std::string minAddToMakeValid_921(std::string s) {
    int min_adds = 0;
    int extra_open_parentheses = 0;
    for (char ch : s) {
        if (ch == '(')
            extra_open_parentheses++;
        else if (ch == ')') {
            if (extra_open_parentheses == 0) {
                min_adds++;
                continue;
            }
            extra_open_parentheses--;
        }
    }

    return extra_open_parentheses + min_adds;
}