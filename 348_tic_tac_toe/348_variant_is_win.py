import pytest

def isWin_348_Variant(board: list[list[int]], player: int,r: int, c: int ) -> bool:
    n = len(board)
    diag = 0
    antiDiag = 0
    rows = 0
    cols = 0
    tmp = board[r][c]
    board[r][c] = player 
    
    
    for i in range(n):
        if board[r][i] == player:
            rows += 1
        if board[i][c] == player:
            cols += 1
        if r == c and board[i][i] == player:
            diag += 1
        if r + c == n - 1 and board[i][n - i - 1] == player:
            antiDiag += 1
    board[r][c] = tmp # For mulitple test cases (python will overwrite the board's value if we don't deep copy)
    return rows == n or cols == n or diag == n or antiDiag == n


if __name__ == "__main__":
    print("Running all Tic-Tac-Toe Variant win condition tests...")

    # --- TEST(TicTacToe_Variant, Rows) ---
    print("\n--- Testing Rows ---")
    board_rows_1 = [
        [1, 1, 0],
        [2, 2, 0],
        [0, 0, 0]
    ]
    assert isWin_348_Variant(board_rows_1, 1, 0, 2), "Rows Test 1 Failed: Player 1 wins (initial state)" # This assertion seems off based on board state (P1 on row 0)
    assert isWin_348_Variant(board_rows_1, 2, 1, 2), "Rows Test 2 Failed: Player 2 wins (row 1 is 2,2,0, need a 2)"
    assert not isWin_348_Variant(board_rows_1, 1, 1, 2), "Rows Test 3 Failed: P1 doesn't win (row 1)"
    assert not isWin_348_Variant(board_rows_1, 1, 2, 0), "Rows Test 4 Failed: P1 doesn't win (row 2, col 0)"
    assert not isWin_348_Variant(board_rows_1, 1, 2, 1), "Rows Test 5 Failed: P1 doesn't win (row 2, col 1)"
    assert not isWin_348_Variant(board_rows_1, 1, 2, 2), "Rows Test 6 Failed: P1 doesn't win (row 2, col 2)"

    assert not isWin_348_Variant(board_rows_1, 2, 0, 2), "Rows Test 7 Failed: P2 doesn't win (row 0)"
    assert not isWin_348_Variant(board_rows_1, 2, 2, 0), "Rows Test 8 Failed: P2 doesn't win (row 2, col 0)"
    assert not isWin_348_Variant(board_rows_1, 2, 2, 1), "Rows Test 9 Failed: P2 doesn't win (row 2, col 1)"
    assert not isWin_348_Variant(board_rows_1, 2, 2, 2), "Rows Test 10 Failed: P2 doesn't win (row 2, col 2)"

    board_rows_2 = [
        [1, 0, 1],
        [0, 0, 0],
        [0, 2, 2]
    ]
    assert isWin_348_Variant(board_rows_2, 1, 0, 1), "Rows Test 11 Failed: Player 1 wins (row 0 - by move)"
    assert not isWin_348_Variant(board_rows_2, 1, 1, 0), "Rows Test 12 Failed: P1 doesn't win (row 1, col 0)"
    assert not isWin_348_Variant(board_rows_2, 1, 1, 1), "Rows Test 13 Failed: P1 doesn't win (row 1, col 1)"
    assert not isWin_348_Variant(board_rows_2, 1, 1, 2), "Rows Test 14 Failed: P1 doesn't win (row 1, col 2)"
    assert not isWin_348_Variant(board_rows_2, 1, 2, 0), "Rows Test 15 Failed: P1 doesn't win (row 2, col 0)"

    assert isWin_348_Variant(board_rows_2, 2, 2, 0), "Rows Test 16 Failed: Player 2 wins (row 2 - by move)"
    assert not isWin_348_Variant(board_rows_2, 2, 0, 1), "Rows Test 17 Failed: P2 doesn't win (row 0, col 1)"
    assert not isWin_348_Variant(board_rows_2, 2, 1, 1), "Rows Test 18 Failed: P2 doesn't win (row 1, col 1)"
    assert not isWin_348_Variant(board_rows_2, 2, 1, 2), "Rows Test 19 Failed: P2 doesn't win (row 1, col 2)"
    assert not isWin_348_Variant(board_rows_2, 2, 1, 0), "Rows Test 20 Failed: P2 doesn't win (row 1, col 0)"
    print("All 'Rows' tests completed.")


    # --- TEST(TicTacToe_Variant, Cols) ---
    print("\n--- Testing Columns ---")
    board_cols_1 = [
        [1, 0, 0],
        [1, 2, 0],
        [0, 2, 0]
    ]
    assert isWin_348_Variant(board_cols_1, 1, 2, 0), "Cols Test 1 Failed: Player 1 wins (col 0 - by move)"
    assert not isWin_348_Variant(board_cols_1, 1, 0, 1), "Cols Test 2 Failed: P1 doesn't win (col 1)"
    assert not isWin_348_Variant(board_cols_1, 1, 0, 2), "Cols Test 3 Failed: P1 doesn't win (col 2)"
    assert not isWin_348_Variant(board_cols_1, 1, 1, 2), "Cols Test 4 Failed: P1 doesn't win (col 2)"
    assert not isWin_348_Variant(board_cols_1, 1, 2, 2), "Cols Test 5 Failed: P1 doesn't win (col 2)"

    assert isWin_348_Variant(board_cols_1, 2, 0, 1), "Cols Test 6 Failed: Player 2 wins (col 1 - by move)"
    assert not isWin_348_Variant(board_cols_1, 2, 2, 1), "Cols Test 7 Failed: P2 doesn't win (col 1)"
    assert not isWin_348_Variant(board_cols_1, 2, 0, 2), "Cols Test 8 Failed: P2 doesn't win (col 2)"
    assert not isWin_348_Variant(board_cols_1, 2, 1, 2), "Cols Test 9 Failed: P2 doesn't win (col 2)"
    assert not isWin_348_Variant(board_cols_1, 2, 2, 2), "Cols Test 10 Failed: P2 doesn't win (col 2)"

    board_cols_2 = [
        [0, 0, 1],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert isWin_348_Variant(board_cols_2, 1, 1, 2), "Cols Test 11 Failed: Player 1 wins (col 2 - by move)"
    assert not isWin_348_Variant(board_cols_2, 1, 0, 0), "Cols Test 12 Failed: P1 doesn't win (col 0)"
    assert not isWin_348_Variant(board_cols_2, 1, 0, 1), "Cols Test 13 Failed: P1 doesn't win (col 1)"
    assert not isWin_348_Variant(board_cols_2, 1, 1, 0), "Cols Test 14 Failed: P1 doesn't win (col 0)"
    assert not isWin_348_Variant(board_cols_2, 1, 1, 1), "Cols Test 15 Failed: P1 doesn't win (col 1)"
    assert not isWin_348_Variant(board_cols_2, 1, 2, 0), "Cols Test 16 Failed: P1 doesn't win (col 0)"
    assert not isWin_348_Variant(board_cols_2, 1, 2, 1), "Cols Test 17 Failed: P1 doesn't win (col 1)"
    print("All 'Columns' tests completed.")

    # --- TEST(TicTacToe_Variant, Diagonals) ---
    print("\n--- Testing Diagonals ---")
    board_diags_1 = [
        [1, 0, 0],
        [2, 1, 0],
        [0, 2, 0]
    ]
    assert isWin_348_Variant(board_diags_1, 1, 2, 2), "Diags Test 1 Failed: Player 1 wins (main diag - by move)"
    assert not isWin_348_Variant(board_diags_1, 1, 0, 1), "Diags Test 2 Failed: P1 doesn't win (not diag)"
    assert not isWin_348_Variant(board_diags_1, 1, 0, 2), "Diags Test 3 Failed: P1 doesn't win (not diag)"
    assert not isWin_348_Variant(board_diags_1, 1, 1, 2), "Diags Test 4 Failed: P1 doesn't win (not diag)"
    assert not isWin_348_Variant(board_diags_1, 1, 2, 0), "Diags Test 5 Failed: P1 doesn't win (not diag)"

    board_diags_2 = [
        [1, 2, 1],
        [2, 0, 0],
        [2, 0, 1]
    ]
    assert isWin_348_Variant(board_diags_2, 1, 1, 1), "Diags Test 6 Failed: Player 1 wins (main diag - by move)"
    assert isWin_348_Variant(board_diags_2, 1, 1, 2), "Diags Test 7 Failed: Player 1 wins (anti-diag - by move)" # This seems to be an anti-diagonal check from C++
    assert not isWin_348_Variant(board_diags_2, 1, 2, 1), "Diags Test 8 Failed: P1 doesn't win (not diag)"
    print("All 'Diagonals' tests completed.")


    # --- TEST(TicTacToe_Variant, Antidiagonals) ---
    print("\n--- Testing Anti-Diagonals ---")
    board_antidiags_1 = [
        [0, 0, 1],
        [2, 1, 2],
        [0, 2, 0]
    ]
    assert isWin_348_Variant(board_antidiags_1, 1, 2, 0), "Anti-Diags Test 1 Failed: Player 1 wins (anti-diag - by move)"
    assert not isWin_348_Variant(board_antidiags_1, 1, 0, 0), "Anti-Diags Test 2 Failed: P1 doesn't win (not anti-diag)"
    assert not isWin_348_Variant(board_antidiags_1, 1, 0, 1), "Anti-Diags Test 3 Failed: P1 doesn't win (not anti-diag)"
    assert not isWin_348_Variant(board_antidiags_1, 1, 2, 2), "Anti-Diags Test 4 Failed: P1 doesn't win (not anti-diag)"
    print("All 'Anti-Diagonals' tests completed.")

    # --- TEST(TicTacToe_Variant, 4By4Matrix_Antidiagonals) ---
    print("\n--- Testing 4x4 Matrix (Anti-Diagonals) ---")
    board_4x4 = [
        [2, 0, 1, 1],
        [2, 1, 1, 0],
        [0, 0, 0, 2],
        [1, 0, 2, 2]
    ]
    assert isWin_348_Variant(board_4x4, 1, 2, 1), "4x4 Anti-Diags Test 1 Failed: Player 1 wins (col 1, by move)"
    assert not isWin_348_Variant(board_4x4, 1, 0, 1), "4x4 Anti-Diags Test 2 Failed: P1 doesn't win"
    assert not isWin_348_Variant(board_4x4, 1, 1, 3), "4x4 Anti-Diags Test 3 Failed: P1 doesn't win"
    assert not isWin_348_Variant(board_4x4, 1, 2, 0), "4x4 Anti-Diags Test 4 Failed: P1 doesn't win"
    assert not isWin_348_Variant(board_4x4, 1, 2, 2), "4x4 Anti-Diags Test 5 Failed: P1 doesn't win"
    assert not isWin_348_Variant(board_4x4, 1, 3, 1), "4x4 Anti-Diags Test 6 Failed: P1 doesn't win"
    print("All '4x4 Matrix' tests completed.")

    # --- TEST(TicTacToe_Variant, EmptyBoard) ---
    print("\n--- Testing Empty Board ---")
    board_empty = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert not isWin_348_Variant(board_empty, 1, 0, 0), "Empty Board Test 1 Failed: P1 (0,0)"
    assert not isWin_348_Variant(board_empty, 1, 0, 1), "Empty Board Test 2 Failed: P1 (0,1)"
    assert not isWin_348_Variant(board_empty, 1, 0, 2), "Empty Board Test 3 Failed: P1 (0,2)"
    assert not isWin_348_Variant(board_empty, 1, 1, 0), "Empty Board Test 4 Failed: P1 (1,0)"
    assert not isWin_348_Variant(board_empty, 1, 1, 1), "Empty Board Test 5 Failed: P1 (1,1)"
    assert not isWin_348_Variant(board_empty, 1, 1, 2), "Empty Board Test 6 Failed: P1 (1,2)"
    assert not isWin_348_Variant(board_empty, 1, 2, 0), "Empty Board Test 7 Failed: P1 (2,0)"
    assert not isWin_348_Variant(board_empty, 1, 2, 1), "Empty Board Test 8 Failed: P1 (2,1)"
    assert not isWin_348_Variant(board_empty, 1, 2, 2), "Empty Board Test 9 Failed: P1 (2,2)"

    assert not isWin_348_Variant(board_empty, 2, 0, 0), "Empty Board Test 10 Failed: P2 (0,0)"
    assert not isWin_348_Variant(board_empty, 2, 0, 1), "Empty Board Test 11 Failed: P2 (0,1)"
    assert not isWin_348_Variant(board_empty, 2, 0, 2), "Empty Board Test 12 Failed: P2 (0,2)"
    assert not isWin_348_Variant(board_empty, 2, 1, 0), "Empty Board Test 13 Failed: P2 (1,0)"
    assert not isWin_348_Variant(board_empty, 2, 1, 1), "Empty Board Test 14 Failed: P2 (1,1)"
    assert not isWin_348_Variant(board_empty, 2, 1, 2), "Empty Board Test 15 Failed: P2 (1,2)"
    assert not isWin_348_Variant(board_empty, 2, 2, 0), "Empty Board Test 16 Failed: P2 (2,0)"
    assert not isWin_348_Variant(board_empty, 2, 2, 1), "Empty Board Test 17 Failed: P2 (2,1)"
    assert not isWin_348_Variant(board_empty, 2, 2, 2), "Empty Board Test 18 Failed: P2 (2,2)"
    print("All 'Empty Board' tests completed.")

    # --- TEST(TicTacToe_Variant, AllPlayer_ReturnsTrue) ---
    print("\n--- Testing All Player Wins ---")
    board_all_p1 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert isWin_348_Variant(board_all_p1, 1, 0, 0), "All P1 Test 1 Failed: (0,0)"
    assert isWin_348_Variant(board_all_p1, 1, 0, 1), "All P1 Test 2 Failed: (0,1)"
    assert isWin_348_Variant(board_all_p1, 1, 0, 2), "All P1 Test 3 Failed: (0,2)"
    assert isWin_348_Variant(board_all_p1, 1, 1, 0), "All P1 Test 4 Failed: (1,0)"
    assert isWin_348_Variant(board_all_p1, 1, 1, 1), "All P1 Test 5 Failed: (1,1)"
    assert isWin_348_Variant(board_all_p1, 1, 1, 2), "All P1 Test 6 Failed: (1,2)"
    assert isWin_348_Variant(board_all_p1, 1, 2, 0), "All P1 Test 7 Failed: (2,0)"
    assert isWin_348_Variant(board_all_p1, 1, 2, 1), "All P1 Test 8 Failed: (2,1)"
    assert isWin_348_Variant(board_all_p1, 1, 2, 2), "All P1 Test 9 Failed: (2,2)"

    board_all_p2 = [
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2]
    ]
    assert isWin_348_Variant(board_all_p2, 2, 0, 0), "All P2 Test 1 Failed: (0,0)"
    assert isWin_348_Variant(board_all_p2, 2, 0, 1), "All P2 Test 2 Failed: (0,1)"
    assert isWin_348_Variant(board_all_p2, 2, 0, 2), "All P2 Test 3 Failed: (0,2)"
    assert isWin_348_Variant(board_all_p2, 2, 1, 0), "All P2 Test 4 Failed: (1,0)"
    assert isWin_348_Variant(board_all_p2, 2, 1, 1), "All P2 Test 5 Failed: (1,1)"
    assert isWin_348_Variant(board_all_p2, 2, 1, 2), "All P2 Test 6 Failed: (1,2)"
    assert isWin_348_Variant(board_all_p2, 2, 2, 0), "All P2 Test 7 Failed: (2,0)"
    assert isWin_348_Variant(board_all_p2, 2, 2, 1), "All P2 Test 8 Failed: (2,1)"
    assert isWin_348_Variant(board_all_p2, 2, 2, 2), "All P2 Test 9 Failed: (2,2)"
    print("All 'All Player Wins' tests completed.")

    print("\n--- All tests finished running. ---")
    print("Remember to replace the placeholder `isWin_348_Variant` function with your actual logic!")