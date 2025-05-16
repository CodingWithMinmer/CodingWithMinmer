from typing import List, Set, Tuple


# This is the mouse's control interface.
# You should not implement it, or speculate about its implementation.
class Mouse:
    """
    Test stub that *hides* absolute coords from Solution_489_Variant.
    Internally we keep:
      - self._room: the real 2D array of 0=open, 1=wall
      - self._abs_pos: the mouse's real (r,c) in that array
    Externally, Solution_489_Variant only ever sees a clean, unknown grid
    whose origin (0,0) is wherever the mouse started.
    """

    def __init__(self, room: List[List[int]], start_abs: Tuple[int, int]) -> None:
        self._room = room
        self._start_abs = start_abs
        self._abs_pos = start_abs

    # Returns true if the cell in the `direction` from current cell is open,
    # else returns false if the cell in front is unmovable, the mouse being
    # a dummy makes a move regardless.
    def move(self, direction: Tuple[int, int]) -> bool:
        # figure out what absolute cell is in front
        dr, dc = direction
        nr, nc = self._abs_pos[0] + dr, self._abs_pos[1] + dc

        # mouse commits the move first
        self._abs_pos = (nr, nc)
        # check bounds & walls
        if not (0 <= nr < len(self._room) and 0 <= nc < len(self._room[0])):
            return False
        if self._room[nr][nc] == 1:
            return False

        return True

    # Check the cell for cheese
    def hasCheese(self) -> bool:
        if self._room[self._abs_pos[0]][self._abs_pos[1]] == "C":
            return True
        return False


# VARIANT: Mouse tries to find cheese in a maze of unkown dimensions.
# SOURCE: https://youtu.be/vQZZSeuDRto?si=WNQdWiQb-TmWclik&t=810
class Solution_489_Variant:
    def __init__(self) -> None:
        self.directions: List[Tuple[int, int]] = [
            (-1, 0),  # up
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
        ]
        self.opposite_directions: List[Tuple[int, int]] = [
            (1, 0),  # down
            (0, -1),  # left
            (-1, 0),  # up
            (0, 1),  # right
        ]
        self.visited: Set[Tuple[int, int]] = set()

    def dfs(self, mouse: Mouse, row: int, col: int):
        # check for cheese
        if mouse.hasCheese():
            return True
        self.visited.add((row, col))

        # try all 4 directions in order: forward, right, back, left
        for i in range(len(self.directions)):
            new_direction = self.directions[i]
            new_row = row + new_direction[0]
            new_col = col + new_direction[1]

            if (new_row, new_col) in self.visited:
                continue
            elif not mouse.move(new_direction):
                mouse.move(self.opposite_directions[i])
                continue
            elif self.dfs(mouse, new_row, new_col):
                return True

            mouse.move(self.opposite_directions[i])

        return False

    def getCheese(self, mouse: Mouse) -> None:
        """
        Time Complexity: O(N x M)
        Space Complexity: O(N x M)
        """
        return self.dfs(mouse, 0, 0)


if __name__ == "__main__":

    # 0 = open cell, 1 = wall, "C" = cell with cheese
    room_map = [
        ["C", 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    start_pos = (1, 2)  # row=1, col=2
    mouse = Mouse(room=room_map, start_abs=start_pos)
    assert Solution_489_Variant().getCheese(mouse) == True

    # 0 = open cell, 1 = wall, "C" = cell with cheese
    room_map = [
        [0, 0, 0, 1],
        ["C", 1, 0, 0],
        [1, 1, 1, 1],
    ]
    start_pos = (1, 2)  # row=1, col=2
    mouse = Mouse(room=room_map, start_abs=start_pos)
    assert Solution_489_Variant().getCheese(mouse) == True

    room_map[1][0] = 0
    mouse = Mouse(room=room_map, start_abs=start_pos)
    assert Solution_489_Variant().getCheese(mouse) == False

    room_map = [
        [0, 0, 1],
        [0, 1, 1],
        ["C", 1, 1],
    ]
    start_pos = (0, 0)  # row=0, col=0
    mouse = Mouse(room=room_map, start_abs=start_pos)
    assert Solution_489_Variant().getCheese(mouse) == True
