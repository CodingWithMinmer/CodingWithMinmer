# VARIANT: the abbreviation can contain the '*' sybnol which acts as a wildcard
# that can match anywhere from 0 to n characters in the base word
# SOURCE: https://youtu.be/ALDB1fi65U8?si=s9Noj_9_lt4cw63Z&t=877
class Solution_408_Variant:
    def recurse(self, word: str, abbr: str, w: int, a: int) -> bool:
        if w == len(word) and a == len(abbr):
            return True
        elif w != len(word) and a == len(abbr):
            return False
        elif w == len(word) and a < len(abbr):
            while a < len(abbr):
                if abbr[a] != "*":
                    return False
                a += 1
            return True
        elif word[w] == abbr[a]:
            return self.recurse(word, abbr, w + 1, a + 1)
        elif abbr[a] == "0":
            return False
        elif abbr[a].isnumeric():
            skip = 0
            while a < len(abbr) and abbr[a].isnumeric():
                skip = skip * 10 + int(abbr[a])
                a += 1
            w += skip
            if w > len(word):
                return False
            return self.recurse(word, abbr, w, a)
        elif abbr[a] == "*":
            return self.recurse(word, abbr, w + 1, a) or self.recurse(
                word, abbr, w, a + 1
            )

        return False

    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        """
        Time Complexity: O(2^(A+W))
        Space Complexity: O(W)

        """
        return self.recurse(word, abbr, 0, 0)


if __name__ == "__main__":
    assert Solution_408_Variant().valid_word_abbreviation("abc", "*") == True
    assert (
        Solution_408_Variant().valid_word_abbreviation("tadpoletech", "*pole*hie")
        == False
    )
    assert (
        Solution_408_Variant().valid_word_abbreviation("minmerhq", "mi*e2q***") == True
    )
    assert Solution_408_Variant().valid_word_abbreviation("tadpoles", "ta3l2") == True
    assert Solution_408_Variant().valid_word_abbreviation("xyzabc", "xy023") == False
    assert (
        Solution_408_Variant().valid_word_abbreviation("summerseasonisbest", "su12b5")
        == False
    )
    assert (
        Solution_408_Variant().valid_word_abbreviation("summerseasonisbest", "su12b3")
        == True
    )
    assert Solution_408_Variant().valid_word_abbreviation("hellzpme", "h2*p*me") == True
    assert Solution_408_Variant().valid_word_abbreviation("test", "tes") == False
    assert Solution_408_Variant().valid_word_abbreviation("test", "tes***") == True
    assert Solution_408_Variant().valid_word_abbreviation("test", "tes***s") == False
