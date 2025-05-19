from typing import List

class Variant:
    def shrink_window(self, days: List[List[str]], left: List[int]) -> List[int]:
        row, col = left[0], left[1]
        if col == len(days[0]) - 1:
            return [row + 1, 0]
        return [row, col + 1]

    def getMaxVacations(self, days: List[List[str]], pto: int) -> int:
        max_vacation = 0
        curr_vacation = 0
        left = [0, 0]
        for row in range(len(days)):
            for col in range(len(days[0])):
                if days[row][col] == 'W':
                    pto -= 1
                curr_vacation += 1

                while pto < 0:
                    if days[left[0]][left[1]] == 'W':
                        pto += 1
                    left = self.shrink_window(days, left)
                    curr_vacation -= 1

                max_vacation = max(curr_vacation, max_vacation)

        return max_vacation