#pragma once
#include <vector>

class Variant_1004_DecimalPTO {
public:
    double getMaxVacations(std::vector<char>& days, double pto) {
        double max_vacation = 0.0;
        double whole_pto = static_cast<int>(pto);
        double partial_pto = pto - whole_pto;
        std::cout << "whole_pto " << whole_pto << std::endl;
        std::cout << "partial_pto " << partial_pto << std::endl;

        int left = 0;
        for (int right = 0; right < days.size(); right++) {
            if (days[right] == 'W')
                whole_pto--;

            while (whole_pto < 0) {
                if (days[left] == 'W')
                    whole_pto++;
                left++;
            }

            double extension = 0.0;
            if ((left > 0 && days[left - 1] == 'W') ||
               (right < days.size() - 1 && days[right + 1] == 'W'))
               extension = partial_pto;

            max_vacation = std::max(max_vacation, right - left + 1 + extension);
        }

        return max_vacation;
    }
};