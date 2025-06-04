class Solution:
    def countElements(self, nums: list[int], target: int) -> int:
        def binarySearch(lowerSearch):
            l = 0
            r = len(nums)-1
            n = len(nums)
            while l <= r:
                mid = (l+r) //2
                
                if nums[mid] > target:
                    r  = mid -1
                elif nums[mid] < target:
                    l = mid +1
                else:
                    if lowerSearch:
                        if mid == l or nums[mid-1] < target:
                            return mid
                        r = mid -1
                    else:

                        if mid == r or nums[mid+1] > target:
                            return mid
                        l = mid +1
                    
            return -1
        lower = binarySearch(True)
        if lower == -1:  return 0
        return binarySearch(False) - lower +1
            

if __name__ == "__main__":
    # Valid cases
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    assert solution.countElements(nums, target) == 2
    target = 6
    assert solution.countElements(nums, target) == 0
    nums = [2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12]
    target = 9
    assert solution.countElements(nums, target) == 5
    target = 2
    assert solution.countElements(nums, target) == 2
    target = 3
    assert solution.countElements(nums, target) == 3
    target = 10
    assert solution.countElements(nums, target) == 1
    target = 12
    assert solution.countElements(nums, target) == 2
    nums = [1, 2, 3, 4, 5]
    target = 1
    assert solution.countElements(nums, target) == 1
    target = 2
    assert solution.countElements(nums, target) == 1
    target = 3
    assert solution.countElements(nums, target) == 1
    target = 4
    assert solution.countElements(nums, target) == 1
    target = 5
    assert solution.countElements(nums, target) == 1
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    target = 1
    assert solution.countElements(nums, target) == 9
    nums = [-3, -2, -1, 0, 1, 2, 3]
    target = -3
    assert solution.countElements(nums, target) == 1
    target = -2
    assert solution.countElements(nums, target) == 1
    target = -1
    assert solution.countElements(nums, target) == 1
    target = 0
    assert solution.countElements(nums, target) == 1
    target = 1
    assert solution.countElements(nums, target) == 1
    target = 2
    assert solution.countElements(nums, target) == 1
    target = 3
    assert solution.countElements(nums, target) == 1

    # Target not found cases
    nums = [5, 7, 7, 8, 8, 10]
    target = 9  # Not Found
    assert solution.countElements(nums, target) == 0
    target = 6  # Not Found
    assert solution.countElements(nums, target) == 0
    target = -5  # Too low
    assert solution.countElements(nums, target) == 0
    target = 60  # Too high
    assert solution.countElements(nums, target) == 0

    nums = []  # Empty list
    target = -5  # Empty vector
    assert solution.countElements(nums, target) == 0
    target = 50  # Empty vector
    assert solution.countElements(nums, target) == 0

    nums = [2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12]
    target = 1  # Too low
    assert solution.countElements(nums, target) == 0
    target = 4  # Not found
    assert solution.countElements(nums, target) == 0
    target = 15  # Too high
    assert solution.countElements(nums, target) == 0

    nums = [1, 2, 3, 4, 5]
    target = 0
    assert solution.countElements(nums, target) == 0
    target = 6
    assert solution.countElements(nums, target) == 0
    print("All tests passed!!!")