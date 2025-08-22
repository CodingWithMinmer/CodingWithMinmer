def findKthPositive(arr,k):
   
    l = 0
    r = len(arr)-1
    while l<=r:
        mid =(l+r) //2
        missing = arr[mid] - mid -arr[0]
        if missing < k:
            l = mid +1
        else:
            r = mid -1
        
    return arr[0] + k + r

if __name__ == '__main__':
    arr = [4,7,9,10]
    k = 1
    assert findKthPositive(arr,k) == 5

    arr = [4,7,9,10]
    k = 2
    res = findKthPositive(arr,k)
    assert res == 6,print(res)

    arr = [4,7,9,10]
    k = 3
    res = findKthPositive(arr,k)
    assert res == 8,print(res)

    arr = [1,2,4]
    k = 3
    assert findKthPositive(arr,k) == 6

    print('All test cases passed!')
