#pragma once

#include "../utils/Node.hpp"
#include <algorithm>
#include <cassert>
#include <iostream>

// VARIANT: What if you nodes could be larger than 9?
void sumNumbers_first_variant_129(Node* root, int& total_sum, int curr_sum)
{
    if (root == nullptr)
        return;

    int places = root->val == 0 ? 10 : 1; // This is a new line not from the video to capture an edgecase of node values of 0
    int node_val = root->val;
    while (node_val > 0) {
        node_val /= 10;
        places *= 10;
    }
    curr_sum = (curr_sum * places) + root->val;

    if (root->left == nullptr && root->right == nullptr) {
        total_sum += curr_sum;
        return;
    }

    sumNumbers_first_variant_129(root->left, total_sum, curr_sum);
    sumNumbers_first_variant_129(root->right, total_sum, curr_sum);
}


int sumNumbers_first_variant_129(Node* root) {
    int total_sum = 0;
    int curr_sum = 0;
    sumNumbers_first_variant_129(root, total_sum, curr_sum);
    return total_sum;
}

void sumNumbers_first_variant_129() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->left->left = new Node(90);
    root->right = new Node(42);
    root->right->left = new Node(511);
    assert(1290 + 142511 == sumNumbers_first_variant_129(root));

    root = new Node(1);
    root->left = new Node(2);
    root->left->left = new Node(912);
    root->left->left->left = new Node(3);
    root->left->left->right = new Node(4);
    root->right = new Node(46);
    root->right->left = new Node(5);
    root->right->right = new Node(61);

    assert(129123 + 129124 + 1465 + 14661 == sumNumbers_first_variant_129(root));

    root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    assert(12 + 13 == sumNumbers_first_variant_129(root));

    root = new Node(10);
    root->left = new Node(200);
    root->right = new Node(3000);
    assert(10200 + 103000 == sumNumbers_first_variant_129(root));

    root = new Node(10);
    root->left = new Node(0);
    root->right = new Node(0);
    assert(200 == sumNumbers_first_variant_129(root));

    root = nullptr;
    assert(0 == sumNumbers_first_variant_129(root));
}