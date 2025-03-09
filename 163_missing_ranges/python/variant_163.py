class Solution:
    def findMissingRangesVariant(
        self, nums: list[int], lower: int, upper: int
    ) -> list[str]:
        n = len(nums)
        missing_ranges = []

        def getMissing(lower: int, upper: int) -> list[str]:
            interval_length = upper - lower + 1
            if interval_length == 1:
                return [str(upper)]
            elif interval_length == 2:
                return [str(lower), str(upper)]
            else:
                return [f"{lower}-{upper}"]

        if n == 0:
            missing_ranges.extend(getMissing(lower, upper))

        if lower < nums[0]:
            missing_ranges.extend(getMissing(lower, nums[0] - 1))

        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue
            missing_ranges.extend(getMissing(nums[i] + 1, nums[i + 1] - 1))

        if upper > nums[-1]:
            missing_ranges.extend(getMissing(nums[-1] + 1, upper))

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
