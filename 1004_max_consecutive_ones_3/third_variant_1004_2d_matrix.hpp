#pragma once
#include <vector>

class Variant_1004_2DMatrix {
public:
    std::vector<int> shrink_window(std::vector<std::vector<char>>& days, std::vector<int> left) {
        int row = left[0];
        int col = left[1];
        if (col == days[0].size() - 1)
            return {row + 1, 0};
        return {row, col + 1};
    }

    int getMaxVacations(std::vector<std::vector<char>> days, int pto) {
        int max_vacation = 0;
        int curr_vacation = 0;
        std::vector<int> left = {0, 0};
        for (int row = 0; row < days.size(); row++) {
            for (int col = 0; col < days[0].size(); col++) {
                if (days[row][col] == 'W')
                    pto--;
                curr_vacation++;
    
                while (pto < 0) {
                    if (days[left[0]][left[1]] == 'W')
                        pto++;
                    left = shrink_window(days, left);
                    curr_vacation--;
                }

                max_vacation = std::max(curr_vacation, max_vacation);
            }
        }

        return max_vacation;
    }
};