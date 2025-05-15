# LC: https://leetcode.com/problems/kth-missing-positive-number/
# SOURCE: https://youtu.be/9L2jd7mSeV8?si=BfUBm-Dj2okY2dU4
def find_kth_positive(arr: list[int], k: int) -> int:
    """
    Time Complexity: O(log N)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        missing = arr[mid] - 1 - mid

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1

    return left + k


if __name__ == "__main__":
    assert find_kth_positive(arr=[4, 7, 8, 9, 11], k=6) == 10
    assert find_kth_positive(arr=[4, 7, 8, 9, 11], k=8) == 13
    assert find_kth_positive(arr=[2, 3, 4, 7, 11], k=5) == 9
    assert find_kth_positive(arr=[1, 2, 3, 4], k=2) == 6
    assert find_kth_positive(arr=[3, 5, 6, 10, 13], k=5) == 8
    assert find_kth_positive(arr=[4, 7, 9, 10], k=1) == 1
    assert find_kth_positive(arr=[4, 7, 9, 10], k=3) == 3
    assert find_kth_positive(arr=[1, 2, 4], k=3) == 6
    assert find_kth_positive(arr=[4, 8, 10, 11, 12, 13, 18], k=7) == 9
