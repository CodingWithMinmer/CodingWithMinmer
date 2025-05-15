# ARIANT: What if you had to return the Kth missing positive number from the
#         leftmost element?
# SOURCE: https://youtu.be/9L2jd7mSeV8?si=5NHIRaWIHFUETdef&t=770
def find_kth_positive_variant(arr: list[int], k: int) -> int:
    """
    Time Complexity: O(log N)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        missing = arr[mid] - arr[0] - mid

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1

    return arr[0] + k + right


if __name__ == "__main__":
    assert find_kth_positive_variant(arr=[4, 7, 8, 9, 11], k=6) == 14
    assert find_kth_positive_variant(arr=[4, 7, 8, 9, 11], k=8) == 16
    assert find_kth_positive_variant(arr=[2, 3, 4, 7, 11], k=5) == 10
    assert find_kth_positive_variant(arr=[1, 2, 3, 4], k=2) == 6
    assert find_kth_positive_variant(arr=[3, 5, 6, 10, 13], k=5) == 11
    assert find_kth_positive_variant(arr=[4, 7, 9, 10], k=1) == 5
    assert find_kth_positive_variant(arr=[4, 7, 9, 10], k=3) == 8
    assert find_kth_positive_variant(arr=[1, 2, 4], k=3) == 6
    assert find_kth_positive_variant(arr=[4, 8, 10, 11, 12, 13, 18], k=7) == 16
