#pragma once

#include <vector>
#include <queue>
#include "../utils/ListNode.hpp"

class Solution_23 {
    struct element {
        ListNode* node;
        bool operator>(const element& other) const {
            return node->val > other.node->val;
        }
    };
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        std::priority_queue<element, std::vector<element>, std::greater<element>> min_pq;
        for (auto list : lists)
            if (list != nullptr)
                min_pq.push(element{list});

        auto dummy = new ListNode(-1);
        auto c = dummy;
        while (!min_pq.empty()) {
            c->next = min_pq.top().node;
            min_pq.pop();

            c = c->next;
            if (c->next != nullptr)
                min_pq.push(element{c->next});
        }
        
        return dummy->next;
    }
};