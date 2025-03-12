class Solution:
    def addDecimalStrings(self, num1: str, num2: str) -> str:
        def splitNumber(num: str):
            n = num.split(".")
            if len(n) > 1:
                return n[0], n[1]
            return n[0], ""

        whole1, decimal1 = splitNumber(num1)
        whole2, decimal2 = splitNumber(num2)

        if len(decimal2) > len(decimal1):
            decimal1 += "0" * (len(decimal2) - len(decimal1))
        else:
            decimal2 += "0" * (len(decimal1) - len(decimal2))

        def addNonDecimal(a: str, b: str):
            """Takes two non decimal values and returns the sum"""
            p1, p2 = len(a) - 1, len(b) - 1
            carry = 0
            res = []
            while p1 >= 0 or p2 >= 0:
                x1 = ord(a[p1]) - ord("0") if p1 >= 0 else 0
                x2 = ord(b[p2]) - ord("0") if p2 >= 0 else 0
                value = (x1 + x2 + carry) % 10
                carry = (x1 + x2 + carry) // 10
                res.append(value)
                p1 -= 1
                p2 -= 1

            if carry > 0:
                res.append(carry)

            return "".join(str(x) for x in res[::-1])

        whole = addNonDecimal(whole1, whole2)
        decimal = addNonDecimal(decimal1, decimal2)
        return f"{whole}.{decimal}"


if __name__ == "__main__":
    solution = Solution()
    assert solution.addDecimalStrings("11.11", "123.5") == "134.61"
    assert solution.addDecimalStrings("9.", ".4") == "9.4"
    assert solution.addDecimalStrings(".15", "612") == "612.15"
