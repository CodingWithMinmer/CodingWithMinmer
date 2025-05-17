# LC: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# SOURCE: https://www.youtube.com/watch?v=5YMKRfFnLEA
class Solution_1249:
    def min_remove_to_make_valid(self, s: str) -> str:
        """
        Time Complexity: O(2n) = O(n)
        Space Complexity: O(2n) = O(n)
        """
        extra_opens = total_opens = 0
        first_pass = []
        for ch in s:
            if ch == "(":
                extra_opens += 1
                total_opens += 1
            elif ch == ")":
                if extra_opens == 0:
                    continue
                extra_opens -= 1
            first_pass.append(ch)

        open_keep = total_opens - extra_opens
        result = []
        for ch in first_pass:
            if ch == "(":
                open_keep -= 1
                if open_keep < 0:
                    continue
            result.append(ch)

        return "".join(result)


if __name__ == "__main__":
    assert Solution_1249().min_remove_to_make_valid("lee(t(c)o)de)") == "lee(t(c)o)de"
    assert Solution_1249().min_remove_to_make_valid("()") == "()"
    assert Solution_1249().min_remove_to_make_valid("((") == ""
    assert Solution_1249().min_remove_to_make_valid("(()))(") == "(())"
    assert Solution_1249().min_remove_to_make_valid("(())()") == "(())()"
    assert Solution_1249().min_remove_to_make_valid("()())(m()(") == "()()(m)"
    assert Solution_1249().min_remove_to_make_valid(")())m(s)(") == "()m(s)"
    assert Solution_1249().min_remove_to_make_valid("()))x((") == "()x"
    assert Solution_1249().min_remove_to_make_valid("))((ab()c)(") == "((ab)c)"
    assert Solution_1249().min_remove_to_make_valid("((ab((()))c)(") == "((ab(()))c)"
