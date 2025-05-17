class Solution:
    def minimumAddToMakeValid(self, s: str) -> str:
        result = []
        extra_opens = 0
        for c in s:
            if c == "(":
                extra_opens += 1
            elif c == ")":
                if extra_opens == 0:
                    result.append("(")
                else:
                    extra_opens -= 1
            result.append(c)

        result += [")"] * extra_opens
        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumAddToMakeValid("(())((") == "(())(())"
    assert solution.minimumAddToMakeValid("))(") == "()()()"
    assert solution.minimumAddToMakeValid(")))") == "()()()"
    assert solution.minimumAddToMakeValid("(((") == "((()))"
    assert solution.minimumAddToMakeValid("") == ""
    assert solution.minimumAddToMakeValid("(())") == "(())"
    assert solution.minimumAddToMakeValid(")))(((") == "()()()((()))"
    assert solution.minimumAddToMakeValid("abcxyz") == "abcxyz"
    assert solution.minimumAddToMakeValid("(()()))((") == "(()())()(())"
    assert solution.minimumAddToMakeValid("((a)()))((xyz") == "((a)())()((xyz))"
