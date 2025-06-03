import pytest
from first_variant_23_integer_arrays import Solution_23_First_Variant 

# # --- Placeholder for Solution_23_Second_Variant ---
# # You'll need to replace this with your actual implementation
class Solution_23_Second_Variant:
    def __init__(self, lists):
        
        fv= Solution_23_First_Variant()
        self.merged = fv.mergeKLists(lists)
        self.i = 0

    def hasNext(self):
        return self.i < len(self.merged)

    def next(self):
        if self.hasNext():
            self.i +=1
            return self.merged[self.i-1]
        raise IndexError('Out of range: No more elements')
        
     




### Tests for Second Variant (Iterator)

def test_merge_k_sorted_lists_second_variant_zero_lists():
    lists = [[]]
    s = Solution_23_Second_Variant(lists)
    assert not s.hasNext()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s.next()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s.next()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s.next()

def test_merge_k_sorted_lists_second_variant_all_non_empty_lists():
    lists = [
        [1, 3],
        [2],
        [4, 5]
    ]
    s = Solution_23_Second_Variant(lists)
    assert s.hasNext(),print(s.hasNext())
    assert s.next() == 1
    assert s.hasNext()
    assert s.next() == 2
    assert s.next() == 3
    assert s.hasNext()
    assert s.next() == 4
    assert s.hasNext()
    assert s.next() == 5
    assert not s.hasNext()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s.next()

def test_merge_k_sorted_lists_second_variant_some_empty_some_not_empty_lists():
    lists = [
        [],
        [1, 3],
        [],
        [2],
        [4, 5],
        [],
        [],
        []
    ]
    s = Solution_23_Second_Variant(lists)
    assert s.hasNext()
    assert s.next() == 1
    assert s.hasNext()
    assert s.next() == 2
    assert s.next() == 3
    assert s.hasNext()
    assert s.next() == 4
    assert s.hasNext()
    assert s.next() == 5
    assert not s.hasNext()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s.next()

def test_merge_k_sorted_lists_second_variant_negative_numbers_and_zeroes():
    lists = [
        [-3, -2, 0, 8, 10],
        [-1, 1, 5, 11],
        [2, 3, 4, 6, 7, 9]
    ]
    s = Solution_23_Second_Variant(lists)
    assert s.hasNext()
    assert s.next() == -3
    assert s.hasNext()
    assert s.next() == -2
    assert s.next() == -1
    assert s.hasNext()
    assert s.next() == 0
    assert s.hasNext()
    assert s.next() == 1
    assert s.next() == 2
    assert s.next() == 3
    assert s.next() == 4
    assert s.next() == 5
    assert s.next() == 6
    assert s.next() == 7
    assert s.next() == 8
    assert s.next() == 9
    assert s.next() == 10
    assert s.next() == 11
    assert not s.hasNext()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s.next()

def test_merge_k_sorted_lists_second_variant_negative_numbers_and_zeroes_and_empty_lists():
    lists = [
        [],[],[],[],[],
        [-3, -2, 0, 8, 10],
        [],[],[],[],[],
        [-1, 1, 5, 11],
        [2, 3, 4, 6, 7, 9],
        [],[],[],[],[]
    ]
    s = Solution_23_Second_Variant(lists)
    assert s.hasNext()
    assert s.next() == -3
    assert s.hasNext()
    assert s.next() == -2
    assert s.next() == -1
    assert s.hasNext()
    assert s.next() == 0
    assert s.hasNext()
    assert s.next() == 1
    assert s.next() == 2
    assert s.next() == 3
    assert s.next() == 4
    assert s.next() == 5
    assert s.next() == 6
    assert s.next() == 7
    assert s.next() == 8
    assert s.next() == 9
    assert s.next() == 10
    assert s.next() == 11
    assert not s.hasNext()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s.next()

def test_merge_k_sorted_lists_second_variant_lots_of_lists():
    lists = [
        [1, 3, 5, 7, 9, 11, 13],
        [2, 4, 6, 8, 10, 12],
        [0],
        [14, 16, 18, 20],
        [15, 17, 19, 21, 23],
        [500, 1000],
        [250, 750, 1500]
    ]
    s = Solution_23_Second_Variant(lists)
    assert s.hasNext()
    assert s.next() == 0
    assert s.hasNext()
    assert s.next() == 1
    assert s.hasNext()
    assert s.next() == 2
    assert s.hasNext()
    assert s.next() == 3
    assert s.hasNext()
    assert s.next() == 4
    assert s.hasNext()
    assert s.next() == 5
    assert s.hasNext()
    assert s.next() == 6
    assert s.hasNext()
    assert s.next() == 7
    assert s.hasNext()
    assert s.next() == 8
    assert s.hasNext()
    assert s.next() == 9
    assert s.hasNext()
    assert s.next() == 10
    assert s.hasNext()
    assert s.next() == 11
    assert s.hasNext()
    assert s.next() == 12
    assert s.next() == 13
    assert s.next() == 14
    assert s.next() == 15
    assert s.next() == 16
    assert s.next() == 17
    assert s.next() == 18
    assert s.next() == 19
    assert s.next() == 20
    assert s.next() == 21
    assert s.next() == 23
    assert s.next() == 250
    assert s.next() == 500
    assert s.next() == 750
    assert s.next() == 1000
    assert s.next() == 1500
    assert not s.hasNext()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s.next()

def test_merge_k_sorted_lists_second_variant_single_list():
    lists = [
        [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    s = Solution_23_Second_Variant(lists)
    assert s.hasNext()
    assert s.next() == -1
    assert s.hasNext()
    assert s.next() == 0
    assert s.hasNext()
    assert s.next() == 1
    assert s.hasNext()
    assert s.next() == 2
    assert s.hasNext()
    assert s.next() == 3
    assert s.hasNext()
    assert s.next() == 4
    assert s.hasNext()
    assert s.next() == 5
    assert s.hasNext()
    assert s.next() == 6
    assert s.hasNext()
    assert s.next() == 7
    assert s.hasNext()
    assert s.next() == 8
    assert s.hasNext()
    assert s.next() == 9
    assert s.hasNext()
    assert s.next() == 10
    assert not s.hasNext()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s.next()

def test_merge_k_sorted_lists_second_variant_one_element_lists():
    lists = [
        [10], [9], [8], [7], [6], [5], [4], [3], [2], [1], [0], [-1]
    ]
    s = Solution_23_Second_Variant(lists)
    assert s.hasNext()
    assert s.next() == -1
    assert s.hasNext()
    assert s.next() == 0
    assert s.hasNext()
    assert s.next() == 1
    assert s.hasNext()
    assert s.next() == 2
    assert s.hasNext()
    assert s.next() == 3
    assert s.hasNext()
    assert s.next() == 4
    assert s.hasNext()
    assert s.next() == 5
    assert s.hasNext()
    assert s.next() == 6
    assert s.hasNext()
    assert s.next() == 7
    assert s.hasNext()
    assert s.next() == 8
    assert s.hasNext()
    assert s.next() == 9
    assert s.hasNext()
    assert s.next() == 10
    assert not s.hasNext()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s.next()

def test_merge_k_sorted_lists_second_variant_duplicates_among_lists():
    lists = [
        [1, 3, 5, 7, 9, 11, 13],
        [1, 3, 5, 7, 9, 11, 13],
        [1, 3, 5, 7, 9, 11, 13],
        [1, 3, 5, 7, 9, 11, 13],
        [1, 3, 5, 7, 9, 11, 13]
    ]
    s = Solution_23_Second_Variant(lists)
    assert s.hasNext()
    assert s.next() == 1
    assert s.next() == 1
    assert s.next() == 1
    assert s.next() == 1
    assert s.next() == 1
    assert s.next() == 3
    assert s.next() == 3
    assert s.next() == 3
    assert s.next() == 3
    assert s.next() == 3
    assert s.next() == 5
    assert s.next() == 5
    assert s.next() == 5
    assert s.next() == 5
    assert s.next() == 5
    assert s.next() == 7
    assert s.next() == 7
    assert s.next() == 7
    assert s.next() == 7
    assert s.next() == 7
    assert s.next() == 9
    assert s.next() == 9
    assert s.next() == 9
    assert s.next() == 9
    assert s.next() == 9
    assert s.next() == 11
    assert s.next() == 11
    assert s.next() == 11
    assert s.next() == 11
    assert s.next() == 11
    assert s.next() == 13
    assert s.next() == 13
    assert s.next() == 13
    assert s.next() == 13
    assert s.next() == 13
    assert not s.hasNext()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s.next()

    lists = [
        [1, 3, 5, 7, 9, 11, 13],
        [2, 4, 6],
        [],[],[],[],[],
        [1, 3, 5, 7, 9, 11, 13],
        [2, 4, 6],
        [1000, 1001],
        [],[],[],[],[]
    ]
    s2 = Solution_23_Second_Variant(lists)
    assert s2.hasNext()
    assert s2.next() == 1
    assert s2.next() == 1
    assert s2.next() == 2
    assert s2.next() == 2
    assert s2.next() == 3
    assert s2.next() == 3
    assert s2.next() == 4
    assert s2.next() == 4
    assert s2.next() == 5
    assert s2.next() == 5
    assert s2.next() == 6
    assert s2.next() == 6
    assert s2.next() == 7
    assert s2.next() == 7
    assert s2.next() == 9
    assert s2.next() == 9
    assert s2.next() == 11
    assert s2.next() == 11
    assert s2.next() == 13
    assert s2.next() == 13
    assert s2.next() == 1000
    assert s2.next() == 1001
    assert not s2.hasNext()
    with pytest.raises(IndexError, match="Out of range: No more elements"):
        s2.next()

if __name__ == '__main__':
    print("\nRunning tests for Second Variant (Iterator)...")
    test_merge_k_sorted_lists_second_variant_zero_lists()
    test_merge_k_sorted_lists_second_variant_all_non_empty_lists()
    test_merge_k_sorted_lists_second_variant_some_empty_some_not_empty_lists()
    test_merge_k_sorted_lists_second_variant_negative_numbers_and_zeroes()
    test_merge_k_sorted_lists_second_variant_negative_numbers_and_zeroes_and_empty_lists()
    test_merge_k_sorted_lists_second_variant_lots_of_lists()
    test_merge_k_sorted_lists_second_variant_single_list()
    test_merge_k_sorted_lists_second_variant_one_element_lists()
    test_merge_k_sorted_lists_second_variant_duplicates_among_lists()
    print("All Second Variant tests passed!")

