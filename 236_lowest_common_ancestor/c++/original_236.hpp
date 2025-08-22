#pragma once

#include "../utils/Node.hpp"

TreeNode* dfs(TreeNode* node, TreeNode* p, TreeNode* q) {
    if (node == nullptr)
        return nullptr;
    if (node->val == p->val || node->val == q->val)
        return node;

    TreeNode* left_key_node = dfs(node->left, p, q);
    TreeNode* right_key_node = dfs(node->right, p, q);

    if (left_key_node != nullptr && right_key_node != nullptr)
        return node;
    else if (left_key_node != nullptr)
        return left_key_node;
    else if (right_key_node != nullptr)
        return right_key_node;
    return nullptr;
}

TreeNode* lowestCommonAncestor_236(TreeNode* root, TreeNode* p, TreeNode* q) {
    return dfs(root, p, q);
}
