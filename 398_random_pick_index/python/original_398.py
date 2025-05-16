from collections import Counter
from random import randint
from typing import List


# LC: https://leetcode.com/problems/random-pick-index/
# SOURCE: https://youtu.be/paCJBO-yi9Q?si=sc6eE6wz_wW_ylar
class Solution_398:
    def __init__(self, nums: List[int]) -> None:
        self.num_to_indices = {}
        for i, num in enumerate(nums):
            self.num_to_indices.setdefault(num, []).append(i)

    def pick(self, target: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if target in self.num_to_indices:
            n = len(self.num_to_indices[target])
        else:
            return -1
        r = randint(0, n - 1)
        return self.num_to_indices[target][r]


if __name__ == "__main__":

    def test(nums: List[int], target: int) -> dict[int:int]:
        iterations = 10**5
        picked_indices = Counter(
            [Solution_398(nums).pick(target) for _ in range(iterations)]
        ).items()
        probabilities = {k: v * 100.0 / iterations for k, v in picked_indices}

        return probabilities

    nums = [5, 5, 1, 5, 2, 1, 5]
    # tests reveal equal probability of picking each index for the
    # respective `target`
    print(f"Probabilities for indices of 1345: {test(nums, target=1345)}")
    print(f"Probabilities for indices of 5: {test(nums, target=5)}")
    print(f"Probabilities for indices of 2: {test(nums, target=2)}")
    print(f"Probabilities for indices of 1: {test(nums, target=1)}")
