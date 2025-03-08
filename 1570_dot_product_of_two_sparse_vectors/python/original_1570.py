from collections import namedtuple

class SparseVector:
    def __init__(self, nums: list[int]):
        Pair = namedtuple("Pair", "index value")
        self.pairs = [Pair(index, value) for index, value in enumerate(nums) if value != 0]

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        i, j = 0, 0
        while i < len(self.pairs) and j < len(vec.pairs):
            if self.pairs[i].index == vec.pairs[j].index:
                result += self.pairs[i].value * vec.pairs[j].value
                i += 1
                j += 1
            elif self.pairs[i].index < vec.pairs[j].index:
                i += 1
            else:
                j += 1
        return result