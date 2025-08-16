from typing import List
        
class SolutionVariant:
    def hasSameDiagonalValues(self, list: List[int], rows: int, cols: int) -> bool:
        for i in range(len(list)):
            cr = i // cols
            cc = i % cols
            if cr == rows - 1 or cc == cols - 1:
                continue

            if list[i] != list[i + (cols + 1)]:
                return False

        return True

class TestToeplitzVariant:
    def test_basic_3_by_3_list(self):
        list = [
            1, 2, 3,
            7, 1, 2,
            6, 7, 1
        ]
        s = SolutionVariant()
        assert s.hasSameDiagonalValues(list, 3, 3) == True

        list = [
            1, 2,
            3, 2,
            6, 7
        ]
        assert s.hasSameDiagonalValues(list, 3, 2) == False
        
    def test_large_integer_toeplitz_matrix(self):
        lst = [
            0,  1,  2,  3,  4,  5,
            6,  0,  1,  2,  3,  4,
            7,  6,  0,  1,  2,  3,
            8,  7,  6,  0,  1,  2,
            9,  8,  7,  6,  0,  1
        ]
        s = SolutionVariant()
        assert s.hasSameDiagonalValues(lst, 5, 6) == True

        lst = [
            0,  1,  2,  3,  4,  5,
            6,  0,  1,  2,  3,  4,
            7,  6,  0,  1,  2,  3,
            8,  7,  6,  0,  1,  2,
            9,  8,  7,  6,  3,  1
        ]
        assert s.hasSameDiagonalValues(lst, 5, 6) == False

    def test_single_column_matrix(self):
        lst = [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ]
        s = SolutionVariant()
        assert s.hasSameDiagonalValues(lst, 11, 1) == True

    def test_single_row_matrix(self):
        lst = [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ]
        s = SolutionVariant()
        assert s.hasSameDiagonalValues(lst, 1, 11) == True