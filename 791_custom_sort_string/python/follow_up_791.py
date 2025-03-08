class Solution:
    def customSortString(self, order: list[str], s: str) -> str:
        # order is list of str (just chars)
        freq = [0 for _ in range(26)]
        result = []
        for char in order:
            if char in freq:
                result.extend([char] * freq[ord(char) - ord("a")])
                freq[ord(char) - ord("a")] = 0

        for remaining_char, f in freq.items():
            if f > 0:
                result += [remaining_char] * f

        return "".join(result)
