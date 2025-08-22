#pragma once

#include <string>

std::string minRemoveToMakeValid(std::string s) {
    int extra_opens = 0;
    int total_opens = 0;
    std::string temp;
    for (char ch : s) {
        if (ch == ')') {
            if (extra_opens == 0)
                continue;
            extra_opens--;
            temp.push_back(ch);
        } else if (ch == '(') {
            total_opens++;
            extra_opens++;
            temp.push_back(ch);
        } else {
            temp.push_back(ch);
        }
    }

    std::string result;
    int keep = total_opens - extra_opens;
    for (char ch : temp) {
        if (ch == '(') {
            if (keep == 0)
                continue;
            result.push_back(ch);
            keep--;
        } else {
            result.push_back(ch);
        }
    }

    return result;
}