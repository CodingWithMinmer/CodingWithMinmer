def min_remove_to_make_valid(s: str) -> str:
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
            if  extra_opens == 0:
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
    assert min_remove_to_make_valid("))((ab()c)(") == "((ab)c)"
    assert min_remove_to_make_valid("((ab((()))c)(") == "((ab(()))c)"