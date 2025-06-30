#pragma once

#include "../utils/Node.hpp"

int diameterOfBinaryTree(Node* node, int& diameter) {
    if (node == nullptr)
        return 0;

    int left_height = diameterOfBinaryTree(node->left, diameter);
    int right_height = diameterOfBinaryTree(node->right, diameter);

    diameter = std::max(diameter, left_height + right_height);

    return std::max(left_height, right_height) + 1;
}

int diameterOfBinaryTree(Node* root) {
    int diameter = 0;
    diameterOfBinaryTree(root, diameter);
    return diameter;
}