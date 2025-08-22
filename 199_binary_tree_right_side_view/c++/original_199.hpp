#pragma once

#include <vector>
#include <queue>
#include "../utils/Node.hpp"

std::vector<int> rightSideView(Node* root) {
    if (root == nullptr)
        return {};

    std::vector<int> result;
    std::queue<Node*> q;
    q.push(root);
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            Node* node = q.front();
            q.pop();

            if (size == i + 1)
                result.push_back(node->val);

            if (node->left != nullptr)
                q.push(node->left);
            if (node->right != nullptr)
                q.push(node->right);
        }
    }
    return result;
}