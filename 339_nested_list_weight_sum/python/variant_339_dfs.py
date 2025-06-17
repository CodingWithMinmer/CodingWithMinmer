from collections import deque
from typing import List, Union

# VARIANT: What if you had to define your own schema for NestedList and implement DFS?
class Object:
    def __init__(self):
        self.value: List['Object' | int]

class Solution:
    def depthSum(self, objs: List[Object]) -> int:
        def dfs(objs, depth):
            sum = 0
            for obj in objs:
                if isinstance(obj, int):
                    sum += obj * depth
                else:
                    sum += dfs(obj.value, depth + 1)
            return sum
        return dfs(objs, 1)