from collections import deque,defaultdict
def first_variant_1424_anti_diagonal(nums):
    res = defaultdict(list)
    q = deque([(0,0)])
    m = len(nums)
    while q:
        r,c = q.popleft()
        res[(r+c)].append(nums[r][c])
        
        if c+1 < len(nums[r]):
            q.append((r,c+1))

        if c == 0 and r+1 < m:
            q.append((r+1,c))
        
    return list(res.values())

        

if __name__ == "__main__":
    nums= [[1,2,3],[4,5,6],[7,8,9]]
    
    res = first_variant_1424_anti_diagonal(nums)
    expected = [[1],[2,4],[3,5,7],[6,8],[9]]
    assert res == expected,print(res)

    nums= [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    expected = [[1],[2,6],[3,7,8],[4,9],[5,10,12],[11,13],[14],[15],[16]]
    res = first_variant_1424_anti_diagonal(nums)
    assert res == expected,print(res)

    print("All test cases passed!")

