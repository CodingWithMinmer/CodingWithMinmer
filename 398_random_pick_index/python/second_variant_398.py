from collections import Counter
from random import randint
from typing import List, Dict

import math


# VARIANT: What if you had to use reservoir sampling to pick an index of the
#          maximum value in the array?
# SOURCE: https://youtu.be/paCJBO-yi9Q?si=XTAHLCf3TaHP3748&t=1196
class Solution_398_Second_Variant:
    def sample_max_number(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        max_number = -math.inf
        picked_index, n = -1, 0
        for i in range(len(nums)):
            curr_num = nums[i]
            if curr_num < max_number:
                continue
            elif curr_num > max_number:
                max_number = curr_num
                picked_index = i
                n = 1
            else:
                n += 1
                r = randint(0, n - 1)
                if not r:
                    picked_index = i

        return picked_index


if __name__ == "__main__":

    def test(nums: List[int]) -> Dict[int:int]:
        iterations = 10**5
        result = []
        picked_indices = Counter(
            [
                Solution_398_Second_Variant().sample_max_number(nums)
                for _ in range(iterations)
            ]
        ).items()
        probabilities = {k: round(v * 100.0 / iterations, 2) for k, v in picked_indices}

        return probabilities

    # testing reveals equal probability of picking each index for max. number
    print(test([11, 11, 2, 30, 6, 30, 30, 2, 62, 62]))
    print(test([1, 1, 1, 1, 1]))
