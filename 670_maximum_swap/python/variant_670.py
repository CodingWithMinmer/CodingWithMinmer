class Solution:
    def buildSecondLargestNumber(self, num: list[int]) -> list[int]:
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

        return num


if __name__ == "__main__":
    solution = Solution()
    assert solution.buildSecondLargestNumber([2, 7, 3, 6]) == [7, 6, 2, 3]
    assert solution.buildSecondLargestNumber([1, 2, 1, 1, 1]) == [1, 2, 1, 1, 1]
