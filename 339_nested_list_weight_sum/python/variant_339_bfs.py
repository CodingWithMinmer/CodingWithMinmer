from collections import deque
from typing import List, Union

# VARIANT: What if you had to define your own schema for NestedList and implement BFS?
class Object:
    def __init__(self):
        self.value: List['Object' | int]

class Solution:
    def depthSum(self, objs: List[Object]) -> int:
        queue = deque(objs)
        level = 1
        sum = 0
        while queue:
            for _ in range(len(queue)):
                obj = queue.popleft()
                if isinstance(obj, int):
                    sum += obj * level
                else:
                    queue.extend(obj.value)
            level += 1

        return sum