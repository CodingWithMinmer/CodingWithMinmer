# VARIANT: What if you were given different types of parentheses?
# Each type of parenthesis is balanced independently of the others.
# Otherwise, this might explode into a DP problem and Meta swears to never ask
# Dynamic programming. They'd never lie, right?
# SOURCE: https://youtu.be/5YMKRfFnLEA?si=mH7JdGac4K7xMETP&t=1649
def delete_least_parentheses(s: str) -> str:
    """
    Time Complexity: O(2n) = O(n)
    Space Complexity: O(2n) = O(n)
    """
    mapping = {")": "(", "}": "{", "]": "["}

    extra_opens = {"(": 0, "{": 0, "[": 0}
    total_opens = {"(": 0, "{": 0, "[": 0}
    first_pass = []
    for ch in s:
        if ch in mapping:  # Closing brackets
            if extra_opens[mapping[ch]] == 0:
                continue
            extra_opens[mapping[ch]] -= 1
        elif not ch.isalnum():  # Opening brackets
            extra_opens[ch] += 1
            total_opens[ch] += 1

        first_pass.append(ch)

    open_keep = {}
    for open in total_opens:
        open_keep[open] = total_opens[open] - extra_opens[open]

    result = []
    for ch in first_pass:
        if ch in open_keep:
            open_keep[ch] -= 1
            if open_keep[ch] < 0:
                continue
        result.append(ch)

    return "".join(result)


if __name__ == "__main__":
    assert delete_least_parentheses("[lee(t(c)o))))d[[e)(({{}}}") == "lee(t(c)o)de{{}}"
    assert delete_least_parentheses("(()))))minmer((((()([][[{{}") == "(())minmer()[]{}"
    assert delete_least_parentheses("(()))()") == "(())()"
    assert delete_least_parentheses("{[({)]}}") == "{[({)]}}"
    assert delete_least_parentheses(")))") == ""
    assert delete_least_parentheses("((((") == ""
    assert delete_least_parentheses("({({([}") == "{}"
    assert delete_least_parentheses("([)]") == "([)]"
    assert delete_least_parentheses("([)") == "()"
    assert delete_least_parentheses("))((ab()c)(") == "((ab)c)"
    assert delete_least_parentheses("((ab((()))c)(") == "((ab(()))c)"
