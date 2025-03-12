class Solution(object):
    def isNumber(self, s: str):
        seen_digit, seen_dot, seen_exponent = [False, False, False]
        for i in range(len(s)):
            if s[i].isdigit():
                seen_digit = True
            elif s[i] in {"+", "-"}:
                if i != 0 and s[i - 1] not in {"E", "e"}:
                    return False
            elif s[i] == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif s[i] in {"e", "E"}:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            else:
                return False

        if not seen_digit:
            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isNumber("0089")
    assert solution.isNumber("-0.1")
    assert solution.isNumber("+3.14")
    assert solution.isNumber("4.")
    assert solution.isNumber("-.9")
    assert solution.isNumber("2e10")
    assert solution.isNumber("-90E3")
    assert solution.isNumber("3e+7")
    assert solution.isNumber("+6e-1")
    assert solution.isNumber("53.5e93")
    assert solution.isNumber("-123.456e789")
    assert not solution.isNumber("abc")
    assert not solution.isNumber("1a")
    assert not solution.isNumber("1e")
    assert not solution.isNumber("e3")
    assert not solution.isNumber("99e2.5")
    assert not solution.isNumber("--6")
    assert not solution.isNumber("-+3")
    assert not solution.isNumber("95a54e53")
