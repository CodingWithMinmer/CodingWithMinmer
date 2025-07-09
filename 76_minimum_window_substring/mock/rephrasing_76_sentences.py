from typing import List
from collections import Counter, defaultdict

class Solution:
    def findSmallestSubstring(self, s, w):
        target_freq = Counter(w)
        curr_freq = defaultdict(int)
        need_matches = len(target_freq)
        curr_matches = 0

        result = ()
        min_len = float('inf')
        left = 0
        for right in range(len(s)):
            char = s[right]
            curr_freq[char] += 1

            if char in target_freq and curr_freq[char] == target_freq[char]:
                curr_matches += 1

            while curr_matches == need_matches:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = (left, right)

                left_char = s[left]
                curr_freq[left_char] -= 1
                if left_char in target_freq and \
                    curr_freq[left_char] < target_freq[left_char]:
                    curr_matches -= 1
                left += 1

        if not result:
            return ""
        start, end = result
        return " ".join(s[start:end + 1])
