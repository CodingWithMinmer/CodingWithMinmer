#pragma once

#include <unordered_map>
#include "../utils/ListNode.hpp"

ListNode* copyRandomList_138(ListNode* head) {
    std::unordered_map<ListNode*, ListNode*> old_to_new;
    auto c = head;
    while (c != nullptr) {
        old_to_new[c] = new ListNode(c->val);
        c = c->next;
    }

    c = head;
    while (c != nullptr) {
        old_to_new[c]->next = old_to_new[c->next];
        old_to_new[c]->random = old_to_new[c->random];
        c = c->next;
    }

    return old_to_new[head];
}