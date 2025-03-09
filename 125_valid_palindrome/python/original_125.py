class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = [c for c in s.lower() if c.isalnum()]
        left, right = 0, len(d) - 1
        while left < right:
            if d[left] != d[right]:
                return False
            left += 1
            right -= 1
        return True
