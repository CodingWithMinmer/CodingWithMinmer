#pragma once

#include <vector>

// VARIANT: What if you had to return the number of flowers you can place?
class Solution_605_Variant {
public:
    int placeFlowers(std::vector<int>& flowerbed) {
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
        }

        return placed;
    }
};
