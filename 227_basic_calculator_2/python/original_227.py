# LC: https://leetcode.com/problems/basic-calculator-ii/
# SOURCE: https://youtu.be/G2AZJDkh6_E?si=Tdnv4jX2cvos-vjU
class Solution_227:
    def basic_calculator_two(self, s: str) -> int:
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
            elif op == "-":
                result += prev_num
                prev_num = -curr_num
            elif op == "*":
                prev_num *= curr_num
            elif op == "/":
                prev_num = prev_num // curr_num
            curr_num, op = 0, ch

        return result + prev_num


if __name__ == "__main__":
    assert Solution_227().basic_calculator_two("3+2*2") == 7
    assert Solution_227().basic_calculator_two("3/2") == 1
    assert Solution_227().basic_calculator_two("3+5 / 2") == 5
    assert Solution_227().basic_calculator_two("11 - 6 + 2 + 4 / 2 * 3 / 2 + 5") == 15
    assert Solution_227().basic_calculator_two("11 + 2 + 4 * 3 + 5") == 30
    assert Solution_227().basic_calculator_two(" 11+4+2+7 ") == 24
    assert Solution_227().basic_calculator_two(" 3*5 * 2 ") == 30
