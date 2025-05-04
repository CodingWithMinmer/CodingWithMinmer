#pragma once

#include <vector>
#include <queue>

// VARIANT: What if you had to merge K sorted integer arrays, no longer linked lists?
class Solution_23_First_Variant {
    struct element {
        int list_index;
        int index;
        int val;
        bool operator>(const element& other) const {
            return val > other.val;
        }
    };
public:
    std::vector<int> mergeKLists(std::vector<std::vector<int>>& lists) {
        std::priority_queue<element, std::vector<element>, std::greater<element>> min_pq;
        for (int i = 0; i < lists.size(); i++)
            if (!lists[i].empty())
                min_pq.push(element{i, 0, lists[i][0]});

        std::vector<int> result;
        while (!min_pq.empty()) {
            auto [list_index, index, val] = min_pq.top();
            min_pq.pop();

            result.push_back(val);

            index++;
            if (index < lists[list_index].size())
                min_pq.push(element{list_index, index, lists[list_index][index]});
        }

        return result;
    }
};