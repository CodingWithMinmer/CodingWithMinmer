from enum import Enum

class Direction(Enum):
    UNKNOWN = -1,
    DEC = 0,
    INC = 1,
    FLAT = 2

def countMonotonicSequences(nums):
    if len(nums) <= 1:
        return 0

    count = 1 if nums[0] != nums[1] else 0
    dir = Direction.UNKNOWN
    for i in range(len(nums[1:])):
        if nums[i] > nums[i - 1]:
            if dir == Direction.DEC or dir == Direction.FLAT:
                count += 1
            dir = Direction.INC
        elif nums[i] < nums[i - 1]:
            if dir == Direction.INC or dir == Direction.FLAT:
                count += 1
            dir = Direction.DEC
        else:
            if dir != Direction.FLAT:
                dir = Direction.FLAT
                count += 1
    
    return count
