import pytest


class Solution_408_Variant:
    def validWordAbbreviation(self, word: str, pattern: str) -> bool:
    
        w=0
        a=0
        m,n = len(word),len(pattern)
        def recurse(w,a):
            if w == m and a == n: return True
            if w < m and a == n: return False
            if w == m and a < n:
                for i in range(a,n):
                    if pattern[i] != '*':
                        return False
                return True
            
            if pattern[a].isdigit():
                num = 0
                # print(aa < n and pattern.isdigit())
                while a < n and pattern[a].isdigit():
                    num = num*10 + int(pattern[a])
                    a+=1
                w += num
                if w > m: return False
                return recurse(w,a)

            if  pattern[a] == '*':
                return recurse(w+1,a) or recurse(w,a+1)
            
            if word[w] == pattern[a]:
                return recurse(w+1,a+1)
            return False
        return recurse(w,a)
        

# --- Tests for ValidWordAbbreviation_WildcardVariant ---

if __name__ == "__main__":
    print("Running all Valid Word Abbreviation (Wildcard Variant) tests...")

    s = Solution_408_Variant()

    # --- Test Suite: Original LC408 Testcases (Only Digits) ---
    print("\n--- Test Suite: Original LC408 Testcases (Only Digits) ---")
    assert s.validWordAbbreviation("internationalization", "i12iz4n"), "Failed: OnlyDigits - i12iz4n"
    assert not s.validWordAbbreviation("apple", "a2e"), "Failed: OnlyDigits - a2e"
    assert s.validWordAbbreviation("unbelievable", "11e"), "Failed: OnlyDigits - 11e"
    assert s.validWordAbbreviation("internationalization", "19n"), "Failed: OnlyDigits - 19n"
    assert s.validWordAbbreviation("representation", "14"), "Failed: OnlyDigits - 14"
    assert s.validWordAbbreviation("acknowledgment", "14"), "Failed: OnlyDigits - 14 (acknowledgment)"
    assert s.validWordAbbreviation("mississippi", "11"), "Failed: OnlyDigits - 11 (mississippi)"
    print("All 'Only Digits' tests passed.")

    # --- Test Suite: Only Alphabet (Exact Match) ---
    print("\n--- Test Suite: Only Alphabet (Exact Match) ---")
    assert s.validWordAbbreviation("abcdefg", "abcdefg"), "Failed: OnlyAlphabet - Exact True"
    assert not s.validWordAbbreviation("abcdefg", "xyz"), "Failed: OnlyAlphabet - Exact False (xyz)"
    assert not s.validWordAbbreviation("aa", "a"), "Failed: OnlyAlphabet - Exact False (aa, a)"
    print("All 'Only Alphabet' tests passed.")

    # --- Test Suite: Both Empty Strings ---
    print("\n--- Test Suite: Empty Strings ---")
    assert s.validWordAbbreviation("", ""), "Failed: Empty Strings"
    print("All 'Empty Strings' tests passed.")

    # --- Test Suite: Wildcard Matches ---
    print("\n--- Test Suite: Wildcard Matches ---")
    assert s.validWordAbbreviation("adcbdk", "*a*bdk"), "Failed: Wildcard - *a*bdk"
    assert s.validWordAbbreviation("aa", "*"), "Failed: Wildcard - aa (*)"
    assert s.validWordAbbreviation("abc", "ab****c"), "Failed: Wildcard - LotsOfWildCards"
    assert not s.validWordAbbreviation("abc", "ab****c**d"), "Failed: Wildcard - Pattern Left, Not All Wildcards"
    assert s.validWordAbbreviation("abc", "ab****c*****"), "Failed: Wildcard - Pattern Left, All Wildcards"
    print("All 'Wildcard Matches' tests passed.")

    # --- Test Suite: Skips Longer/To End of Word ---
    print("\n--- Test Suite: Skips ---")
    assert not s.validWordAbbreviation("testing", "t32g"), "Failed: Skips - Longer than word (t32g)"
    assert not s.validWordAbbreviation("testing", "t7"), "Failed: Skips - Longer than word (t7)"
    assert s.validWordAbbreviation("testing", "t6"), "Failed: Skips - To End of Word"
    print("All 'Skips' tests passed.")

    # --- Test Suite: Mixed Wildcard and Digits ---
    print("\n--- Test Suite: Wildcard and Digits ---")
    assert s.validWordAbbreviation("validation", "v2i*ion"), "Failed: Mixed - v2i*ion"
    assert s.validWordAbbreviation("zzzzzzzzzzp", "*p"), "Failed: Mixed - *p"
    assert s.validWordAbbreviation("zzzzzzzzzzp", "*"), "Failed: Mixed - *"
    assert s.validWordAbbreviation("international", "i*n*l"), "Failed: Mixed - i*n*l"
    assert s.validWordAbbreviation("developer", "d*ve*r"), "Failed: Mixed - d*ve*r"
    assert s.validWordAbbreviation("elephant", "e3h*"), "Failed: Mixed - e3h*"
    assert s.validWordAbbreviation("mechanical", "m*4l"), "Failed: Mixed - m*4l"
    assert s.validWordAbbreviation("dictionary", "d*o3y"), "Failed: Mixed - d*o3y"
    assert s.validWordAbbreviation("automation", "a2o*ion"), "Failed: Mixed - a2o*ion"
    assert s.validWordAbbreviation("something", "s*m*hing"), "Failed: Mixed - s*m*hing"
    assert s.validWordAbbreviation("multiverse", "m*5e"), "Failed: Mixed - m*5e"
    assert s.validWordAbbreviation("extraordinary", "e*5*ary"), "Failed: Mixed - e*5*ary"
    assert s.validWordAbbreviation("mathematical", "m*3*3cal"), "Failed: Mixed - m*3*3cal"
    assert s.validWordAbbreviation("unbelievable", "u1b*4*able"), "Failed: Mixed - u1b*4*able"
    assert s.validWordAbbreviation("communication", "c2m*4*ion"), "Failed: Mixed - c2m*4*ion"
    assert s.validWordAbbreviation("programming", "p*6*ing"), "Failed: Mixed - p*6*ing"
    assert s.validWordAbbreviation("subterranean", "s*4*5n"), "Failed: Mixed - s*4*5n"
    assert s.validWordAbbreviation("revolutionary", "r3l*6y"), "Failed: Mixed - r3l*6y"
    assert s.validWordAbbreviation("balloon", "b2l2n"), "Failed: Mixed - b2l2n"
    assert s.validWordAbbreviation("alphabet", "a1p1a1e1"), "Failed: Mixed - a1p1a1e1"
    assert s.validWordAbbreviation("elephant", "e1e1h*"), "Failed: Mixed - e1e1h*"
    assert s.validWordAbbreviation("subterranean", "s*4*6n"), "Failed: Mixed - s*4*6n"
    assert s.validWordAbbreviation("unbelievable", "u1b*6*ble"), "Failed: Mixed - u1b*6*ble"
    assert not s.validWordAbbreviation("transformation", "t2a*5*ion"), "Failed: Mixed - transformation (False)"
    assert not s.validWordAbbreviation("zzzzzzzzzzp", "*a"), "Failed: Mixed - zzzzzzzzzzp (*a)"
    assert not s.validWordAbbreviation("automation", "a4t*n"), "Failed: Mixed - automation (False)"
    assert not s.validWordAbbreviation("dictionary", "d*o4y"), "Failed: Mixed - dictionary (False)"
    assert not s.validWordAbbreviation("elephant", "e3z*"), "Failed: Mixed - elephant (False)"
    assert not s.validWordAbbreviation("validation", "v2z*ion"), "Failed: Mixed - validation (False)"
    assert not s.validWordAbbreviation("submarine", "s*b*m"), "Failed: Mixed - submarine (False)"
    assert not s.validWordAbbreviation("international", "i*o4l"), "Failed: Mixed - international (False)"
    assert not s.validWordAbbreviation("extraordinary", "e*5*zary"), "Failed: Mixed - extraordinary (False)"
    assert not s.validWordAbbreviation("mathematical", "m*3*4cals"), "Failed: Mixed - mathematical (False)"
    assert not s.validWordAbbreviation("transformation", "t2a*6tion"), "Failed: Mixed - transformation (False 2)"
    assert not s.validWordAbbreviation("communication", "c2m*3*ition"), "Failed: Mixed - communication (False)"
    assert not s.validWordAbbreviation("programming", "p*5*ingg"), "Failed: Mixed - programming (False)"
    assert not s.validWordAbbreviation("revolutionary", "r3v*7y"), "Failed: Mixed - revolutionary (False)"
    assert not s.validWordAbbreviation("balloon", "b12n"), "Failed: Mixed - balloon (False)"
    assert not s.validWordAbbreviation("alphabet", "a1p1a2e1"), "Failed: Mixed - alphabet (False)"
    assert not s.validWordAbbreviation("elephant", "e1e1z*"), "Failed: Mixed - elephant (False 2)"
    print("All 'Wildcard and Digits' tests passed.")

    # --- Test Suite: Multi-Digits and Wildcards ---
    print("\n--- Test Suite: Multi-Digits and Wildcards ---")
    assert s.validWordAbbreviation("unbelievable", "11*e"), "Failed: Multi-Digits - 11*e"
    assert s.validWordAbbreviation("internationalization", "10*i5n"), "Failed: Multi-Digits - 10*i5n"
    assert s.validWordAbbreviation("acknowledgment", "5*3*t"), "Failed: Multi-Digits - 5*3*t"
    assert s.validWordAbbreviation("abbreviation", "1b10*"), "Failed: Multi-Digits - 1b10*"
    assert s.validWordAbbreviation("representation", "*14"), "Failed: Multi-Digits - *14"
    assert s.validWordAbbreviation("extraordinary", "5*6*"), "Failed: Multi-Digits - 5*6*"
    assert s.validWordAbbreviation("multidimensionality", "4*6*5y"), "Failed: Multi-Digits - 4*6*5y"
    assert s.validWordAbbreviation("predetermination", "3*d*10"), "Failed: Multi-Digits - 3*d*10"
    print("All 'Multi-Digits and Wildcards' tests passed.")

    # --- Test Suite: TLE Specific Case ---
    print("\n--- Test Suite: TLE Specific Case ---")
    assert s.validWordAbbreviation("bbbbbbbabbabbabaaabba", "bb*ab**ba*bb***bba"), "Failed: TLE case"
    print("TLE test case passed (ensure your solution is efficient!).")

    print("\nAll tests completed successfully!")