class Solution:
    def customSortString(self, order: list[str], s: str) -> str:
        freqs = [0] * 26
        for ch in s:
            freqs[ord(ch) - ord("a")] += 1

        result = ""
        for ch in order:
            result += ch * freqs[ord(ch) - ord("a")]
            freqs[ord(ch) - ord("a")] = 0

        for i in range(26):
            result += chr(i + ord("a")) * freqs[i]

        return result
