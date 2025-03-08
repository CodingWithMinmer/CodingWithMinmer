class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = [0 for _ in range(26)]

        def get_index(char: str):
            """Returns index in freq"""
            return ord(char) - ord("a")

        for char in s:
            freq[get_index(char)] += 1

        result = []
        for char in order:
            i = get_index(char)
            if freq[i] > 0:
                result.extend([char] * freq[i])
                freq[i] = 0

        for i, f in enumerate(freq):
            if f > 0:
                result += [chr(ord("a") + i)] * f

        return "".join(result)
