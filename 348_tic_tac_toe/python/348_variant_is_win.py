from typing import List


# VARIANT: What if you were given an existing board and had to figure out if
#          one move led to a win?
# SOURCE: https://youtu.be/BuoP3RlH3Q4?si=8zXLND0GvtjhUj70&t=903
class TicTacToe_348_Variant:

    def is_win(
        self,
        board: List[List[int]],
        player: int,
        row: int,
        col: int,
    ) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        board[row][col] = player

        rows = cols = diagonal = anti_diagonal = 0

        n = len(board)
        for i in range(n):
            if board[row][i] == player:
                rows += 1

            if board[i][col] == player:
                cols += 1

            if board[i][i] == player:
                diagonal += 1

            if board[i][n - 1 - i] == player:
                anti_diagonal += 1

        return (rows == n) or (cols == n) or (diagonal == n) or (anti_diagonal == n)


if __name__ == "__main__":
    board = [
        [1, 1, 2],
        [2, 1, 2],
        [0, 0, 0],
    ]
    assert TicTacToe_348_Variant().is_win(board, 2, 1, 1) == True
    assert TicTacToe_348_Variant().is_win(board, 2, 0, 1) == False

    board = [[1, 2], [0, 0]]
    assert TicTacToe_348_Variant().is_win(board, 1, 1, 1) == True
