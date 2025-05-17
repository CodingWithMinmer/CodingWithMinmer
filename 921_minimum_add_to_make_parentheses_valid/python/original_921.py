class Solution:
    def minimumAddToMakeValid(self, s: str) -> int:
        extra_right = 0
        left_open = 0
        for c in s:
            if c == "(":
                left_open += 1
            elif c == ")":
                if left_open == 0:
                    extra_right += 1
                    continue
                left_open -= 1
        return left_open + extra_right
