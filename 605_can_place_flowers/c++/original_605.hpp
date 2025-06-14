#pragma once

#include <vector>

class Solution_605_OG {
public:
    bool canPlaceFlowers(std::vector<int>& flowerbed, int n) {
        int i = 0;
        int placed = 0;
        while (i < flowerbed.size()) {
            int empty_left_plot = (i == 0) ? 0 : flowerbed[i - 1];
            int empty_right_plot = (i == flowerbed.size() - 1) ? 0 : flowerbed[i + 1];

            if (flowerbed[i] == 0 && empty_left_plot == 0 && empty_right_plot == 0) {
                placed++;
                i += 2;
            }
            else if (flowerbed[i] == 1)
                i += 2;
            else
                i += 3;

            if (placed >= n)
                return true;
        }

        return false;
    }
};
