from typing import List

class Variant_1004_DecimalPTO:
    def getMaxVacations(self, days: List[str], pto: float) -> float:
        pto,pto_extension = int(pto), pto -int(pto)
        maxHoliday = 0
        left = 0
        for right in range(len(days)):
            if days[right]=='W':
                pto -=1
            while pto < 0:
                if days[left] == 'W':
                    pto +=1
                left +=1
            extension = 0.0
            if left > 0 and days[left-1] == 'W' or (right < len(days)-1 and days[right +1] == 'W'):
                extension = pto_extension
            maxHoliday = max(maxHoliday,right -left + 1 + extension)
        return maxHoliday
    
def test_max_consecutive_ones_decimal_pto_variant():
    s = Variant_1004_DecimalPTO()

    # OG_Problem
    assert s.getMaxVacations(['H', 'H', 'W', 'W'], 0.0) == 2.0
    assert s.getMaxVacations(['W', 'H', 'H', 'W', 'W', 'H', 'W'], 2.0) == 5.0
    assert s.getMaxVacations(['W', 'W', 'H', 'H', 'W', 'W', 'W'], 0.0) == 2.0
    assert s.getMaxVacations(['W', 'H', 'H', 'W', 'W', 'H', 'W'], 5.0) == 7.0
    assert s.getMaxVacations(['W', 'H', 'H', 'W', 'W', 'H', 'W'], 10.0) == 7.0
    assert s.getMaxVacations(['H', 'H', 'H', 'H', 'H', 'H', 'H'], 0.0) == 7.0
    assert s.getMaxVacations(['W', 'H', 'W', 'W', 'W', 'H', 'W', 'H'], 1.0) == 3.0
    assert s.getMaxVacations(['H', 'H', 'H', 'H', 'H', 'H'], 2.0) == 6.0
    assert s.getMaxVacations(['W', 'H', 'H', 'W', 'W', 'H', 'H', 'H', 'H', 'H'], 2.0) == 9.0

    # Half_PTO_Days
    res = s.getMaxVacations(['W', 'H'], 0.5)
    assert s.getMaxVacations(['W', 'H'], 0.5) == 1.5,print(f'Got {res}')
    assert s.getMaxVacations(['H', 'W'], 0.5) == 1.5
    assert s.getMaxVacations(['H', 'H', 'W', 'W', 'W'], 2.5) == 4.5
    assert s.getMaxVacations(['H', 'H', 'W', 'W'], 2.5) == 4.0
    assert s.getMaxVacations(['H', 'W', 'H', 'W', 'H', 'W', 'H', 'W', 'H'], 3.0) == 7.0
    assert s.getMaxVacations(['H', 'H', 'H', 'W', 'W', 'W', 'H', 'H', 'H', 'H', 'W'], 2.5) == 6.5
    assert s.getMaxVacations(['W', 'W', 'W', 'W'], 1.5) == 1.5
    assert s.getMaxVacations(['H', 'W', 'H', 'H', 'W', 'H', 'H', 'W', 'H', 'H', 'H'], 2.5) == 9.5

    # Other_Partial_PTOs
    assert s.getMaxVacations(['W', 'W', 'W', 'W', 'W', 'W', 'W'], 3.2) == 3.2
    assert s.getMaxVacations(['W', 'H', 'W', 'H', 'W', 'H', 'H', 'H'], 1.1) == 5.1
    assert s.getMaxVacations(['W', 'H', 'W'], 2.85) == 3.0
    assert s.getMaxVacations(['W', 'H', 'W'], 1.5) == 2.5

    # NoPTO_TakeNoDaysOff
    assert s.getMaxVacations(['W', 'W', 'W', 'W'], 0.0) == 0.0
    assert s.getMaxVacations(['H', 'H', 'H', 'H'], 0.0) == 4.0

    # TooManyPTO_AllDaysOff
    assert s.getMaxVacations(['H', 'H', 'W', 'W'], 50.0) == 4.0
    assert s.getMaxVacations(['W', 'W', 'W', 'W', 'W', 'W', 'W'], 50.0) == 7.0
    assert s.getMaxVacations(['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], 50.0) == 8.0
    assert s.getMaxVacations(['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], 0.0) == 8.0
    assert s.getMaxVacations([], 0.0) == 0.0
    assert s.getMaxVacations([], 50.0) == 0.0

    print("All tests passed!")

if __name__ == "__main__":
    test_max_consecutive_ones_decimal_pto_variant()