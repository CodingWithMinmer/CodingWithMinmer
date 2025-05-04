#pragma once

#include <vector>
#include <set>

// This is the robot's control interface.
// You should not implement it, or speculate about its implementation
class Robot {
   public:
     // Returns true if the cell in front is open and robot moves into the cell.
     // Returns false if the cell in front is blocked and robot stays in the current cell. 
     bool move();

     // Robot will stay in the same cell after calling turnLeft/turnRight.
     // Each turn will be 90 degrees.
    void turnLeft();
    void turnRight();

         // Clean the current cell.
     void clean();
 };
 class Solution_489 {
    struct Direction {
        std::pair<int, int> offsets; // row, col
    };
    std::vector<Direction> directions = {
        {{-1, 0}}, // Top
        {{0, 1}},  // Right
        {{1, 0}},  // Down
        {{0, -1}}  // Left
    };
    std::set<std::pair<int, int>> visited;

    void dfs(Robot& robot, int direction, int row, int col) {
        robot.clean();
        visited.insert({row, col});

        for (int i = 0; i < directions.size(); i++) {
            int new_direction = (direction + i) % 4;
            int new_row = row + directions[new_direction].offsets.first;
            int new_col = col + directions[new_direction].offsets.second;

            if (visited.contains({new_row, new_col}) || !robot.move()) {
                robot.turnRight();
                continue;
            }
            dfs(robot, new_direction, new_row, new_col);
            robot.turnRight();
        }
        robot.turnRight();
        robot.turnRight();
        robot.move();
        robot.turnRight();
        robot.turnRight();
    }
public:
    void cleanRoom(Robot& robot) {
        int direction = 0;
        dfs(robot, direction, 0, 0);
    }
};