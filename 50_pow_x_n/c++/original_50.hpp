#pragma once

#include <cmath>

class Solution_50 {
public:
    double myPow(double x, long long n) {
        if (n < 0)
            return 1.0 / myPow(x, std::abs(n));
        if (n == 0)
            return 1;

        double result = myPow(x, n / 2);

        if (n % 2 == 1)
            return x * result * result;
        return result * result;
    }

    double myPow(double x, int n) { 
        return myPow(x, (long long)n); 
    }
};