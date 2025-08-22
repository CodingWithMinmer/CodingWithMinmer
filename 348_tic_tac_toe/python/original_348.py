# LC: https://leetcode.com/problems/design-tic-tac-toe/
# SOURCE: https://youtu.be/BuoP3RlH3Q4?si=8zXLND0GvtjhUj70
class TicTacToe_348:
    def __init__(self, n: int) -> None:
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n

    def move(self, player: int, row: int, col: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(N)
        """
        point = 1 if player == 1 else -1

        self.rows[row] += point
        self.cols[col] += point
        if row == col:
            self.diagonal += point
        if (self.n - 1) == (row + col):
            self.anti_diagonal += point

        if (
            (abs(self.rows[row]) == self.n)
            or (abs(self.cols[col]) == self.n)
            or (abs(self.diagonal) == self.n)
            or (abs(self.anti_diagonal) == self.n)
        ):
            return player

        return 0
