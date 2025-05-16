from typing import List, Set, Tuple


# This is the robot's control interface.
# You should not implement it, or speculate about its implementation.
class Robot:
    """
    Test stub that *hides* absolute coords from Solution_489.
    Internally we keep:
      - self._room: the real 2D array of 0=open, 1=wall
      - self._abs_pos: the robot's real (r,c) in that array
    Externally, Solution_489 only ever sees a clean, unknown grid
    whose origin (0,0) is wherever the robot started.
    """

    # movement deltas in order: up, right, down, left
    _DIRS: List[Tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, room: List[List[int]], start_abs: Tuple[int, int]) -> None:
        self._room = room
        self._start_abs = start_abs
        self._abs_pos = start_abs
        self._dir_idx = 0  # 0=up,1=right,2=down,3=left
        # track cleaned in **relative** coords
        self._cleaned_rel: Set[Tuple[int, int]] = set()

    # Returns true if the cell in front is open and the robot moves into the
    # cell, else returns false if the cell in front is blocked and the robot
    # stays in the current cell.
    def move(self) -> bool:
        # figure out what absolute cell is in front
        dr, dc = Robot._DIRS[self._dir_idx]
        nr, nc = self._abs_pos[0] + dr, self._abs_pos[1] + dc

        # check bounds & walls
        if not (0 <= nr < len(self._room) and 0 <= nc < len(self._room[0])):
            return False
        if self._room[nr][nc] == 1:
            return False

        # it’s free: commit the move
        self._abs_pos = (nr, nc)
        return True

    # Robot will stay in the same cell after calling turnLeft/turnRight.
    # Each turn will be 90 degrees.
    def turnLeft(self) -> None:
        # counter-clockwise
        self._dir_idx = (self._dir_idx - 1) % 4

    def turnRight(self) -> None:
        # clockwise
        self._dir_idx = (self._dir_idx + 1) % 4

    # Clean the current cell.
    def clean(self) -> None:
        # compute relative pos = abs_pos - start_abs
        r_rel = self._abs_pos[0] - self._start_abs[0]
        c_rel = self._abs_pos[1] - self._start_abs[1]
        # mark current cell cleaned
        self._cleaned_rel.add((r_rel, c_rel))

    def get_cleaned(self, absolute: bool = False) -> Set[Tuple[int, int]]:
        """
        By default returns the set of cleaned cells *in relative coords*.
        If absolute=True, translates them back to the room_map's coords.
        """
        if not absolute:
            return set(self._cleaned_rel)
        else:
            return {
                (r + self._start_abs[0], c + self._start_abs[1])
                for (r, c) in self._cleaned_rel
            }


# LC: https://leetcode.com/problems/robot-room-cleaner/
# SOURCE: https://youtu.be/vQZZSeuDRto?si=n6TFHbJwTh0I_Gjq
class Solution_489:
    def __init__(self) -> None:
        self.directions: List[Tuple[int, int]] = [
            (-1, 0),  # up
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
        ]
        self.visited: Set[Tuple[int, int]] = set()

    def dfs(self, robot: Robot, direction: int, row: int, col: int):
        # clean & mark
        robot.clean()
        self.visited.add((row, col))

        # try all 4 directions in order: forward, right, back, left
        for i in range(len(self.directions)):
            new_direction = (direction + i) % 4
            new_row = row + self.directions[new_direction][0]
            new_col = col + self.directions[new_direction][1]

            if (new_row, new_col) in self.visited or not robot.move():
                # rotate the robot to the right (so next i corresponds to
                # the next relative direction)
                robot.turnRight()
                continue

            self.dfs(robot, new_direction, new_row, new_col)
            robot.turnRight()

        # backtrack: go back to (row,col), restore orientation
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def cleanRoom(self, robot: Robot) -> None:
        """
        Time Complexity: O(N x M)
        Space Complexity: O(N x M)
        """
        direction = 0
        self.dfs(robot, direction, 0, 0)


if __name__ == "__main__":

    def test(room_map: List[List[int]], start_pos: Tuple[int, int]) -> None:

        print("Room before cleaning (X=start, .=uncleaned, #=wall):")
        visualize_map(room_map, start_pos=start_pos)

        robot = Robot(room_map, start_pos)
        Solution_489().cleanRoom(robot)

        cleaned = robot.get_cleaned(absolute=True)
        # print("\nCleaned cells (row, col):")
        # for r, c in sorted(cleaned):
        #     print(f"  ({r}, {c})")
        print("\nRoom after cleaning (C=cleaned, .=uncleaned, #=wall):")
        visualize_map(room_map, cleaned=cleaned)

    def visualize_map(room_map: List[List[int]], start_pos=None, cleaned=None):
        for i, row in enumerate(room_map):
            line = []
            for j, v in enumerate(row):
                if v == 1:
                    line.append("#")
                elif cleaned and (i, j) in cleaned:
                    line.append("C")
                elif start_pos and i == start_pos[0] and j == start_pos[1]:
                    line.append("X")
                else:
                    line.append(".")
            print("".join(line))

    # 0 = open/uncleaned cell, 1 = wall
    room_map = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    start_pos = (1, 2)  # row=1, col=2
    test(room_map, start_pos)

    print("-" * 100)
    room_map = [
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1],
    ]
    start_pos = (1, 2)  # row=1, col=2
    test(room_map, start_pos)

    print("-" * 100)
    start_pos = (0, 0)  # row=0, col=0
    test(room_map, start_pos)

    print("-" * 100)
    room_map = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 1, 1],
    ]
    start_pos = (0, 0)  # row=0, col=0
    test(room_map, start_pos)
