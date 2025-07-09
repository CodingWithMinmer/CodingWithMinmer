#pragma once

#include "../utils/Node.hpp"
#include <vector>
#include <queue>
#include <unordered_map>

class Solution_987 {
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
    std::vector<std::vector<int>> verticalTraversal(TreeNode* root) {
        std::unordered_map<int, std::vector<std::pair<TreeNode*, int>>> col_to_node_and_row;
        auto [leftmost_col, rightmost_column] = level_order_traversal(root, col_to_node_and_row);

        std::vector<std::vector<int>> result;
        for (int i = leftmost_col; i <= rightmost_column; i++) {
            std::sort(
                col_to_node_and_row[i].begin(), col_to_node_and_row[i].end(),
                [](auto& a, auto& b) {
                    int a_val = a.first->val;
                    int b_val = b.first->val;
                    int a_row = a.second;
                    int b_row = b.second;

                    if (a_row == b_row)
                        return a_val < b_val;
                    else
                        return a_row < b_row;
                });

            std::vector<int> curr_col;
            for (auto [node, row] : col_to_node_and_row[i])
                curr_col.push_back(node->val);
            result.push_back(curr_col);
        }

        return result;
    }
};