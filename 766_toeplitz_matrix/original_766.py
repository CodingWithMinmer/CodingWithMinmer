from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols= len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if i < rows-1 and j < cols-1:
                    if matrix[i][j] != matrix[i+1][j+1]:return False
        return True
    

class TestToeplitz:
    def test_basic_3_by_3_matrix(self):
        # A 3x3 Toeplitz matrix
        matrix = [
            [1, 2, 3],
            [7, 1, 2],
            [6, 7, 1]
        ]
        s = Solution()
        assert s.isToeplitzMatrix(matrix) == True

        # A 3x2 non-Toeplitz matrix
        matrix = [
            [1, 2],
            [3, 2],
            [6, 7]
        ]
        assert s.isToeplitzMatrix(matrix) == False
        
    def test_large_integer_toeplitz_matrix(self):
        # A 5x6 Toeplitz matrix
        matrix = [
            [0, 1, 2, 3, 4, 5],
            [6, 0, 1, 2, 3, 4],
            [7, 6, 0, 1, 2, 3],
            [8, 7, 6, 0, 1, 2],
            [9, 8, 7, 6, 0, 1]
        ]
        s = Solution()
        assert s.isToeplitzMatrix(matrix) == True

        # A 5x6 non-Toeplitz matrix
        matrix = [
            [0, 1, 2, 3, 4, 5],
            [6, 0, 1, 2, 3, 4],
            [7, 6, 0, 1, 2, 3],
            [8, 7, 6, 0, 1, 2],
            [9, 8, 7, 6, 3, 1]  # This row breaks the Toeplitz property
        ]
        assert s.isToeplitzMatrix(matrix) == False

    def test_single_column_matrix(self):
        # An 11x1 matrix, which is always Toeplitz
        matrix = [
            [0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]
        ]
        s = Solution()
        assert s.isToeplitzMatrix(matrix) == True

    def test_single_row_matrix(self):
        # A 1x11 matrix, which is always Toeplitz
        matrix = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ]
        s = Solution()
        assert s.isToeplitzMatrix(matrix) == True