#pragma once

#include "../utils/Node.hpp"
#include <algorithm>
#include <cassert>
#include <iostream>

// VARIANT: What if you had to ignore negative signs in your calculations until
// you reached a leaf node, and instead, only consider signage if a root-to-leaf path is
// a "negative path"?
void sumNumbers_second_variant_129(Node* root, 
                           int& total_sum, 
                           int curr_sum, 
                           int num_negatives) {
    if (root == nullptr)
        return;

    curr_sum = (curr_sum * 10) + std::abs(root->val);
    if (root->val < 0)
        num_negatives++;

    if (root->left == nullptr && root->right == nullptr) {
        int sign = num_negatives % 2 == 1 ? -1 : 1;
        total_sum += curr_sum * sign;
        return;
    }

    sumNumbers_second_variant_129(root->left, total_sum, curr_sum, num_negatives);
    sumNumbers_second_variant_129(root->right, total_sum, curr_sum, num_negatives);
}

int sumNumbers_second_variant_129(Node* root) {
    int total_sum = 0;
    int curr_sum = 0;
    int num_negatives = 0;
    sumNumbers_second_variant_129(root, total_sum, curr_sum, num_negatives);
    return total_sum;
}

void sumNumbers_second_variant_129() {
    Node* root = new Node(-1);
    root->left = new Node(-2);
    root->left->left = new Node(-9);
    root->right = new Node(4);
    root->right->left = new Node(-5);
    assert(-129 + 145 == sumNumbers_second_variant_129(root));

    root = new Node(-1);
    root->left = new Node(-2);
    root->left->left = new Node(-9);
    root->left->left->left = new Node(3);
    root->left->left->right = new Node(-3);
    root->right = new Node(4);
    root->right->left = new Node(-5);
    root->right->right = new Node(6);

    assert(-1293 + 1293 + 145 + -146 == sumNumbers_second_variant_129(root));

    root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    assert(12 + 13 == sumNumbers_second_variant_129(root));

    root = new Node(-1);
    root->left = new Node(-2);
    root->right = new Node(-3);
    assert(12 + 13 == sumNumbers_second_variant_129(root));

    root = new Node(-1);
    root->left = new Node(-2);
    root->left->left = new Node(-3);
    assert(-123 == sumNumbers_second_variant_129(root));

    root = nullptr;
    assert(0 == sumNumbers_second_variant_129(root));
}