def countMonotonicSequences(nums):
    dir = -1
    count = 0
    is_flat = False
    for i in range(len(nums[1:])):
        if nums[i] > nums[i - 1]:
            if dir == 0 or dir == -1:
                count += 1
            if is_flat and dir == 1:
                is_flat = False
                count += 2
            if is_flat:
                is_flat = False
                count += 1
            dir = 1
        elif nums[i] < nums[i - 1]:
            if dir == 1 or dir == -1:
                count += 1
            if is_flat and dir == 0:
                is_flat = False
                count += 2
            if is_flat:
                is_flat = False
                count += 1
            dir = 0
        else:
            is_flat = True
    
    if is_flat:
        count += 1

    return count