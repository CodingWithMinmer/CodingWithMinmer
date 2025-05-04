#pragma once

#include <string>

// VARIANT: What if you had to solve the OG problem without any extra space complexity?
std::string minRemoveToMakeValid_Variant(std::string s) {
    int extra_opens = 0;
    int total_opens = 0;
    int j = 0;
    for (char ch : s) {
        if (ch == ')') {
            if (extra_opens == 0)
                continue;
            extra_opens--;
            s[j++] = ch;
        } else if (ch == '(') {
            total_opens++;
            extra_opens++;
            s[j++] = ch;
        } else {
            s[j++] = ch;
        }
    }

    int length = j;
    j = 0;
    int keep = total_opens - extra_opens;
    for (int i = 0; i < length; i++) {
        char ch = s[i];
        if (ch == '(') {
            if (keep == 0)
                continue;
            s[j++] = ch;
            keep--;
        } else {
            s[j++] = ch;
        }
    }

    return s.substr(0, j);
}

void minRemoveToMakeValid_Variant() {
    std::string s = "))((ab()c)(";
    assert(minRemoveToMakeValid_Variant(s) == "((ab)c)");

    s = "((ab((()))c)(";
    assert(minRemoveToMakeValid_Variant(s) == "((ab(()))c)");
}