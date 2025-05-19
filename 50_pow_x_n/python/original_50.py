class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0 / self.myPow(x, abs(n))
        if n == 0:
            return 1

        result = self.myPow(x, n // 2)

        if n % 2 == 1:
            return x * result * result
        return result * result
