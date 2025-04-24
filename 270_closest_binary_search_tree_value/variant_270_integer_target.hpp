#pragma once

#include <climits>
#include "../utils/Node.hpp"

// VARIANT: What if the target parameter was given as an integer, not a double?
class Solution_270_Variant {
public:
    int closestValue(TreeNode* root, int target) {
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

            if (root->val > target)
                root = root->left;
            else
                root = root->right;
        }
        return result;
    }
};