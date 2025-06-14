import collections

# Assuming the content of 'first_variant_1091_return_shortest_path.hpp' is implemented in a class Solution_1091_First_Variant
# and 'second_variant_1091_return_single_path.hpp' in Solution_1091_Second_Variant.
# For this example, I'll provide a placeholder implementation for the Python classes.

# Placeholder for Solution_1091_First_Variant (BFS-based for shortest path)
from collections import deque
class Solution_1091_First_Variant:
    def shortestPathBinaryMatrix(self, grid):
        m,n = len(grid),len(grid[0])
        if grid[m-1][n-1] != 0 or grid[0][0] != 0: return []
        q = deque([(0,0,[[0,0]])])
        visited = {(0,0)}
        directions = [[1,0],[-1,0],[-1,-1],[-1,1], [1,-1],[1,1],[0,1],[0,-1]]
        

        while q:
            r,c,path = q.popleft()
            print((r,c),path)
            if (r,c) == (m-1,n-1):
                return path
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if -1 < nr < m and -1 < nc < n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    visited.add((nr,nc))

                    
                    print('path',path,(r,c),(nr,nc))
                    q.append((nr,nc,path+[[nr,nc]]))
        return []
                
        

def test_shortest_path_first_variant():
    print("Running tests for ShortestPath_FirstVariant...")

    # OneMove
    grid = [[0, 1], [1, 0]]
    expected = [[0, 0], [1, 1]]
    s = Solution_1091_First_Variant()
    assert s.shortestPathBinaryMatrix(grid) == expected, f"OneMove failed. Expected: {expected}, Got: {s.shortestPathBinaryMatrix(grid)}"
    print("OneMove passed.")

    # ThreeMoves
    grid = [[0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]]
    expected = [[0, 0], [0, 1], [1, 2], [2, 2]]
    s = Solution_1091_First_Variant()
    assert s.shortestPathBinaryMatrix(grid) == expected, f"ThreeMoves failed. Expected: {expected}, Got: {s.shortestPathBinaryMatrix(grid)}"
    print("ThreeMoves passed.")

    # OnlyDiagonalPath
    grid = [[0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0]]
    expected = [[0, 0], [1, 1], [2, 2], [3, 3]]
    s = Solution_1091_First_Variant()
    assert s.shortestPathBinaryMatrix(grid) == expected, f"OnlyDiagonalPath failed. Expected: {expected}, Got: {s.shortestPathBinaryMatrix(grid)}"
    print("OnlyDiagonalPath passed.")

    # PrioritizeShorterDiagonalPath
    grid = [[0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]]
    expected = [[0, 0], [1, 1], [2, 2], [3, 3]]
    s = Solution_1091_First_Variant()
    assert s.shortestPathBinaryMatrix(grid) == expected, f"PrioritizeShorterDiagonalPath failed. Expected: {expected}, Got: {s.shortestPathBinaryMatrix(grid)}"
    print("PrioritizeShorterDiagonalPath passed.")

    # SingleRow
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
    expected = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]]
    s = Solution_1091_First_Variant()
    assert s.shortestPathBinaryMatrix(grid) == expected, f"SingleRow failed. Expected: {expected}, Got: {s.shortestPathBinaryMatrix(grid)}"
    print("SingleRow passed.")

    # SingleColumn
    grid = [[0], [0], [0], [0], [0]]
    expected = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
    s = Solution_1091_First_Variant()
    assert s.shortestPathBinaryMatrix(grid) == expected, f"SingleColumn failed. Expected: {expected}, Got: {s.shortestPathBinaryMatrix(grid)}"
    print("SingleColumn passed.")

    # TopLeftIsOne_NotPossible
    grid = [[1, 0, 0],
            [1, 1, 0],
            [1, 1, 0]]
    s = Solution_1091_First_Variant()
    assert not s.shortestPathBinaryMatrix(grid), f"TopLeftIsOne_NotPossible failed. Expected empty, Got: {s.shortestPathBinaryMatrix(grid)}"
    print("TopLeftIsOne_NotPossible passed.")

    # BottomRightIsOne_NotPossible
    grid = [[0, 0, 0],
            [1, 1, 0],
            [1, 1, 1]]
    s = Solution_1091_First_Variant()
    assert not s.shortestPathBinaryMatrix(grid), f"BottomRightIsOne_NotPossible failed. Expected empty, Got: {s.shortestPathBinaryMatrix(grid)}"
    print("BottomRightIsOne_NotPossible passed.")

    # PathNotPossible
    grid = [[0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]]
    s = Solution_1091_First_Variant()
    assert not s.shortestPathBinaryMatrix(grid), f"PathNotPossible failed. Expected empty, Got: {s.shortestPathBinaryMatrix(grid)}"
    print("PathNotPossible passed.")
    print("-" * 30)



if __name__ == "__main__":
    test_shortest_path_first_variant()
    print("All tests passed!")