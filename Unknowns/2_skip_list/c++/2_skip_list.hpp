#pragma once

struct SkipList
{
    struct Node
    {
        int val;
        Node* prev = nullptr;
        Node* next = nullptr;
        Node* top = nullptr;
        Node* bottom = nullptr;

        Node(int val) : val(val) {}
    };

    bool search(Node* root, int target) {
        if (root == nullptr)
            return false;
        if (root->val == target)
            return true;

        Node* c = root;
        while (c != nullptr) {
            while (c->next != nullptr && c->next->val <= target) {
                c = c->next;
                if (c->val == target)
                    return true;
            }
            c = c->bottom;
        }

        return false;
    }
};