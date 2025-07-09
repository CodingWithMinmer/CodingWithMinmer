from collections import Counter
from random import randint
from typing import List


# VARIANT: What if you had to use reservoir sampling to randomly sample K
#          numbers without replacement probability?
# SOURCE: https://youtu.be/paCJBO-yi9Q?si=t9CACAg2TC4YFOEw&t=371
class Solution_398_First_Variant:
    def sample_k_numbers(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        result = []
        for i in range(k):
            result.append(nums[i])

        for i in range(k, len(nums)):
            r = randint(0, i)
            if r < k:
                result[r] = nums[i]

        return result


if __name__ == "__main__":

    def test(nums: List[int], k: int) -> dict[int:int]:
        iterations = 10**5
        result = []
        for _ in range(iterations):
            result += Solution_398_First_Variant().sample_k_numbers(nums, k)
        picked_indices = Counter(result).items()
        probabilities = {
            key: round(v * 100.0 / k / iterations, 2) for key, v in picked_indices
        }

        return probabilities

    nums = [6, 8, 2, 1, 3, 10, 4]
    # testing reveals equal probability of picking each number
    print(test(nums, 3))
