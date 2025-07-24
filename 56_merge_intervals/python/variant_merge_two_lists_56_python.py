from typing import List


def try_merge(result: List[List[int]], curr_interval: List[int]):
    if not result or curr_interval[0] > result[-1][1]:
        result.append(curr_interval)
    else:
        result[-1][1] = max(curr_interval[1], result[-1][1])


def merge_2_interval_lists_56_variant_python(
    A: List[List[int]], B: List[List[int]]
) -> List[List[int]]:
    result = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i][0] <= B[j][0]:
            curr_interval = A[i]
            i += 1
        else:
            curr_interval = B[j]
            j += 1

        try_merge(result, curr_interval)

    if i < len(A):
        while i < len(A):
            try_merge(result, A[i])
            i += 1
    else:
        while j < len(B):
            try_merge(result, B[j])
            j += 1

    return result


if __name__ == "__main__":
    A = [[3, 11], [14, 15], [18, 22], [23, 24], [25, 26]]
    B = [[2, 8], [13, 20]]
    expected = [[2, 11], [13, 22], [23, 24], [25, 26]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

    A = []
    B = [[2, 8], [13, 20]]
    expected = [[2, 8], [13, 20]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

    A = [[1, 5], [10, 15], [20, 25]]
    B = [[5, 10], [15, 20]]
    expected = [[1, 25]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

    A = [[1, 5], [11, 15], [21, 25]]
    B = [[6, 10], [16, 20]]
    expected = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)
