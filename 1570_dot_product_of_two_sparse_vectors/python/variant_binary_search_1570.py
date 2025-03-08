from collections import namedtuple
from bisect import bisect_left


class SparseVectorVariant:
    def __init__(self, nums: list[int]):
        Pair = namedtuple("Pair", "index value")
        self.pairs = [
            Pair(index, value) for index, value in enumerate(nums) if value != 0
        ]

    def dotProduct(self, vec: "SparseVectorVariant") -> int:
        result = 0
        shorter, longer = (
            (self.pairs, vec.pairs)
            if len(self.pairs) < len(vec.pairs)
            else (vec.pairs, self.pairs)
        )
        for pair in shorter:
            matched_idx = bisect_left(longer, (pair.index,))
            if matched_idx >= len(longer) or longer[matched_idx].index != pair.index:
                continue
            result += pair.value * longer[matched_idx].value

        return result
