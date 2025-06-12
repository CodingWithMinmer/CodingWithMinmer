def validPalindrome(s: str) -> bool:
    def check_remaining(s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            return False

        return True

    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue

        return check_remaining(s, left, right - 1) or check_remaining(
            s, left + 1, right
        )

    return True
