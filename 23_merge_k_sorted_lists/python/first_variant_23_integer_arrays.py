import heapq
from typing import List


class element:
    def __init__(self, list_index: int, index: int, val: int):
        self.list_index = list_index
        self.index = index
        self.val = val

    def __lt__(self, other):
        return self.val < other.val


# VARIANT: What if you had to merge K sorted integer arrays,
#          no longer linked lists?
# SOURCE: https://youtu.be/ewjDj_s1HVU?si=InCiJasPX6zyvpyD&t=889
def mergeKLists(lists: List[List[int]]) -> List[int]:
    """
    Time Complexity: O(N.log k)
    Space Complexity: O(k)
    """
    min_pq = []

    for i, l in enumerate(lists):
        if l[0]:
            heapq.heappush(min_pq, element(i, 0, l[0]))

    result = []
    while min_pq:
        item = heapq.heappop(min_pq)
        list_index, index, val = item.list_index, item.index, item.val

        result.append(val)
        index += 1
        if index < len(lists[list_index]):
            heapq.heappush(min_pq, element(list_index, index, lists[list_index][index]))

    return result


if __name__ == "__main__":
    assert mergeKLists([[1, 3], [2], [4, 5]]) == [1, 2, 3, 4, 5]
    assert mergeKLists([[1, 2, 4], [3, 5, 10], [6], [7]]) == [1, 2, 3, 4, 5, 6, 7, 10]
