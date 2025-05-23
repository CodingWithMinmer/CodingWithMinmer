#pragma once

#include <cassert>
#include <iostream>
#include <vector>
#include <queue>
#include "../utils/Node.hpp"

// VARIANT: What if you had to return both the left- and right side views of a binary tree?
std::vector<int> get_left_right_side_views(Node* root) {
    if (root == nullptr)
        return {};

    std::vector<int> left_side;
    std::vector<int> right_side;
    std::queue<Node*> q;
    q.push(root);
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            auto node = q.front();
            q.pop();

            if (i == 0)
                left_side.push_back(node->val);
            if (size == i + 1)
                right_side.push_back(node->val);

            if (node->left != nullptr)
                q.emplace(node->left);
            if (node->right != nullptr)
                q.emplace(node->right);
        }
    }

    std::vector<int> result;
    for (int i = left_side.size() - 1; i >= 0; i--)
        result.push_back(left_side[i]);
    for (int i = 1; i < right_side.size(); i++)
        result.push_back(right_side[i]);
    return result;
}

void get_left_right_side_views() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->right->right = new Node(7);
    root->right->left = new Node(6);
    root->right->right->left = new Node(8);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    std::vector<int> expected = {8, 4, 2, 1, 3, 7, 8};
    assert(expected == get_left_right_side_views(root));

    root = new Node(1);
    expected = {1};
    assert(expected == get_left_right_side_views(root));

    root = new Node(1);
    root->left = new Node(2);
    root->left->left = new Node(3);
    expected = {3, 2, 1, 2, 3};
    assert(expected == get_left_right_side_views(root));

    root = new Node(1);
    root->left = new Node(2);
    expected = {2, 1, 2};
    assert(expected == get_left_right_side_views(root));

    root = nullptr;
    assert(get_left_right_side_views(root).empty());

    root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->right->left = new Node(5);
    root->right->left->right = new Node(6);
    root->right->left->right->right = new Node(7);
    root->left->right = new Node(4);
    expected = {7, 6, 4, 2, 1, 3, 5, 6, 7};
    assert(expected == get_left_right_side_views(root));
}