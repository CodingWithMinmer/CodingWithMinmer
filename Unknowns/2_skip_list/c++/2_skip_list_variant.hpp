#pragma once

// VARIANT: What if you had to return the closest node whose value is equal or lower to the given target?
struct SkipList_Variant
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

    Node* search_closest(Node* root, int target) {
        if (root == nullptr)
            return nullptr;
        if (root->val == target)
            return root;

        Node* c = root;
        while (c->bottom != nullptr) {
            while (c->next != nullptr && c->next->val <= target) {
                c = c->next;
                if (c->val == target)
                    return c;
            }
            c = c->bottom;
        }

        while (c->next != nullptr && c->next->val <= target)
            c = c->next;
        return c;
    }
};