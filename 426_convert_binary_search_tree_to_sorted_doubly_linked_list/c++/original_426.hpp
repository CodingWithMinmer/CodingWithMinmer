#pragma once

#include "../utils/Node.hpp"

class Solution_426 {
    void dfs(Node* c, Node*& p, Node*& head) {
        if (c == nullptr)
            return;

        dfs(c->left, p, head);
        if (p == nullptr)
            head = c;
        else
            p->right = c, c->left = p;
        p = c;

        dfs(c->right, p, head);
    }

public:
    Node* treeToDoublyList_426(Node* root) {
        if (root == nullptr)
            return nullptr;

        Node* p = nullptr;
        Node* head = nullptr;
        dfs(root, p, head);

        head->left = p;
        p->right = head;

        return head;
    }
};