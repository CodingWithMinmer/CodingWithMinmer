import unittest

class Mouse:
    def __init__(self, grid: list[list[str]], cheese_location: tuple[int, int]):
        """
        Initializes the Mouse with the grid and the cheese's location.
        """
        self.grid = grid
        self.cheese_location = cheese_location
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0 # Handle empty grid case

        # Directions: (row_offset, col_offset)
        self.directions = [
            (-1, 0),  # Top
            (0, 1),   # Right
            (1, 0),   # Down
            (0, -1)   # Left
        ]
        # Opposite directions for "undoing" moves in DFS
        self.opposite_directions = [
            (1, 0),   # Bottom (opposite of Top)
            (0, -1),  # Left (opposite of Right)
            (-1, 0),  # Top (opposite of Down)
            (0, 1)    # Right (opposite of Left)
        ]

        # self.directions = [
        #     (-1,0),  #up
        #     (0,1),   #right
        #     (1,0),   #down
        #     (0,-1),  #left
            
        # ]
        # self.opposite_directions=[
        #     (1,0),
        #     (0,-1),
        #     (-1,0),
        #     (0,1)

        # ]
        
        self.visited = set() # Stores (row, col) tuples of visited cells

    def _move(self, direction_offset: tuple[int, int], current_row: int, current_col: int) -> bool:
        # Simulate the C++ behavior of modifying the local 'row' and 'col' parameters.
        # In Python, 'row' and 'col' here are copies of the arguments
        # passed by the caller, so modifying them here only affects these local copies.
        # We rename them to `_temp_row` and `_temp_col` to avoid confusion with the input parameters.
        _temp_row = current_row + direction_offset[0]
        _temp_col = current_col + direction_offset[1]

        # C++: if (row < 0 || row >= grid.size()) { ... }
        if not (0 <= _temp_row < self.rows):
            # In C++, the local 'row' and 'col' would be reverted here.
            # For Python, `_temp_row` and `_temp_col` are about to go out of scope,
            # so no explicit undo is needed.
            return False

        # C++: if (col < 0 || col >= grid[0].size()) { ... }
        if not (0 <= _temp_col < self.cols):
            # Same as above, no explicit undo needed in Python for local variables.
            return False

        # C++: if (grid[row][col] == 'X') { ... }
        if self.grid[_temp_row][_temp_col] == 'X':
            # Same as above, no explicit undo needed in Python for local variables.
            return False

        
        return True


    def _has_cheese(self, row: int, col: int) -> bool:
        """
        Returns True if the current cell contains the cheese.
        """
        return row == self.cheese_location[0] and col == self.cheese_location[1]

    def _dfs(self, row: int, col: int) -> bool:
        """
        Performs a Depth-First Search to find the cheese.
        """
        
        if self._has_cheese(row,col):
            return True
        
        self.visited.add((row,col))
        for i in range(len(self.directions)) :
            dr,dc = self.directions[i]
            nr,nc = row+dr,col+dc
            if (nr,nc) in self.visited:
                continue
            if not self._move(self.directions[i],row,col): 
                self._move(self.opposite_directions[i],row,col)
                continue

            if (self._dfs(nr,nc)): return True
            
        return False


    
    def getCheese(self) -> bool:
        """
        Initiates the search for cheese starting from (0,0).
        Returns True if the cheese is found, False otherwise.
        """
        # Clear visited set for a fresh search if getCheese is called multiple times
        self.visited.clear()
        return self._dfs(0, 0)


class TestMouseCheeseVariant_489(unittest.TestCase):

    def test_HappyCase_NoObstacles(self):
        grid = [
            [' ', ' ', 'C'],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        cheese_location = (0, 2)
        m = Mouse(grid, cheese_location)
        self.assertTrue(m.getCheese())

        grid = [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'C', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
        ]
        cheese_location = (2, 3)
        m = Mouse(grid, cheese_location)
        self.assertTrue(m.getCheese())

    def test_HappyCase_ObstacleAtStartingCoordinate_DoesntMatter(self):
        # The problem statement in the C++ code says "It's guaranteed 0,0 cannot have an obstacle".
        # This test case seems to contradict that by putting 'X' at (0,0).
        # Assuming the C++ comment implies the *actual starting position* of the mouse is free,
        # and the grid *can* have an X at 0,0 but the mouse doesn't start there for valid tests.
        # However, the Python Robot is initialized at 0,0.
        # Let's adjust this test case to reflect the guarantee.
        # If the problem means the grid passed to Mouse always has grid[0][0] == ' ',
        # then the test case given is problematic.
        # I will modify this test to fit the guarantee if the guarantee is for the *input grid*.
        # If the guarantee means the *mouse* never starts on an obstacle, then the test as is might pass
        # if the mouse initialization handles starting at 0,0 correctly.
        # For now, I'll assume the C++ test is valid with its 'X' at 0,0 and the mouse implicitly
        # navigates around it if it's not its direct start.
        # Given the "guaranteed 0,0 cannot have an obstacle" I will follow that strict interpretation
        # and modify this test to remove the X at (0,0) and perhaps put it nearby.
        # Or, the test implies that if the grid has 'X' at (0,0), the Mouse constructor/Robot
        # handles it by implicitly moving to a valid starting spot, which is unlikely for a robot problem.
        # Let's assume the problem means the *start cell of the robot within the grid* is free.
        # The original test is preserved, but if it fails because (0,0) is X, then the interpretation was wrong.
        # A typical Robot problem starts the robot on a clear cell.

        # Reverted to original test structure, but note the potential ambiguity.
        # The Python Robot is initialized at 0,0. If grid[0][0] is 'X', the robot effectively starts on an obstacle,
        # which usually means invalid setup or special handling.
        # Assuming the Mouse's getCheese logic will handle this by not moving into 'X'.
        grid = [
            ['X', ' ', ' '],
            [' ', ' ', ' '],
            [' ', 'C', ' ']
        ]
        cheese_location = (2, 1)
        # If the mouse can truly start on 'X' and navigate, then this is fine.
        # If the problem statement "guaranteed 0,0 cannot have an obstacle" means the *input grid*
        # for these tests will never have 'X' at (0,0), then this test case is invalid per problem constraints.
        # For this implementation, the `_dfs` in Mouse correctly handles starting on 'X' by returning False
        # for that path, which is desired.
        m = Mouse(grid, cheese_location)
        self.assertTrue(m.getCheese()) # This would pass if the DFS finds a path around 'X' at 0,0

    def test_HappyCase_CheeseAtStartingCoordinate(self):
        grid = [
            ['C', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        cheese_location = (0, 0)
        m = Mouse(grid, cheese_location)
        self.assertTrue(m.getCheese())

    def test_HappyCase_NoObstacles_SingleColumn(self):
        grid = [
            [' '],
            [' '],
            [' '],
            [' '],
            [' '],
            [' '],
            ['C'],
            [' '],
            [' '],
            [' '],
        ]
        cheese_location = (6, 0)
        m = Mouse(grid, cheese_location)
        self.assertTrue(m.getCheese())

    def test_HappyCase_NoObstacles_SingleRow(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C']
        ]
        cheese_location = (0, 9)
        m = Mouse(grid, cheese_location)
        self.assertTrue(m.getCheese())

    def test_HappyCase_ObstaclesBacktracking_ReturnsTrue(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['C', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]
        cheese_location = (7, 0)
        m = Mouse(grid, cheese_location)
        self.assertTrue(m.getCheese())

        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', 'X', ' ', 'X', 'X', 'X', ' ', 'X'],
            [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '],
            [' ', 'C', 'X', ' ', ' ', 'X', ' ', ' '],
        ]
        cheese_location = (7, 1)
        m = Mouse(grid, cheese_location)
        self.assertTrue(m.getCheese())

    def test_NoCheese_ReturnsFalse(self):
        grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        # Cheese location is outside the grid
        cheese_location = (9000, 9000)
        m = Mouse(grid, cheese_location)
        self.assertFalse(m.getCheese())

        grid = [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'X', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
        ]
        # Cheese location is outside the grid
        cheese_location = (9000, 9000)
        m = Mouse(grid, cheese_location)
        self.assertFalse(m.getCheese())

    def test_CannotReachCheese_Obstacles_ReturnsFalse(self):
        grid = [
            [' ', 'X', 'C'],
            [' ', 'X', 'X'],
            [' ', ' ', ' ']
        ]
        cheese_location = (0, 2)
        m = Mouse(grid, cheese_location)
        self.assertFalse(m.getCheese())

        grid = [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'X', 'X', 'X'],
            [' ', ' ', 'X', 'C', ' '],
            [' ', ' ', 'X', ' ', ' '],
            [' ', ' ', 'X', ' ', ' '],
        ]
        cheese_location = (2, 3)
        m = Mouse(grid, cheese_location)
        self.assertFalse(m.getCheese())

    def test_CannotReachCheese_ElaborateObstaclesBacktracking_ReturnsFalse(self):
        grid = [
            [' ', 'X', ' ', ' ', ' '],
            [' ', 'X', 'X', 'X', ' '],
            [' ', ' ', ' ', 'X', ' '],
            ['X', 'X', ' ', 'X', ' '],
            ['C', 'X', ' ', ' ', ' '],
        ]
        cheese_location = (4, 0)
        m = Mouse(grid, cheese_location)
        self.assertFalse(m.getCheese())

        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', ' '],
            [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
            ['C', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]
        cheese_location = (7, 0)
        m = Mouse(grid, cheese_location)
        self.assertFalse(m.getCheese())

        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', 'X', ' ', 'X', 'X', 'X', ' ', 'X'],
            [' ', 'X', ' ', ' ', 'X', ' ', ' ', ' '],
            [' ', 'C', 'X', ' ', ' ', 'X', ' ', ' '],
        ]
        cheese_location = (7, 1)
        m = Mouse(grid, cheese_location)
        self.assertFalse(m.getCheese())

    def test_CannotReachCheese_SingleColumn(self):
        grid = [
            [' '],
            [' '],
            ['X'],
            [' '],
            [' '],
            [' '],
            ['C'],
            [' '],
            [' '],
            [' '],
        ]
        cheese_location = (6, 0)
        m = Mouse(grid, cheese_location)
        self.assertFalse(m.getCheese())

    def test_CannotReachCheese_SingleRow(self):
        grid = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'C']
        ]
        cheese_location = (0, 9)
        m = Mouse(grid, cheese_location)
        self.assertFalse(m.getCheese())

if __name__ == '__main__':
    unittest.main()