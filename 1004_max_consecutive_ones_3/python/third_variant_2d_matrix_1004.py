from typing import List

class Variant_1004_2DMatrix:
    def shrink_window(self, days: List[List[str]], left: List[int]) -> List[int]:
        cRow,cCol = left
        if cCol == len(days[0])-1:
            return [cRow+1,0]
        return [cRow,cCol+1]


    def getMaxVacations(self, days: List[List[str]], pto: int) -> int:
        max_vacation = 0
        cur_vacation = 0
        left = [0,0] #[row,col]
        m,n = len(days),len(days[0])
        for i in range(m):
            for j in  range(n):
                if days[i][j] == "W":
                    pto -=1
                cur_vacation +=1
                while pto < 0:
                    if days[left[0]][left[1]] == 'W':
                        pto+=1
                    left = self.shrink_window(days,left)
                    cur_vacation -=1
                max_vacation= max(max_vacation,cur_vacation)
        return max_vacation


def test_max_consecutive_ones_2d_matrix_variant():
    s = Variant_1004_2DMatrix()

    # All_Workdays
    days_all_work = [['W', 'W', 'W'],
                     ['W', 'W', 'W'],
                     ['W', 'W', 'W']]
    assert s.getMaxVacations(days_all_work, 0) == 0
    assert s.getMaxVacations(days_all_work, 1) == 1
    assert s.getMaxVacations(days_all_work, 2) == 2
    assert s.getMaxVacations(days_all_work, 3) == 3
    assert s.getMaxVacations(days_all_work, 4) == 4
    assert s.getMaxVacations(days_all_work, 5) == 5
    assert s.getMaxVacations(days_all_work, 6) == 6
    assert s.getMaxVacations(days_all_work, 7) == 7
    assert s.getMaxVacations(days_all_work, 8) == 8
    assert s.getMaxVacations(days_all_work, 9) == 9
    assert s.getMaxVacations(days_all_work, 10) == 9
    assert s.getMaxVacations(days_all_work, 9000) == 9

    # All_Holidays
    days_all_holidays = [['H', 'H', 'H'],
                         ['H', 'H', 'H'],
                         ['H', 'H', 'H']]
    assert s.getMaxVacations(days_all_holidays, 0) == 9
    assert s.getMaxVacations(days_all_holidays, 1) == 9
    assert s.getMaxVacations(days_all_holidays, 2) == 9
    assert s.getMaxVacations(days_all_holidays, 3) == 9
    assert s.getMaxVacations(days_all_holidays, 4) == 9
    assert s.getMaxVacations(days_all_holidays, 5) == 9
    assert s.getMaxVacations(days_all_holidays, 6) == 9
    assert s.getMaxVacations(days_all_holidays, 7) == 9
    assert s.getMaxVacations(days_all_holidays, 8) == 9
    assert s.getMaxVacations(days_all_holidays, 9) == 9
    assert s.getMaxVacations(days_all_holidays, 10) == 9
    assert s.getMaxVacations(days_all_holidays, 9000) == 9

    # Mixed_Workdays_Holidays
    days_mixed_1 = [['W', 'H', 'H'],
                    ['W', 'W', 'H'],
                    ['W', 'W', 'W']]
    assert s.getMaxVacations(days_mixed_1, 1) == 3
    assert s.getMaxVacations(days_mixed_1, 2) == 5
    assert s.getMaxVacations(days_mixed_1, 3) == 6
    assert s.getMaxVacations(days_mixed_1, 4) == 7
    assert s.getMaxVacations(days_mixed_1, 5) == 8
    assert s.getMaxVacations(days_mixed_1, 6) == 9
    assert s.getMaxVacations(days_mixed_1, 7) == 9
    assert s.getMaxVacations(days_mixed_1, 8) == 9
    assert s.getMaxVacations(days_mixed_1, 9) == 9
    assert s.getMaxVacations(days_mixed_1, 9000) == 9

    days_mixed_2 = [['W', 'H', 'W'],
                    ['H', 'W', 'H'],
                    ['W', 'H', 'W']]
    assert s.getMaxVacations(days_mixed_2, 1) == 3
    assert s.getMaxVacations(days_mixed_2, 2) == 5
    assert s.getMaxVacations(days_mixed_2, 3) == 7
    assert s.getMaxVacations(days_mixed_2, 4) == 8
    assert s.getMaxVacations(days_mixed_2, 5) == 9
    assert s.getMaxVacations(days_mixed_2, 6) == 9
    assert s.getMaxVacations(days_mixed_2, 7) == 9
    assert s.getMaxVacations(days_mixed_2, 8) == 9
    assert s.getMaxVacations(days_mixed_2, 9) == 9

    # Different_Dimensions
    days_dim_1 = [['W', 'H', 'H', 'W', 'W'],
                  ['H', 'W', 'W', 'W', 'W']]
    assert s.getMaxVacations(days_dim_1, 1) == 3
    assert s.getMaxVacations(days_dim_1, 2) == 5
    assert s.getMaxVacations(days_dim_1, 3) == 6
    assert s.getMaxVacations(days_dim_1, 4) == 7
    assert s.getMaxVacations(days_dim_1, 5) == 8
    assert s.getMaxVacations(days_dim_1, 6) == 9
    assert s.getMaxVacations(days_dim_1, 7) == 10
    assert s.getMaxVacations(days_dim_1, 8) == 10
    assert s.getMaxVacations(days_dim_1, 9) == 10
    assert s.getMaxVacations(days_dim_1, 9000) == 10

    days_dim_2 = [['W'],
                  ['H'],
                  ['H'],
                  ['W'],
                  ['W'],
                  ['H'],
                  ['W'],
                  ['W'],
                  ['W'],
                  ['W']]
    assert s.getMaxVacations(days_dim_2, 1) == 3
    assert s.getMaxVacations(days_dim_2, 2) == 5
    assert s.getMaxVacations(days_dim_2, 3) == 6
    assert s.getMaxVacations(days_dim_2, 4) == 7
    assert s.getMaxVacations(days_dim_2, 5) == 8
    assert s.getMaxVacations(days_dim_2, 6) == 9
    assert s.getMaxVacations(days_dim_2, 7) == 10
    assert s.getMaxVacations(days_dim_2, 8) == 10
    assert s.getMaxVacations(days_dim_2, 9) == 10
    assert s.getMaxVacations(days_dim_2, 9000) == 10

    print("All 2D matrix tests passed!")

if __name__ == "__main__":
    test_max_consecutive_ones_2d_matrix_variant()