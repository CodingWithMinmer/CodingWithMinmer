class Solution:
    def mergeSortedArray(self, nums1: list[int], nums2: list[int]):
        a = len(nums1) // 2 - 1
        b = len(nums2) - 1
        i = len(nums1) - 1

        while b >= 0:
            if a >= 0 and nums1[a] >= nums2[b]:
                nums1[i] = nums1[a]
                a -= 1
            else:
                nums1[i] = nums2[b]
                b -= 1
            i -= 1


if __name__ == "__main__":
    solution = Solution()
    list_a = [1, 3, 0, 0]
    list_b = [4, 10]
    expected = [1, 3, 4, 10]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected

    list_a = [5, 6, 7, 8, 0, 0, 0, 0]
    list_b = [1, 2, 3, 4]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected

    list_a = [0]
    list_b = [99]
    expected = [99]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected

    list_a = [1, 10, 0, 0]
    list_b = [2, 11]
    expected = [1, 2, 10, 11]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected
