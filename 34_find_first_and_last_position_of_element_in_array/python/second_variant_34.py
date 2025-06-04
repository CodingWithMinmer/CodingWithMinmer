
class Solution:
    def countUnique(self, nums: list[int]) -> int:
        n = len(nums)
        def upper(l,target):
            r = n
            while l <= r:
                mid = (l+r) //2
                if nums[mid] == target:
                    
                    if mid == n-1 or nums[mid+1] > target:
                        return mid
                    l = mid +1

                elif nums[mid] > target:
                    r = mid -1
                else:
                    l = mid +1                                        
            return -1
        
        start= end= 0
        count =0
        
        while start < n:
            end = upper(end,nums[start])
            start = end+1
            count +=1
        return count


if __name__ == "__main__":
    solution = Solution()
    # Nonzero Count cases
    nums = [2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12]
    assert solution.countUnique(nums) == 5
    nums = [-3, -2, -1, 0, 1, 2, 3]
    assert solution.countUnique(nums) == 7
    nums = [-3, -3, -3, -2, -2, -2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    assert solution.countUnique(nums) == 7
    nums = [1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 7, 7, 8, 8, 10]
    assert solution.countUnique(nums) == 6
    nums = [19, 19, 19, 19]
    assert solution.countUnique(nums) == 1
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert solution.countUnique(nums) == 1
    nums = [9001]
    assert solution.countUnique(nums) == 1
    nums = [5, 7, 7, 8, 8, 10]
    assert solution.countUnique(nums) == 4
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert solution.countUnique(nums) == 10

    # Zero Count case
    nums = []
    assert solution.countUnique(nums) == 0
    print("All tests passed!")
