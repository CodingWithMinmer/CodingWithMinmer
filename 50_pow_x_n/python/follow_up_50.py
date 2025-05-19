class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = abs(n)

        result = 1.0
        doubling_val = x
        while n != 0:
            if n % 2 == 1:
                result *= doubling_val
            doubling_val *= doubling_val
            n //= 2

        return result