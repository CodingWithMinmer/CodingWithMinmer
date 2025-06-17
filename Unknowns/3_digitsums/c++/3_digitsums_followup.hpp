#pragma once

#include <vector>
#include <queue>

// FOLLOW-UP: What if the order in the output array mattered? It should be sorted in ascending order
// In the case of a tiebreak (of equal digit sums), prioritize the number with the lower index
class Kth_Smallest_DigitSums_Followup {
    struct comparator {
        bool operator()(const std::vector<int>& a, const std::vector<int>& b) const {
            if (a[0] != b[0])
                return a[0] < b[0];
            return a[2] < b[2];
        }
    };

    int compute(int num) {
        int digit_sum = 0;
        while (num != 0) {
            digit_sum += num % 10;
            num /= 10;
        }
        return digit_sum;
    }
public:
    std::vector<int> kthSmallestDigitSums(std::vector<int> numbers, int k) {
        std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, comparator> max_heap;
        for (int i = 0; i < numbers.size(); i++) {
            int digit_sum = compute(numbers[i]);
            max_heap.push({digit_sum, numbers[i], i});
            if (max_heap.size() > k)
                max_heap.pop();
        }

        std::vector<int> result;
        while (!max_heap.empty()) {
            result.push_back(max_heap.top()[1]);
            max_heap.pop();
        }
        std::reverse(result.begin(), result.end());
        return result;
    }
};
