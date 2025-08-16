from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(0,rows-1):
            for c in range(0,cols-1):
                if(matrix[r][c]!=matrix[r+1][c+1]):
                    return False

        return True