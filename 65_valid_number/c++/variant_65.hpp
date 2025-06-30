#pragma once

#include <string>

// VARIANT: What if you didn't have to implement exponents?
bool isNumber_variant_65(std::string s) {
    bool seen_dot = false;
    bool seen_digit = false;
    for (int i = 0; i < s.size(); i++) {
        if (std::isdigit(s[i])) {
            seen_digit = true;
        }
        else if (s[i] == '-' || s[i] == '+') {
            if (i != 0)
                return false;

            seen_digit = false;
        }
        else if (s[i] == '.') {
            if (seen_dot)
                return false;

            seen_dot = true;
        }
        else
            return false;
    }

    if (!seen_digit)
        return false;
    return true;
}

void isNumber_variant_65() {
    std::string s = "420";
    assert(true == isNumber_variant_65(s));
//////////////////////////////////////////
    s = "7.";
    assert(true == isNumber_variant_65(s));

    s = "7..";
    assert(false == isNumber_variant_65(s));

    s = ".";
    assert(false == isNumber_variant_65(s));
//////////////////////////////////////////
    s = "+3";
    assert(true == isNumber_variant_65(s));

    s = "-10";
    assert(true == isNumber_variant_65(s));

    s = "3-";
    assert(false == isNumber_variant_65(s));

    s = "++6";
    assert(false == isNumber_variant_65(s));
//////////////////////////////////////////
    s = "+7e5";
    assert(false == isNumber_variant_65(s));

    s = "7E5";
    assert(false == isNumber_variant_65(s));

    s = "7ee";
    assert(false == isNumber_variant_65(s));

    s = "7e";
    assert(false == isNumber_variant_65(s));

    s = "8e1.2";
    assert(false == isNumber_variant_65(s));

    s = "+20e-5";
    assert(false == isNumber_variant_65(s));

    s = "+20e5";
    assert(false == isNumber_variant_65(s));
//////////////////////////////////////////
    s = "Abc";
    assert(false == isNumber_variant_65(s));
//////////////////////////////////////////
    s = "2";
    assert(true == isNumber_variant_65(s));

    s = "0089";
    assert(true == isNumber_variant_65(s));

    s = "-0.1";
    assert(true == isNumber_variant_65(s));

    s = "+3.14";
    assert(true == isNumber_variant_65(s));

    s = "4.";
    assert(true == isNumber_variant_65(s));

    s = "-.9";
    assert(true == isNumber_variant_65(s));
//////////////////////////////////////////
    s = "1a";
    assert(false == isNumber_variant_65(s));

    s = "--6";
    assert(false == isNumber_variant_65(s));

    s = "-+3";
    assert(false == isNumber_variant_65(s));
}