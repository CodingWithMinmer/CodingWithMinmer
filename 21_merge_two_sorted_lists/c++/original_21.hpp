#pragma once

#include "utils/ListNode.hpp"

ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    auto curr = new ListNode(-1);
    auto head = curr;

    auto l1 = list1, l2 = list2;
    while (l1 != nullptr && l2 != nullptr) {
        if (l1->val <= l2->val) {
            curr->next = l1;
            l1 = l1->next;
        } else {
            curr->next = l2;
            l2 = l2->next;
        }

        curr = curr->next;
    }

    if (l1 != nullptr)
        curr->next = l1;
    else if (l2 != nullptr)
        curr->next = l2;

    return head->next;
}