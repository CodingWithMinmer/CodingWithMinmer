import pytest
# from utils.ListNode import ListNode
# --- Placeholder for Solution_23_First_Variant ---
# You'll need to replace this with your actual implementation
class Solution_23_First_Variant:
    def merge(self,arr1,arr2):
        newMerged = []
        p1,p2 = 0,0
        m,n = len(arr1),len(arr2)
        while p1 < m and p2 < n:
            
            if arr1[p1] <= arr2[p2]:
                newMerged.append(arr1[p1])
                p1 +=1
            else:
                newMerged.append(arr2[p2])
                p2 +=1
            

        if p1 < m:
            newMerged += arr1[p1:]
        if p2 < n:
            newMerged += arr2[p2:]
            
        return newMerged
    
    def mergeKLists(self, lists):
        # This is a dummy implementation for testing purposes
        # Replace this with your actual logic to merge k sorted integer arrays
        interval = 1
        amount  = len(lists)
        while interval < amount:
            for i in range(0,amount-interval,interval*2):
                # print(lists[i],lists[i+1])
                lists[i] = self.merge(lists[i],lists[i+interval])
                
                
            interval *=2
        return lists[0] if amount > 0 else None 



# --- Tests for First Variant ---

def test_merge_k_sorted_lists_first_variant_zero_lists():
    lists = [[]]
    s = Solution_23_First_Variant()
    assert s.mergeKLists(lists) == []

def test_merge_k_sorted_lists_first_variant_all_non_empty_lists():
    lists = [
        [1, 3],
        [2],
        [4, 5]
    ]
    s = Solution_23_First_Variant()
    expected = [1, 2, 3, 4, 5]
    assert s.mergeKLists(lists) == expected

def test_merge_k_sorted_lists_first_variant_some_empty_some_not_empty_lists():
    lists = [
        {},
        {1, 3},
        {},
        {2},
        {4, 5},
        {},
        {},
        {}
    ]
    # Convert sets back to lists for consistent behavior with the dummy Solution
    lists_as_lists = [list(l) for l in lists]
    s = Solution_23_First_Variant()
    expected = [1, 2, 3, 4, 5]
    assert s.mergeKLists(lists_as_lists) == expected

def test_merge_k_sorted_lists_first_variant_negative_numbers_and_zeroes():
    lists = [
        [-3, -2, 0, 8, 10],
        [-1, 1, 5, 11],
        [2, 3, 4, 6, 7, 9]
    ]
    s = Solution_23_First_Variant()
    expected = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert s.mergeKLists(lists) == expected

def test_merge_k_sorted_lists_first_variant_negative_numbers_and_zeroes_and_empty_lists():
    lists = [
        [],[],[],[],[],
        [-3, -2, 0, 8, 10],
        [],[],[],[],[],
        [-1, 1, 5, 11],
        [2, 3, 4, 6, 7, 9],
        [],[],[],[],[]
    ]
    s = Solution_23_First_Variant()
    expected = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert s.mergeKLists(lists) == expected

def test_merge_k_sorted_lists_first_variant_lots_of_lists():
    lists = [
        [1, 3, 5, 7, 9, 11, 13],
        [2, 4, 6, 8, 10, 12],
        [0],
        [14, 16, 18, 20],
        [15, 17, 19, 21, 23],
        [500, 1000],
        [250, 750, 1500]
    ]
    s = Solution_23_First_Variant()
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                15, 16, 17, 18, 19, 20, 21, 23, 250, 500, 750, 1000, 1500]
    assert s.mergeKLists(lists) == expected

def test_merge_k_sorted_lists_first_variant_single_list():
    lists = [
        [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    s = Solution_23_First_Variant()
    expected = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert s.mergeKLists(lists) == expected

def test_merge_k_sorted_lists_first_variant_one_element_lists():
    lists = [
        [10], [9], [8], [7], [6], [5], [4], [3], [2], [1], [0], [-1]
    ]
    s = Solution_23_First_Variant()
    expected = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert s.mergeKLists(lists) == expected

def test_merge_k_sorted_lists_first_variant_duplicates_among_lists():
    lists = [
        [1, 3, 5, 7, 9, 11, 13],
        [1, 3, 5, 7, 9, 11, 13],
        [1, 3, 5, 7, 9, 11, 13],
        [1, 3, 5, 7, 9, 11, 13],
        [1, 3, 5, 7, 9, 11, 13]
    ]
    s = Solution_23_First_Variant()
    expected = [1, 1, 1, 1, 1,
                3, 3, 3, 3, 3,
                5, 5, 5, 5, 5,
                7, 7, 7, 7, 7,
                9, 9, 9, 9, 9,
                11, 11, 11, 11, 11,
                13, 13, 13, 13, 13]
    assert s.mergeKLists(lists) == expected

    lists = [
        [1, 3, 5, 7, 9, 11, 13],
        [2, 4, 6],
        [],[],[],[],[],
        [1, 3, 5, 7, 9, 11, 13],
        [2, 4, 6],
        [1000, 1001],
        [],[],[],{},{} # Changed set to list to avoid issues with empty set
    ]
    s = Solution_23_First_Variant()
    expected = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 9, 9,
                11, 11, 13, 13, 1000, 1001]
    assert s.mergeKLists(lists) == expected




if __name__ == "__main__":
    test_merge_k_sorted_lists_first_variant_zero_lists()
    test_merge_k_sorted_lists_first_variant_all_non_empty_lists()
    test_merge_k_sorted_lists_first_variant_some_empty_some_not_empty_lists()
    test_merge_k_sorted_lists_first_variant_negative_numbers_and_zeroes()
    test_merge_k_sorted_lists_first_variant_negative_numbers_and_zeroes_and_empty_lists()
    test_merge_k_sorted_lists_first_variant_lots_of_lists()
    test_merge_k_sorted_lists_first_variant_single_list()
    test_merge_k_sorted_lists_first_variant_one_element_lists()
    test_merge_k_sorted_lists_first_variant_duplicates_among_lists()
    print("All First Variant tests passed!")