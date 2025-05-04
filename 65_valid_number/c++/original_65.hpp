#pragma once

#include <string>

bool isNumber_65(std::string s) {
    bool seen_dot = false;
    bool seen_digit = false;
    bool seen_exponent = false;
    for (int i = 0; i < s.size(); i++) {
        if (std::isdigit(s[i])) {
            seen_digit = true;
        }
        else if (s[i] == '-' || s[i] == '+') {
            if (i != 0 && s[i - 1] != 'e' && s[i - 1] != 'E')
                return false;
            
            seen_digit = false;
        }
        else if (s[i] == '.') {
            if (seen_dot || seen_exponent)
                return false;

            seen_dot = true;
        }
        else if (s[i] == 'e' || s[i] == 'E') {
            if (seen_exponent || !seen_digit)
                return false;

            seen_exponent = true;
            seen_digit = false;
        }
        else
            return false;
    }

    if (!seen_digit)
        return false;
    return true;
}

void isNumber_65() {
    std::string s = "420";
    assert(true == isNumber_65(s));
//////////////////////////////////////////
    s = "7.";
    assert(true == isNumber_65(s));

    s = "7..";
    assert(false == isNumber_65(s));

    s = ".";
    assert(false == isNumber_65(s));
//////////////////////////////////////////
    s = "+3";
    assert(true == isNumber_65(s));

    s = "-10";
    assert(true == isNumber_65(s));

    s = "3-";
    assert(false == isNumber_65(s));

    s = "++6";
    assert(false == isNumber_65(s));
//////////////////////////////////////////
    s = "+7e5";
    assert(true == isNumber_65(s));

    s = "7E5";
    assert(true == isNumber_65(s));

    s = "7ee";
    assert(false == isNumber_65(s));

    s = "7e";
    assert(false == isNumber_65(s));

    s = "8e1.2";
    assert(false == isNumber_65(s));

    s = "+20e-5";
    assert(true == isNumber_65(s));

    s = "+20e5";
    assert(true == isNumber_65(s));
//////////////////////////////////////////
    s = "Abc";
    assert(false == isNumber_65(s));
}