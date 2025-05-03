# LC: https://leetcode.com/problems/valid-word-abbreviation/description/
# SOURCE: https://youtu.be/ALDB1fi65U8?si=GQqghgFIkpY2KPE9
def valid_word_abbreviation(word: str, abbr: str) -> bool:
    """
        Time Complexity: O(A), where A is the length of 'abbr'
        Space Complexity: O(1)
    """

    m, n  = len(word), len(abbr)
    a = w = 0
    while a < n and w < m:
        if word[w] == abbr[a]:
            a += 1
            w += 1
        elif abbr[a] == "0":
            return False
        elif abbr[a].isnumeric():
            skip = 0
            while a < n and abbr[a].isnumeric():
                skip = skip*10 + int(abbr[a])
                a += 1
            w += skip
        else:
            return False

    return a == n and w == m

if __name__ == "__main__":
    assert valid_word_abbreviation("tadpoles", "ta3l2") == True
    assert valid_word_abbreviation("xyzabc", "xy023") == False
    assert valid_word_abbreviation("summerseasonisbest", "su12b5") == False
    assert valid_word_abbreviation("summerseasonisbest", "su12b3") == True
