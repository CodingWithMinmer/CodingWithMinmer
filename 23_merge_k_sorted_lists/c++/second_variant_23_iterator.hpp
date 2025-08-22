#pragma once

#include <vector>
#include <queue>

// VARIANT: What if you had to merge K sorted integer arrays an an iterator?
class Solution_23_Second_Variant {
    struct element {
        int list_index;
        int index;
        int val;
    
        bool operator>(const element& other) const {
            return val > other.val;
        }
    };
    std::priority_queue<element, std::vector<element>, std::greater<element>> min_pq;
    std::vector<std::vector<int>>& lists;
public:
Solution_23_Second_Variant(std::vector<std::vector<int>>& lists) : lists(lists) {
        for (int i = 0; i < lists.size(); i++)
            if (!lists[i].empty())
                min_pq.push(element{i, 0, lists[i][0]});
    }

    bool hasNext() {
        return !min_pq.empty();
    }

    int next() {
        if (!hasNext())
            throw std::out_of_range("No more elements left");

        auto [list_index, index, val] = min_pq.top();
        min_pq.pop();

        index++;
        if (index < lists[list_index].size())
            min_pq.push(element{list_index, index, lists[list_index][index]});
        return val;
    }
};