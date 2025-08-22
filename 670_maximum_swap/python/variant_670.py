class Solution:
    def buildSecondLargestNumber(self, num: list[int]) -> list[int]:
        if not num or len(num) == 1:
            return []

        freqs = [0 for _ in range(10)]
        for digit in num:
            freqs[digit] += 1

        largest_num = []
        for i in range(9, -1, -1):
            for _ in range(freqs[i]):
                largest_num.append(i)

        for i in range(len(largest_num) - 1, 0, -1):
            if largest_num[i - 1] != largest_num[i]:
                largest_num[i - 1], largest_num[i] = largest_num[i], largest_num[i - 1]
                return largest_num

        return []


if __name__ == "__main__":
    solution = Solution()
    assert solution.buildSecondLargestNumber([2, 7, 3, 6]) == [7, 6, 2, 3]
    assert solution.buildSecondLargestNumber([1, 2, 1, 1, 1]) == [1, 2, 1, 1, 1]

    # MaximumSwap_Variant_BuildSecondLargest True
    assert solution.buildSecondLargestNumber([]) == []
    assert solution.buildSecondLargestNumber([1]) == []
    assert solution.buildSecondLargestNumber([2]) == []
    assert solution.buildSecondLargestNumber([3]) == []
    assert solution.buildSecondLargestNumber([4]) == []
    assert solution.buildSecondLargestNumber([5]) == []
    assert solution.buildSecondLargestNumber([6]) == []
    assert solution.buildSecondLargestNumber([7]) == []
    assert solution.buildSecondLargestNumber([8]) == []
    assert solution.buildSecondLargestNumber([9]) == []
    assert solution.buildSecondLargestNumber([0]) == []

    # Distinct Digits And One Swap
    assert solution.buildSecondLargestNumber([2, 7, 3, 6]) == [7, 6, 2, 3]
    assert solution.buildSecondLargestNumber([2, 3, 4, 1, 8]) == [8, 4, 3, 1, 2]

    # All Duplicate Digits Cannot Build Second Largest
    assert solution.buildSecondLargestNumber([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == []
    assert solution.buildSecondLargestNumber([2, 2]) == []
    assert solution.buildSecondLargestNumber([0, 0, 0, 0, 0, 0]) == []

    # Duplicate Digits And Looped Swap
    assert solution.buildSecondLargestNumber([1, 2, 1, 1, 1]) == [1, 2, 1, 1, 1]
    assert solution.buildSecondLargestNumber([5, 9, 7, 6, 6, 3, 9, 6, 6]) == [
        9,
        9,
        7,
        6,
        6,
        6,
        6,
        3,
        5,
    ]
    assert solution.buildSecondLargestNumber([5, 9, 7, 6, 6, 3, 9, 6, 6, 3, 3]) == [
        9,
        9,
        7,
        6,
        6,
        6,
        6,
        3,
        5,
        3,
        3,
    ]
    assert solution.buildSecondLargestNumber([4, 4, 4, 4, 9, 9, 9, 9, 9]) == [
        9,
        9,
        9,
        9,
        4,
        9,
        4,
        4,
        4,
    ]

    # Zeroes
    assert solution.buildSecondLargestNumber([0, 0, 0, 0, 0, 6, 0]) == [
        0,
        6,
        0,
        0,
        0,
        0,
        0,
    ]
    assert solution.buildSecondLargestNumber([0, 0, 1, 2, 3, 3]) == [3, 3, 2, 0, 1, 0]
    assert solution.buildSecondLargestNumber([0, 0, 8, 4, 9, 9, 6, 7]) == [
        9,
        9,
        8,
        7,
        6,
        0,
        4,
        0,
    ]
