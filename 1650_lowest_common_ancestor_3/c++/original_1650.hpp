#pragma once

#include "../utils/Node.hpp"

Node* lowestCommonAncestor_1650(Node* p_start, Node* q_start) {
    Node* p = p_start;
    Node* q = q_start;
    while (p != q) {
        if (p->parent != nullptr)
            p = p->parent;
        else
            p = q_start;

        if (q->parent != nullptr)
            q = q->parent;
        else
            q = p_start;
    }
    return p;
}