#pragma once

#include <cmath>

// Follow-up: What if you had to solve the problem in SC O(1)?
// Retain the TC of O(LOG N).
class Solution_50_FollowUp {
public:
    double binaryExp(double x, long long n) {
        if (n < 0) {
            x = 1.0 / x;
            n = std::abs(n);
        }

        double result = 1.0;
        double doubling_val = x;
        while (n != 0) {
            if (n % 2 == 1) 
                result *= doubling_val;

            doubling_val *= doubling_val;
            n /= 2;
        }
        return result;
    }

    double myPow(double x, int n) { 
        return binaryExp(x, (long long)n); 
    }
};