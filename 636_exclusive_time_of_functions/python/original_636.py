from collections import deque
from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result, stack, prev = [0] * n, deque(), 0             
                                                               
        for log in logs:             
            id, type, time = log.split(":")            
            id, time = int(id), int(time)
            if type == "start":
                if stack:                             
                    result[stack[-1]] += time - prev
                stack.append(id)                         
                prev = time
            else:      
                result[stack.pop()] += time - prev + 1
                prev = time + 1

        return result