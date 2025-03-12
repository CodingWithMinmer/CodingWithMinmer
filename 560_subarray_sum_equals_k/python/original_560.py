from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count, cumulative = 0, 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        for num in nums:
            cumulative += num
            if (cumulative - k) in prefix_sums:
                count += prefix_sums[cumulative - k]
            prefix_sums[cumulative] += 1
        return count
