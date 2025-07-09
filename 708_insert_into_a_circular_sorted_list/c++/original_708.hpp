#pragma once

#include "../../utils/Node.hpp"

class Solution708 {
public:
    Node* insert(Node* head, int insertVal) {
        if (head == nullptr) {
            auto node = new Node(insertVal);
            node->next = node;
            return node;
        }

        auto prev = head;
        auto curr = head->next;
        while (true) {
            if (prev->val <= insertVal && insertVal <= curr->val)
                break;
            if (prev->val > curr->val && (insertVal >= prev->val || insertVal <= curr->val))
                break;
            
            prev = curr;
            curr = curr->next;
            if (prev == head)
                break;
        }

        prev->next = new Node(insertVal, curr);
        return head;
    }
};