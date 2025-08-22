#pragma once

#include "../utils/Node.hpp"
#include <unordered_map>

// VARIANT: What if you had to define the data structures yourself and clone the 
// disconnected graph?
Node* dfs_133_variant(Node* node, std::unordered_map<Node*, Node*>& old_to_new) {
    if (old_to_new.contains(node))
        return old_to_new[node];

    old_to_new[node] = new Node(node->val);

    for (auto neighbor : node->neighbors)
        old_to_new[node]->neighbors.push_back(dfs_133_variant(neighbor, old_to_new));

    return old_to_new[node];
}
Graph cloneGraph_133_first_variant(Graph input) {
    Graph output;
    for (Node* node : input.roots) {
        if (node == nullptr)
            continue;

        std::unordered_map<Node*, Node*> old_to_new;
        output.roots.push_back(dfs_133_variant(node, old_to_new));
    }

    return output;
}