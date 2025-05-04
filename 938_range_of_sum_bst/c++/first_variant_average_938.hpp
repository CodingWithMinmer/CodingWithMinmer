#pragma once

#include <cassert>
#include <stack>
#include "../utils/Node.hpp"

// VARIANT: What if you had to return the average of all the nodes within the
// lower and upper range? 
// Note sometimes you are expected to use integer divison for the average, other times
// it's floating point division.
double average_of_bst(Node* root, int low, int high) {
    double sum = 0;
    double count = 0;
    std::stack<Node*> stack;
    stack.push(root);
    while (!stack.empty()) {
        auto curr = stack.top();
        stack.pop();
        if (curr->val >= low && curr->val <= high) {
            sum += curr->val;
            count++;
        }

        if (curr->right != nullptr && curr->val < high)
            stack.push(curr->right);
        if (curr->left != nullptr && curr->val > low)
            stack.push(curr->left);
    }
    return sum / count;
}

void average_of_bst() {
    Node* root = new Node(10);
    root->left = new Node(5);
    root->left->left = new Node(3);
    root->left->right = new Node(7);

    root->right = new Node(15);
    root->right->right = new Node(18);

    assert(average_of_bst(root, 7, 15) == 32.0/3.0);
    assert(average_of_bst(root, 0, 9000) == 58.0/6.0);
    assert(average_of_bst(root, 7, 7) == 7.0);
    assert(average_of_bst(root, 14, 18) == 33.0/2.0);
    assert(average_of_bst(root, 3, 6) == 4.0);
}