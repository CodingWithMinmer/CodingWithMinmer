class Solution(object):
    def isNumber(self, s: str):
        seen_digit, seen_dot = [False, False]
        for i in range(len(s)):
            if s[i].isdigit():
                seen_digit = True
            elif s[i] in {"+", "-"}:
                if i != 0:
                    return False
            elif s[i] == ".":
                if seen_dot:
                    return False
                seen_dot = True
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
    # Exponents not valid anymore
    assert not solution.isNumber("3e+7")
    assert not solution.isNumber("+6e-1")
    assert not solution.isNumber("53.5e93")
    assert not solution.isNumber("-123.456e789")
    assert not solution.isNumber("abc")
    assert not solution.isNumber("2e10")
    assert not solution.isNumber("-90E3")
    assert not solution.isNumber("1a")
    assert not solution.isNumber("1e")
    assert not solution.isNumber("e3")
    assert not solution.isNumber("99e2.5")
    assert not solution.isNumber("--6")
    assert not solution.isNumber("-+3")
    assert not solution.isNumber("95a54e53")
