#pragma once

#include <cassert>
#include <vector>
#include <string>

// VARIANT: What if you had to return the city that a person lives in? The input is given very differently.
class Solution_variant_528 {
    std::vector<std::pair<std::string, int>> prefix_sums;
public:
    Solution_variant_528(std::vector<std::pair<std::string, int>>& city_populations) {
        for (auto [city, population] : city_populations) {
            if (prefix_sums.empty())
                prefix_sums.push_back({city, population});
            else
                prefix_sums.push_back({city, population + prefix_sums.back().second});
        }
    }

    std::string pickIndexWrapper(int generated_person) {
        return pickIndex(generated_person);
    }

    std::string pickIndex(int override) {
        int person = override == 0 ? rand() % prefix_sums.back().second : override;
        int left = 0, right = prefix_sums.size() - 1;
        while (left <= right) {
            int mid = (right - left)/2 + left;

            if (person < prefix_sums[mid].second)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return prefix_sums[left].first;
    }
};

void pickIndex() {
    std::vector<std::pair<std::string, int>> input = {
        {"US", 300}, {"VN", 100}, {"BR", 200}
    };
    Solution_variant_528 s(input);
    assert(s.pickIndexWrapper(0) == "US");
    assert(s.pickIndexWrapper(150) == "US");
    assert(s.pickIndexWrapper(299) == "US");

    assert(s.pickIndexWrapper(300) == "VN");
    assert(s.pickIndexWrapper(375) == "VN");
    assert(s.pickIndexWrapper(399) == "VN");

    assert(s.pickIndexWrapper(400) == "BR");
    assert(s.pickIndexWrapper(420) == "BR");
    assert(s.pickIndexWrapper(599) == "BR");
}