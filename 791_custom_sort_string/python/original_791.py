from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        result = []
        for char in order:
            if char in freq:
                result.extend([char] * freq[char])
                freq[char] = 0

        for remaining_char, f in freq.items():
            if f > 0:
                result += [remaining_char] * f

        return "".join(result)
