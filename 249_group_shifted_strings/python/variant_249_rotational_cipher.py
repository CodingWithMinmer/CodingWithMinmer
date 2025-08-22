# VARIANT: What if you had to right shift a given string by a given
#          rotational factor?
# SOURCE: https://youtu.be/uEOaAs-KY3M?si=058UUgbKtUjImD8m&t=1245
class Solution_249_Variant:
    def rotational_cipher(self, string: str, rotational_factor: int) -> str:
        """
        Time Complexity: O(L), where: L = len(string)
        Space Complexity: O(1)
        """
        if not rotational_factor:
            return string

        result = ""
        for ch in string:
            if ch.islower():
                result += chr((ord(ch) - ord("a") + rotational_factor) % 26 + ord("a"))
            elif ch.isupper():
                result += chr((ord(ch) - ord("A") + rotational_factor) % 26 + ord("A"))
            elif ch.isdigit():
                result += chr((ord(ch) - ord("0") + rotational_factor) % 10 + ord("0"))
            else:
                result += ch

        return result


if __name__ == "__main__":
    assert (
        Solution_249_Variant().rotational_cipher(
            string="minMerz-894", rotational_factor=5
        )
        == "rnsRjwe-349"
    )
    assert (
        Solution_249_Variant().rotational_cipher(
            string="XYZ_abo_112288", rotational_factor=39
        )
        == "KLM_nob_001177"
    )
    assert (
        Solution_249_Variant().rotational_cipher(string="89-yfZZ@", rotational_factor=3)
        == "12-biCC@"
    )
