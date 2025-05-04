#pragma once

#include <string>

class Solution_227 {
public:
    int calculate(std::string s) {
        int curr_num = 0;
        int prev_num = 0;
        int result = 0;
        char op = '+';
        for (int i = 0; i < s.size(); i++) {
            if (std::isdigit(s[i]))
                curr_num = curr_num * 10 + (s[i] - '0');
    
            if ((!std::isdigit(s[i]) && s[i] != ' ') || i == s.size() - 1) {
                if (op == '+') {
                    result += prev_num;
                    prev_num = curr_num;
                } else if (op == '-') {
                    result += prev_num;
                    prev_num = curr_num * -1;
                } else if (op == '*')
                    prev_num = prev_num * curr_num;
                else if (op == '/')
                    prev_num = prev_num / curr_num;
    
                curr_num = 0;
                op = s[i];
            }
        }
    
        result += prev_num;
        return result;
    }
};