#pragma once

#include <vector>

// VARIANT: What if you were given an existing board and had to figure out if one move led to a win?
bool isWin_348_Variant(std::vector<std::vector<int>> board, int player, int row, int col) {
    board[row][col] = player;
    int rows = 0, cols = 0, diagonal = 0, anti_diagonal = 0;

    int n = board.size();
    for (int i = 0; i < n; i++) {
        if (board[row][i] == player)
            rows++;

        if (board[i][col] == player)
            cols++;

        if (board[i][i] == player)
            diagonal++;

        if (board[i][n - 1 - i] == player)
            anti_diagonal++;
    }

    return rows == n || cols == n || diagonal == n || anti_diagonal == n;
}
