from collections import Counter
from random import randint
from typing import List


# LC: https://leetcode.com/problems/random-pick-with-weight/
# SOURCE: https://youtu.be/cw826XIOZIg?si=afCo0uhLC-s2b_Kd
class Solution528:
    def __init__(self, w: List[int]) -> None:
        self.prefix_sums = []

        #  SC & TC: O(n)
        for weight in w:
            if not self.prefix_sums:
                self.prefix_sums.append(weight)
            else:
                self.prefix_sums.append(weight + self.prefix_sums[-1])

    def pick_index(self) -> int:
        """
        Time Complexity: O(log n)
        """
        roll = randint(0, self.prefix_sums[-1] - 1)
        left, right = 0, len(self.prefix_sums) - 1
        while left <= right:
            mid = (right + left) // 2
            if roll < self.prefix_sums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == "__main__":

    def test(weights: List[int]) -> dict[int:int]:
        iterations = 10**6
        picked_indices = Counter(
            [Solution528(weights).pick_index() for _ in range(iterations)]
        ).items()
        probabilities = {weights[k]: v * 100.0 / iterations for k, v in picked_indices}

        return probabilities

    print(f"Probabilities: {test([3, 5, 2])}")
