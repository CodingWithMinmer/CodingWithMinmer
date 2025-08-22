from typing import List


def longestOnes_second_variant_1004_python(year: List[bool], pto: int) -> int:
    max_vacation = 0
    left = 0
    for right in range(len(year)):
        if not year[right]:
            pto -= 1

        while pto < 0:
            if not year[left]:
                pto += 1
            left += 1

        max_vacation = max(max_vacation, right - left + 1)
    return max_vacation


if __name__ == "__main__":
    year = [False, True, True, False, False, True, False]
    pto = 2
    assert longestOnes_second_variant_1004_python(year, pto) == 5

    year = [False, False, True, True, False, False, False]
    pto = 0
    assert longestOnes_second_variant_1004_python(year, pto) == 2

    year = [False, False, True, True, False, False, False]
    pto = 5
    assert longestOnes_second_variant_1004_python(year, pto) == 7

    year = [False, False, True, True, False, False, False]
    pto = 10
    assert longestOnes_second_variant_1004_python(year, pto) == 7

    year = [True, True, True, True, True, True, True]
    pto = 0
    assert longestOnes_second_variant_1004_python(year, pto) == 7

    year = [False, True, False, False, False, True, False, True]
    pto = 1
    assert longestOnes_second_variant_1004_python(year, pto) == 3
