#pragma once

#include <cassert>
#include <vector>
#include "../utils/Node.hpp"

// VARIANT: What if you had to optimize your solution for 10^4 function invocations?
// How would your algorithm change?
class RangeSumCalculator
{
    std::vector<int> vals;
    std::vector<int> prefix_sums;

    void inorder(Node* root) {
        if (root == nullptr)
            return;

        inorder(root->left);
        vals.push_back(root->val);
        if (prefix_sums.empty())
            prefix_sums.push_back(root->val);
        else
            prefix_sums.push_back(prefix_sums.back() + root->val);

        inorder(root->right);
    }
    int find_right_boundary(int left, int right, int upper) {
        while (left <= right) {
            int mid = (right - left)/2 + left;
            if (vals[mid] <= upper)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return right;
    }
    int find_left_boundary(int left, int right, int lower) {
        while (left <= right) {
            int mid = (right - left)/2 + left;
            if (vals[mid] >= lower)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return left;
    }
public:
    RangeSumCalculator(Node* root) {
        inorder(root);
    }
    int calculate(int lower, int upper) {
        int right_boundary = find_right_boundary(0, vals.size() - 1, upper);
        int left_boundary = find_left_boundary(0, vals.size() - 1, lower);
        if (left_boundary == 0)
            return prefix_sums[right_boundary];
        return prefix_sums[right_boundary] - prefix_sums[left_boundary - 1];
    }
};

void range_sum_calculator() {
    Node* root = new Node(10);
    root->left = new Node(5);
    root->left->left = new Node(3);
    root->left->left->left = new Node(1);
    root->left->right = new Node(7);
    root->left->right->left = new Node(6);

    root->right = new Node(15);
    root->right->left = new Node(13);
    root->right->right = new Node(18);

    RangeSumCalculator s(root);
    assert(s.calculate(5, 16) == 56);
    assert(s.calculate(0, 9000) == 1+3+5+6+7+10+13+15+18);
    assert(s.calculate(7, 7) == 7);
    assert(s.calculate(14, 18) == 33);
    assert(s.calculate(3, 6) == 14);
}