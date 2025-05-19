from typing import List

class Variant:
    def getMaxVacations(self, days: List[str], pto: float) -> float:
        max_vacation = 0.0
        whole_pto, partial_pto = int(pto), pto - int(pto)
        left = 0
        for right in range(len(days)):
            if days[right] == 'W':
                whole_pto -= 1

            while whole_pto < 0:
                if days[left] == 'W':
                    whole_pto += 1
                left += 1

            extension = 0.0
            if left > 0 and days[left - 1] == 'W' or \
               right < len(days) - 1 and days[right + 1] == 'W':
               extension = partial_pto

            max_vacation = max(max_vacation, right - left + 1 + extension)

        return max_vacation