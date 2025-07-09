from collections import deque, defaultdict
from typing import List

class Log:
    def __init__(self, name, type, time):
        self.name = name
        self.type = type
        self.time = time

def profile_app(logs: List[Log]):
    result, stack, prev = defaultdict(int), deque(), 0             
                                                            
    for log in logs:
        if log.type == "start":
            if stack:                             
                result[stack[-1]] += log.time - prev
            stack.append(log.name)                         
        else:      
            result[stack.pop()] += log.time - prev
        prev = log.time

    return result