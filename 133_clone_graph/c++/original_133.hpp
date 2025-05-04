#pragma once

#include "../utils/Node.hpp"
#include <unordered_map>

Node* dfs_133(Node* node, std::unordered_map<Node*, Node*>& old_to_new) {
    if (old_to_new.contains(node))
        return old_to_new[node];

    old_to_new[node] = new Node(node->val);

    for (auto neighbor : node->neighbors)
        old_to_new[node]->neighbors.push_back(dfs_133(neighbor, old_to_new));

    return old_to_new[node];
}

Node* cloneGraph_133(Node* node) {
    if (node == nullptr)
        return nullptr;
    std::unordered_map<Node*, Node*> old_to_new;
    return dfs_133(node, old_to_new);
}