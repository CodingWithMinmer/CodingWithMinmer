class Solution:
    def subarraySumExists(self, nums: list[int], k: int) -> bool:
        count, cumulative = 0, 0
        prefix_sums = set([0])
        for num in nums:
            cumulative += num
            if (cumulative - k) in prefix_sums:
                return True
            prefix_sums.add(cumulative)
        return count


if __name__ == "__main__":
    solution = Solution()
    assert solution.subarraySumExists([1, 1, 1], 2)
    assert not solution.subarraySumExists([1, 4, 7], 3)
