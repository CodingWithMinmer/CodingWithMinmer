from typing import List


# VARIANT: What if you had to solve the OG problem without any extra space complexity?
# SOURCE: https://youtu.be/5YMKRfFnLEA?si=fBGWVjhJ74zAqbGu&t=1092
def min_remove_to_make_valid_variant(s: List[str]) -> str:
    """
    NB: given that 'str' is immutable in python and does not support item
        assignment, in order to perform the changes in-place the input must be
        given as a mutable set of items, hence, the input here is a list

    Time Complexity: O(2n) = O(n)
    Space Complexity: O(1)
    """
    extra_opens = total_opens = 0
    j = 0
    for ch in s:
        if ch == "(":
            extra_opens += 1
            total_opens += 1
        elif ch == ")":
            if extra_opens == 0:
                continue
            extra_opens -= 1
        s[j] = ch
        j += 1

    open_keep = total_opens - extra_opens
    length, j = j, 0
    for i in range(length):
        ch = s[i]
        if ch == "(":
            open_keep -= 1
            if open_keep < 0:
                continue
        s[j] = ch
        j += 1

    return "".join(s[:j])


if __name__ == "__main__":
    assert min_remove_to_make_valid_variant(list("))((ab()c)(")) == "((ab)c)"
    assert min_remove_to_make_valid_variant(list("((ab((()))c)(")) == "((ab(()))c)"
