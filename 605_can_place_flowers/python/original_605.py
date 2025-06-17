from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        placed = 0
        while i < len(flowerbed):
            empty_left_plot = 0 if i == 0 else flowerbed[i - 1]
            empty_right_plot = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]
            if flowerbed[i] == empty_left_plot == empty_right_plot == 0:
                placed += 1
                i += 2
            elif flowerbed[i]:
                i += 2 
            else:
                i += 3
            if placed >= n:
                return True

        return False