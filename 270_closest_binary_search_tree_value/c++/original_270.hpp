#pragma once

#include "../utils/Node.hpp"

class Solution_270 {
public:
    int closestValue(TreeNode* root, double target) {
        int closest_distance = INT_MAX;
        int result;
        while (root != nullptr) {
            int distance = std::abs(root->val - target);
            if (distance < closest_distance ||
                (distance == closest_distance && root->val < result)) {
                closest_distance = distance;
                result = root->val;
            }

            if (distance == 0)
                return root->val;

            if (root->val < target)
                root = root->right;
            else
                root = root->left;
        }
        return result;
    }
};