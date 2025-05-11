import heapq
from typing import List


class element:
    def __init__(self, list_index: int, index: int, val: int):
        self.list_index = list_index
        self.index = index
        self.val = val

    def __lt__(self, other):
        return self.val < other.val


# VARIANT: What if you had to merge K sorted integer arrays an an iterator?
# SOURCE: https://youtu.be/ewjDj_s1HVU?si=z5NzGnGkg_FgGYuE&t=1334
class Solution_23_Second_Variant:
    def __init__(self, lists: List[List[int]]) -> None:
        """
        Time Complexity: O(k)
        Space Complexity: O(k)
        """
        self.lists = lists
        self.min_pq = []

        for i, l in enumerate(lists):
            if l[0]:
                heapq.heappush(self.min_pq, element(i, 0, l[0]))

    def hasNext(self) -> bool:
        return self.min_pq != []

    def next(self) -> None:
        result = []
        if not self.hasNext():
            raise Exception("No more elements left")

        item = heapq.heappop(self.min_pq)
        list_index, index, val = item.list_index, item.index, item.val

        index += 1
        if index < len(self.lists[list_index]):
            heapq.heappush(
                self.min_pq, element(list_index, index, self.lists[list_index][index])
            )

        return val


if __name__ == "__main__":
    iterator = Solution_23_Second_Variant([[1, 3], [2], [4, 5]])
    assert iterator.hasNext() == True
    assert iterator.next() == 1
    assert iterator.next() == 2
    assert iterator.next() == 3
    assert iterator.hasNext() == True
    assert iterator.next() == 4
    assert iterator.next() == 5
    assert iterator.hasNext() == False
