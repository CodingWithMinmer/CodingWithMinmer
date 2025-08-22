#pragma once

#include <vector>

// VARIANT: What if Meta presents the OG problem in the context of PTO days you want to take off?
// Specifically, you're given a vector of booleans where T means it's a weekend, and F means
// it's a week day.
int longestVacationTimeSecondVariant(std::vector<bool>& year, int pto) {
    int max_vacation = 0;
    int left = 0;
    for (int right = 0; right < year.size(); right++) {
        if (!year[right])
            pto--;

        while (pto < 0) {
            if (!year[left])
                pto++;
            left++;
        }

        max_vacation = std::max(max_vacation, right - left + 1);
    }

    return max_vacation;
}

void longestVacationTimeSecondVariant() {
	std::vector<bool> year = {false, true, true, false, false, true, false};
	int pto = 2;
    assert(5 == longestVacationTimeSecondVariant(year, pto));

    year = {false, false, true, true, false, false, false};
    pto = 0;
    assert(2 == longestVacationTimeSecondVariant(year, pto));

    year = {false, false, true, true, false, false, false};
    pto = 5;
    assert(7 == longestVacationTimeSecondVariant(year, pto));

    year = {false, false, true, true, false, false, false};
    pto = 10;
    assert(7 == longestVacationTimeSecondVariant(year, pto));

    year = {true, true, true, true, true, true, true};
    pto = 0;
    assert(7 == longestVacationTimeSecondVariant(year, pto));

    year = {false, true, false, false, false, true, false, true};
    pto = 1;
    assert(3 == longestVacationTimeSecondVariant(year, pto));
}
