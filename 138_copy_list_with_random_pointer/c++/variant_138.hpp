#pragma once

#include <unordered_map>
#include "../utils/Node.hpp"

// VARIANT: What if you had to deep copy a binary tree, not a linked list?
Node* deepCopy(Node* node, std::unordered_map<Node*, Node*>& old_to_new) {
    if (node == nullptr)
        return nullptr;

    old_to_new[node] = new Node(node->val);
    old_to_new[node]->left = deepCopy(node->left, old_to_new);
    old_to_new[node]->right = deepCopy(node->right, old_to_new);

    return old_to_new[node];
}

void copyRandom(Node* node, std::unordered_map<Node*, Node*>& old_to_new) {
    if (node == nullptr)
        return;

    old_to_new[node]->random = old_to_new[node->random];

    copyRandom(node->left, old_to_new);
    copyRandom(node->right, old_to_new);
}

Node* copyRandomBinaryTree_variant_138(Node* root) {
    std::unordered_map<Node*, Node*> old_to_new;
    deepCopy(root, old_to_new);
    copyRandom(root, old_to_new);

    return old_to_new[root];
}