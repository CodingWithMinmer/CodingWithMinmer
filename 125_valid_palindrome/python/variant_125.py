class Solution:
    def isPalindrome(self, s: str, include: list[str]) -> bool:
        include_set = set(include)
        left, right = 0, len(s) - 1
        while left < right:
            while s[left] not in include_set and left < right:
                left += 1
            while s[right] not in include_set and left < right:
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    assert not solution.isPalindrome("racecarX", ["r", "X"])
    assert solution.isPalindrome("Yo, banana boY!", ["Y", "o", "b", "a", "n"])
