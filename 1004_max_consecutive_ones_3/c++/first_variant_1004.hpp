#pragma once

#include <vector>

// VARIANT: What if Meta presents the OG problem in the context of PTO days you want to take off?
// Specifically, you're given a char array of 'W' for work days and 'H' for weekends.
int longestVacationTimeFirstVariant(std::vector<char>& days, int pto) {
    int max_vacation = 0;
    int left = 0;
    for (int right = 0; right < days.size(); right++) {
        if (days[right] == 'W')
            pto--;

        while (pto < 0) {
            if (days[left] == 'W')
                pto++;
            left++;
        }

        max_vacation = std::max(max_vacation, right - left + 1);
    }

    return max_vacation;
}

void longestVacationTimeFirstVariant() {
	std::vector<char> days = {'W', 'H', 'H', 'W', 'W', 'H', 'W'};
	int pto = 2;
    assert(5 == longestVacationTimeFirstVariant(days, pto));

    days = {'W', 'W', 'H', 'H', 'W', 'W', 'W'};
    pto = 0;
    assert(2 == longestVacationTimeFirstVariant(days, pto));

    days = {'W', 'W', 'H', 'H', 'W', 'W', 'W'};
    pto = 5;
    assert(7 == longestVacationTimeFirstVariant(days, pto));

    days = {'W', 'W', 'H', 'H', 'W', 'W', 'W'};
    pto = 10;
    assert(7 == longestVacationTimeFirstVariant(days, pto));

    days = {'H', 'H', 'H', 'H', 'H', 'H', 'H'};
    pto = 0;
    assert(7 == longestVacationTimeFirstVariant(days, pto));

    days = {'W', 'H', 'W', 'W', 'W', 'H', 'W', 'H'};
    pto = 1;
    assert(3 == longestVacationTimeFirstVariant(days, pto));
}
