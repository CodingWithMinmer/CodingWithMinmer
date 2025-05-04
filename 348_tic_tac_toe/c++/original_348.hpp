#pragma once

#include <vector>

class TicTacToe_348 {
    std::vector<int> rows;
    std::vector<int> cols;
    int diagonal = 0;
    int anti_diagonal = 0;
    int n;
public:
    TicTacToe_348(int n) : n(n), cols(n, 0), rows(n, 0) {}

    int move(int row, int col, int player) {
        int point = player == 1 ? 1 : -1;

        rows[row] += point;
        cols[col] += point;
        if (row == col)
            diagonal += point;
        if ((n - 1) - col == row)
            anti_diagonal += point;

        if (std::abs(rows[row]) == n || 
            std::abs(cols[col]) == n ||
            std::abs(diagonal) == n || 
            std::abs(anti_diagonal) == n)
            return player;
        return 0;
    }
};