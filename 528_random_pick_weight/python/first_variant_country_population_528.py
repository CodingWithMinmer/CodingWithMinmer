from random import randint
from typing import List, Tuple


# VARIANT: What if you had to return the city that a person lives in?
# SOURCE: https://youtu.be/cw826XIOZIg?si=q8X8SWsaFjIK5d3O&t=631
class Solution_528_Variant:
    def __init__(self, populations: List[Tuple[int, int]]) -> None:
        self.prefix_sums = []

        #  SC & TC: O(n)
        for city, population in populations:
            if not self.prefix_sums:
                self.prefix_sums.append((city, population))
            else:
                self.prefix_sums.append((city, population + self.prefix_sums[-1][1]))

    def pick_index(self, generated_person: int | None) -> int:
        """
        Time Complexity: O(log n)
        Space Complexity: O(n)
        """
        if generated_person is None:
            person = randint(0, self.prefix_sums[-1][1] - 1)
        else:
            person = generated_person

        left, right = 0, len(self.prefix_sums) - 1
        while left <= right:
            mid = (right + left) // 2
            if person < self.prefix_sums[mid][1]:
                right = mid - 1
            else:
                left = mid + 1

        return self.prefix_sums[left][0]


if __name__ == "__main__":

    populations = [("US", 300), ("VN", 100), ("BR", 200)]
    s = Solution_528_Variant(populations)
    assert s.pick_index(0) == "US"
    assert s.pick_index(150) == "US"
    assert s.pick_index(299) == "US"
    assert s.pick_index(300) == "VN"
    assert s.pick_index(375) == "VN"
    assert s.pick_index(399) == "VN"
    assert s.pick_index(400) == "BR"
    assert s.pick_index(420) == "BR"
    assert s.pick_index(599) == "BR"
