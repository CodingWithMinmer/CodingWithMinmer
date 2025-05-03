# VARIANT: Implement only addition and multiplication.
# SOURCE: https://youtu.be/G2AZJDkh6_E?si=yMwzH2C5l_lD-u1U&t=1898
def basic_calculator_two_variant(s: str) -> int:
    """
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    curr_num = prev_num = result = 0
    op = "+"
    for ch in s + "+":
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
            continue
        elif ch == " ":
            continue
        elif op == "+":
            result += prev_num
            prev_num = curr_num
        elif op == "*":
            prev_num *= curr_num
        curr_num, op = 0, ch

    return result + prev_num

if __name__ == "__main__":
    assert basic_calculator_two_variant("11 + 2 + 4 * 3 + 5") == 30