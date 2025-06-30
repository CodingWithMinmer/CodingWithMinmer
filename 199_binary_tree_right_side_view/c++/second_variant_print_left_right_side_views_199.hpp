#pragma once

#include <iostream>
#include <vector>
#include <queue>
#include "../utils/Node.hpp"

// VARIANT: What if you had to print to console the left and right side views?
void print_left_right_side_views(Node* root) {
    if (root == nullptr)
        return;
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
                q.push(node->left);
            if (node->right != nullptr)
                q.push(node->right);
        }
    }
    for (int i = left_side.size() - 1; i >= 0; i--)
        std::cout << left_side[i] << ' ';
    for (int i = 1; i < right_side.size(); i++)
        std::cout << right_side[i] << ' ';
}

void print_left_right_side_views() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->right->right = new Node(7);
    root->right->left = new Node(6);
    root->right->right->left = new Node(8);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    print_left_right_side_views(root); // 8 4 2 1 3 7 8
    std::cout << std::endl;

    root = new Node(1);
    print_left_right_side_views(root); // 1
    std::cout << std::endl;

    root = nullptr;
    print_left_right_side_views(root); //
    std::cout << std::endl;

    root = new Node(1);
    root->left = new Node(2);
    root->left->left = new Node(3);
    print_left_right_side_views(root); // 3 2 1 2 3
    std::cout << std::endl;
}