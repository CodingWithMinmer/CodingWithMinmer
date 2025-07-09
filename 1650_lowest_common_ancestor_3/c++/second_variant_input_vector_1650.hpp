#pragma once

#include <cassert>

#include "../utils/Node.hpp"
#include <vector>

// VARIANT: What if you were given all the nodes as a part of a vector, and no longer the root node?
Node* lowestCommonAncestor_second_variant_1650(std::vector<Node*>& nodes,
    Node* p_start,
    Node* q_start) {
    std::unordered_map<Node*, Node*> child_to_parent;
    for (auto node : nodes) {
        if (node->left != nullptr)
            child_to_parent[node->left] = node;
        if (node->right != nullptr)
            child_to_parent[node->right] = node;
    }
    auto p = p_start;
    auto q = q_start;
    while (p != q) {
        if (child_to_parent.contains(p))
            p = child_to_parent[p];
        else
            p = q_start;

        if (child_to_parent.contains(q))
            q = child_to_parent[q];
        else
            q = p_start;
    }

    return p;
}

void lowestCommonAncestor_second_variant_1650() {
    Node* root = new Node(1);
    root->left = new Node(2);
    Node* node_2 = root->left;

    root->left->left = new Node(4);
    Node* node_4 = root->left->left;

    root->left->right = new Node(5);
    Node* node_5 = root->left->right;

    root->left->right->right = new Node(6);
    Node* node_6 = root->left->right->right;

    root->left->right->right->left = new Node(7);
    Node* node_7 = root->left->right->right->left;

    root->right = new Node(3);
    Node* node_3 = root->right;

    std::vector nodes = {root, node_2, node_4, node_5, node_6, node_7, node_3};
    assert(node_2 == lowestCommonAncestor_second_variant_1650(nodes, node_4, node_7)); // different subtrees
    assert(node_3 == lowestCommonAncestor_second_variant_1650(nodes, node_3, node_3)); // same node, but not allowed as LC input due to constraints
    assert(node_5 == lowestCommonAncestor_second_variant_1650(nodes, node_5, node_6)); // same subtree and answer is p
    assert(node_5 == lowestCommonAncestor_second_variant_1650(nodes, node_5, node_7)); // same subtree
    assert(root == lowestCommonAncestor_second_variant_1650(nodes, root, node_3));
}