#pragma once

#include "../utils/Node.hpp"
#include <vector>
#include <queue>
#include <unordered_map>
#include <cassert>

// VARIANT: What if you had to return the sorted nodes in a single list?
class Solution_987_Second_Variant {
    struct node_metadata {
        int row;
        int column;
        TreeNode* node;
    };
    std::pair<int, int> level_order_traversal(
        TreeNode* root,
        std::unordered_map<int, std::vector<std::pair<TreeNode*, int>>>& col_to_node_and_row) {
        int leftmost_col = 0, rightmost_column = 0;
        std::queue<node_metadata> q;
        q.emplace(node_metadata{0, 0, root});
        while (!q.empty()) {
            auto [row, col, node] = q.front();
            q.pop();

            col_to_node_and_row[col].push_back(std::pair{node, row});
            if (col < leftmost_col)
                leftmost_col = col;
            else if (col > rightmost_column)
                rightmost_column = col;

            if (node->left != nullptr)
                q.emplace(node_metadata{row + 1, col - 1, node->left});
            if (node->right != nullptr)
                q.emplace(node_metadata{row + 1, col + 1, node->right});
        }

        return {leftmost_col, rightmost_column};
    }

public:
    std::vector<int> verticalTraversal(TreeNode* root) {
        std::unordered_map<int, std::vector<std::pair<TreeNode*, int>>> col_to_node_and_row;
        auto [leftmost_col, rightmost_col] = level_order_traversal(root, col_to_node_and_row);

        std::vector<int> result;
        for (int i = leftmost_col; i <= rightmost_col; i++) {
            std::sort(col_to_node_and_row[i].begin(), col_to_node_and_row[i].end(), [](auto& a, auto& b) {
                int a_val = a.first->val;
                int b_val = b.first->val;
                int a_row = a.second;
                int b_row = b.second;

                if (a_row == b_row)
                    return a_val < b_val;
                else
                    return a_row < b_row;
            });
            for (auto [node, row] : col_to_node_and_row[i])
                result.push_back(node->val);
        }
        return result;
    }
};
void verticalTraversal_987_second_variant() {
    TreeNode* root = new TreeNode(6);
    root->left = new TreeNode(8);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(15);
    root->left->left->right = new TreeNode(1);

    root->right = new TreeNode(7);
    root->right->right = new TreeNode(9);
    root->right->left = new TreeNode(10);

    std::vector<int> expected = {3, 8, 1, 6, 10, 15, 7, 9};
    Solution_987_Second_Variant s;
    assert(expected == s.verticalTraversal(root));
}