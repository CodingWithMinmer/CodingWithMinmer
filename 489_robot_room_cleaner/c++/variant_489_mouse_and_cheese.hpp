#pragma once

#include <vector>
#include <iostream>
#include <set>

class Mouse
{
    //////////////////////////////////////////
    // NOT PART OF IMPLEMENTATION
    std::vector<std::vector<char>> grid;
    std::pair<int, int> cheese_location;
    //////////////////////////////////////////

    struct Direction
    {
        std::pair<int, int> offsets; // row, col
    };
    std::vector<Direction> directions =
        {Direction{{-1, 0}}, // Top
         Direction{{0, 1}}, // Right
         Direction{{1, 0}}, // Down
         Direction{{0, -1}}}; // Left
    std::vector<Direction> opposite_directions =
        {Direction{{1, 0}}, // Bottom
         Direction{{0, -1}}, // Left
         Direction{{-1, 0}}, // Top
         Direction{{0, 1}}}; // Right
    std::set<std::pair<int, int>> visited;

    bool dfs(int row, int col) {
        if (hasCheese(row, col))
            return true;
        visited.insert({row, col});

        for (int i = 0; i < directions.size(); i++) {
            int new_row = row + directions[i].offsets.first;
            int new_col = col + directions[i].offsets.second;
            if (visited.contains({new_row, new_col}))
                continue;
            if (!move(directions[i], row, col)) {
                move(opposite_directions[i], row, col);
                continue;
            }

            if (dfs(new_row, new_col))
                return true;
            move(opposite_directions[i], row, col);
        }
        
        return false;
    }

public:
    Mouse(std::vector<std::vector<char>> grid, std::pair<int, int> cheese_location) 
        : grid(grid), cheese_location(cheese_location) {}
    /**
     * Moves to one of the directions (left, right, up, down) and returns false if you can't move and true if you can.
     */
    bool move(Direction direction, int row, int col) {
        row += direction.offsets.first;
        col += direction.offsets.second;

        if (row < 0 || row >= grid.size()) {
            row -= direction.offsets.first;
            col -= direction.offsets.second;
            return false;
        }
        if (col < 0 || col >= grid[0].size()) {
            row -= direction.offsets.first;
            col -= direction.offsets.second;
            return false;
        }
        if (grid[row][col] == 'X') {
            row -= direction.offsets.first;
            col -= direction.offsets.second;
            return false;
        }

        row -= direction.offsets.first;
        col -= direction.offsets.second;
        return true;
    }
    /**
     * Returns true if there is a cheese in the current cell.
     */
    bool hasCheese(int row, int col) {
        return row == cheese_location.first && col == cheese_location.second;
    }
    /**
     * Should return true and leave the mouse at that location or
     * false if we can't find cheese and return the mouse back to
     * where it started.
     */
    bool getCheese()
    {
        return dfs(0, 0);
    }
};
