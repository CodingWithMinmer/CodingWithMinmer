from typing import List

# LC: https://leetcode.com/problems/group-shifted-strings/
# SOURCE: https://youtu.be/uEOaAs-KY3M?si=058UUgbKtUjImD8m
class Solution_249:
    def shift(self, string: str):
        key = ""
        left_shifts = ord(string[0]) - ord("a")
        for ch in string:
            encoded_char = ord(ch) - left_shifts + 26
            if encoded_char > 122:
                encoded_char -= 26

            key += chr(encoded_char)
        return key

    def group_strings(self, strings: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(N * L)
        Space Complexity: O(N * L), where:
            N = len(strings)
            L = numner of letters
        """
        shifted_to_original = {}
        for string in strings:
            shifted = self.shift(string)
            if shifted in shifted_to_original:
                shifted_to_original[shifted].append(string)
            else:
                shifted_to_original[shifted] = [string]

        return list(shifted_to_original.values())


if __name__ == "__main__":
    assert Solution_249().group_strings(
        ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    ) == [
        ["abc", "bcd", "xyz"],
        ["acef"],
        ["az", "ba"],
        ["a", "z"],
    ]

    assert Solution_249().group_strings(["a"]) == [["a"]]

    assert Solution_249().group_strings(["fd", "ad", "ca", "be"]) == [
        ["fd", "ca"],
        ["ad", "be"],
    ]
