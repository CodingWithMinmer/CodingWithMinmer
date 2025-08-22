#pragma once

#include <string>

int addStrings_415(std::string num1, std::string num2,
               std::string &result, int carry)
{
    int n1 = num1.size() - 1;
    int n2 = num2.size() - 1;
    while (n1 >= 0 || n2 >= 0)
    {
        int sum = 0;
        if (n1 >= 0)
            sum += num1[n1--] - '0';
        if (n2 >= 0)
            sum += num2[n2--] - '0';
        sum += carry;

        result += std::to_string(sum % 10);
        carry = sum / 10;
    }

    if (carry)
        result += std::to_string(carry);

    std::reverse(result.begin(), result.end());
    return carry;
}

std::string addStrings_415(std::string num1, std::string num2)
{
    std::string result;
    int carry = 0;
    addStrings_415(num1, num2, result, carry);
    return result;
}