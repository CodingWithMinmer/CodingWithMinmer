#pragma once

#include <string>
#include <vector>
#include <sstream>

// VARIANT: What if you had to add two strings of numbers that could contain decimals?
// Both, one or neither could have decimals. Very, very tricky...
std::string addStrings_415(std::string num1, std::string num2, int& carry) {
    int n1 = num1.size() - 1;
    int n2 = num2.size() - 1;
    std::string result;
    while (n1 >= 0 || n2 >= 0) {
        int sum = 0;
        if (n1 >= 0)
            sum += num1[n1--] - '0';
        if (n2 >= 0)
            sum += num2[n2--] - '0';
        sum += carry;

        result.push_back(sum % 10 + '0');
        carry = sum / 10;
    }

    return result;
}

std::string addStringDecimals_415(std::string num1, std::string num2) {
    std::vector<std::string> nums1;
    std::string token;
    std::stringstream ss1(num1);
    while (std::getline(ss1, token, '.')) 
        nums1.push_back(token);
    std::vector<std::string> nums2;
    std::stringstream ss2(num2);
    while (std::getline(ss2, token, '.')) 
        nums2.push_back(token);

    std::string decimals1 = nums1.size() > 1 ? nums1[1] : "";
    std::string decimals2 = nums2.size() > 1 ? nums2[1] : "";
    bool has_decimals = !decimals1.empty() || !decimals2.empty();
    while (decimals1.size() != decimals2.size()) {
        if (decimals1.size() < decimals2.size())
            decimals1.push_back('0');
        else
            decimals2.push_back('0');
    }

    int carry = 0;
    std::string result;
    result += addStrings_415(decimals1, decimals2, carry);

    if (has_decimals)
        result.push_back('.');

    result += addStrings_415(nums1[0], nums2[0], carry);
    if (carry)
        result.push_back(carry + '0');
    std::reverse(result.begin(), result.end());
    return result;
}