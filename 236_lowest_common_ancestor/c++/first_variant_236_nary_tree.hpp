#pragma once

#include "../utils/Node.hpp"

// VARIANT: What if you were given an N-ary Tree as the input, no longer a binary tree?
Node* lowestCommonAncestor_236_variant(Node* node, Node* p, Node* q) {
    if (node == nullptr)
        return nullptr;
    if (node->val == p->val || node->val == q->val)
        return node;

    std::vector<Node*> key_nodes;
    for (Node* child : node->children) {
        auto key_node = lowestCommonAncestor_236_variant(child, p, q);
        if (key_node != nullptr)
            key_nodes.push_back(key_node);
    }

    if (key_nodes.size() == 2)
        return node;
    else if (key_nodes.size() == 1)
        return key_nodes[0];
    else
        return nullptr;
}

