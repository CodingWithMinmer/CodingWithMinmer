# VARIANT: What if you had to return the number of dominoe pairs that add up to
#          a target?
# SOURCE: https://youtu.be/JRaZN8fOlFk?si=c-7gjrvZ8PNRoHXo&t=1027
def two_sum_second_variant(dominoes: list[list[int, int]], target: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    domino_to_freq = {}
    result = 0
    for a1, a2 in dominoes:
        b1 = target - a1
        b2 = target - a2
        if (b1, b2) in domino_to_freq:
            result += domino_to_freq[(b1, b2)]

        if (a1, a2) in domino_to_freq:
            domino_to_freq[(a1, a2)] += 1
        else:
            domino_to_freq[(a1, a2)] = 1

    return result


if __name__ == "__main__":
    assert (
        two_sum_second_variant(
            [(3, 4), (1, 9), (3, 4), (2, 1), (9, 1), (9, 1), (7, 6), (1, 9)], 10
        )
        == 6
    )
    assert two_sum_second_variant([(1, 8), (12, 5), (12, 5), (12, 5)], 13) == 3
    assert two_sum_second_variant([(1, 8), (12, 5), (12, 5), (12, 5), (1, 8)], 13) == 6
    assert (
        two_sum_second_variant(
            [
                (1, 8),
                (12, 5),
                (12, 5),
                (12, 5),
                (1, 8),
                (12, 5),
            ],
            13,
        )
        == 8
    )
    assert (
        two_sum_second_variant(
            [
                (1, 8),
                (1, 1),
                (5, 4),
                (1, 3),
                (1, 8),
                (12, 5),
            ],
            300,
        )
        == 0
    )
    assert two_sum_second_variant([], 0) == 0
    assert two_sum_second_variant([(1, 2), (3, 2), (1, 2), (3, 2)], 4) == 4
    assert two_sum_second_variant([(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], 0) == 10
    assert two_sum_second_variant([(3, 7)], 10) == 0
    assert two_sum_second_variant([(1, 9), (9, 1), (1, 9), (9, 1)], 10) == 4
    assert two_sum_second_variant([(1, 2), (3, 4), (5, 6)], 10) == 0
    assert two_sum_second_variant([(1, 2), (3, 4), (0, 4)], 1) == 0
    assert (
        two_sum_second_variant(
            [(9, 2), (4, 5), (3, 9), (9, 9), (2, 1), (2, 1), (2, 1)], 6
        )
        == 3
    )
    assert (
        two_sum_second_variant(
            [(0, 9), (9, 0), (9, 0), (0, 9), (2, 1), (0, 9), (0, 9)], 9
        )
        == 8
    )
