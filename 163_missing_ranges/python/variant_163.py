class Solution:
    def findMissingRangesVariant(self, nums, lower, upper):
        curr_lower = lower
        missing_ranges = []
        nums.append(upper + 1)

        for num in nums:
            if num - curr_lower > 2:
                missing_ranges.append(f"{curr_lower}-{num - 1}")
            elif num - curr_lower == 2:
                missing_ranges.append(str(curr_lower))
                missing_ranges.append(str(curr_lower + 1))
            elif num - curr_lower == 1:
                missing_ranges.append(str(curr_lower))

            curr_lower = num + 1

        return missing_ranges


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 2, 87) == [
        "2-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-87",
    ]

    solution = Solution()
    # Empty vector cases
    assert solution.findMissingRangesVariant([], 0, 0) == ["0"]
    assert solution.findMissingRangesVariant([], 5, 35) == ["5-35"]
    assert solution.findMissingRangesVariant([], 0, 35) == ["0-35"]

    # Valid cases
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 2, 87) == [
        "2-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-87",
    ]

    # Upper bound with dash
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 800) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-800",
    ]

    # Upper bound with one missing number
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 21) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
    ]

    # Upper bound with two missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 22) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
        "22",
    ]

    # Upper bound with no missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 20) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # No missing ranges with one element
    assert solution.findMissingRangesVariant([0], 0, 0) == []

    # No missing ranges with one element V2
    assert solution.findMissingRangesVariant([6], 6, 6) == []

    # Lower bound with dash
    assert solution.findMissingRangesVariant([0, 8, 9, 15, 16, 18, 20], 0, 20) == [
        "1-7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with no missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 5, 20) == [
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with two missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 3, 20) == [
        "3",
        "4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with one missing number
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 4, 20) == [
        "4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Upper bound with no dash
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 5, 22) == [
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
        "22",
    ]

    # One element with two ranges missing
    assert solution.findMissingRangesVariant([10], 5, 22) == ["5-9", "11-22"]
