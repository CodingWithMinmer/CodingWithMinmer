class Solution:
    def countUnique(self, nums: list[int]) -> int:
        # Should run in O(k * log(N)) complexity, where k is # of unique elements
        if len(nums) == 0:
            return 0

        def upper(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        start = 0
        count = 0
        while start < len(nums):
            end = upper(nums, nums[start])
            start = end + 1
            count += 1

        return count


if __name__ == "__main__":
    solution = Solution()
    assert solution.countUnique([5, 7, 7, 8, 8, 10]) == 4
    assert solution.countUnique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert solution.countUnique([]) == 0
