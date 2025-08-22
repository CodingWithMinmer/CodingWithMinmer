def remove_all_adjacent_duplicates_variant_1047_python(s):
    letters = []
    for ch in s:
        if not letters:
            letters.append({"val": ch, "freq": 1})
            continue
        if letters[-1]["val"] == ch:
            letters[-1]["freq"] += 1
            continue

        if letters[-1]["freq"] > 1:
            letters.pop()

        if not letters or letters[-1]["val"] != ch:
            letters.append({"val": ch, "freq": 1})
        elif letters[-1]["val"] == ch:
            letters[-1]["freq"] += 1

    if letters and letters[-1]["freq"] > 1:
        letters.pop()

    result = "".join([letter["val"] for letter in letters])
    return result


if __name__ == "__main__":
    s = "azxxxzy"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "ay"

    s = "abbaxx"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aabbccdd"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aaabbaad"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "d"

    s = "abcdefg"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "abcdefg"

    s = "abbcddeff"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "ace"

    s = "abcdeffedcba"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aabccddeeffbbbbbbbbbf"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "f"

    s = "abbbacca"
    # Cannot pick and choose duplicates in the middle to delete first
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "a"
