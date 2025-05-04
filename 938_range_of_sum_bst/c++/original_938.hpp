#pragma once

#include <stack>
#include "../utils/Node.hpp"

int rangeSumBST(Node* root, int low, int high) {
    int sum = 0;
    std::stack<Node*> stack;
    stack.push(root);
    while (!stack.empty()) {
        auto curr = stack.top();
        stack.pop();
        if (curr->val >= low && curr->val <= high)
            sum += curr->val;

        if (curr->right != nullptr && curr->val < high)
            stack.push(curr->right);
        if (curr->left != nullptr && curr->val > low)
            stack.push(curr->left);
    }
    return sum;
}
