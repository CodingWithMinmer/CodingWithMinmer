#pragma once

#include <vector>

class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;
    Node* parent;
    Node* random;
    std::vector<Node*> children;
    std::vector<Node*> neighbors;

    Node() : val(0), left(nullptr), right(nullptr), next(nullptr), parent(nullptr) {}

    Node(int val) : val(val), left(nullptr), right(nullptr), next(nullptr), parent(nullptr) {}

    Node(int val, Node* _next) : val(val), next(_next) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
            : val(_val), left(_left), right(_right), next(_next) {}
};

class Graph {
public:
    std::vector<Node*> roots;
};

// As defined on Leetcode.com
class TreeNode {
    public:
        int val;
        TreeNode* left;
        TreeNode* right;
        TreeNode* next;
        TreeNode* parent;
        TreeNode* random;
        std::vector<TreeNode*> children;
        std::vector<TreeNode*> neighbors;
    
        TreeNode() : val(0), left(nullptr), right(nullptr), next(nullptr), parent(nullptr) {}
    
        TreeNode(int val) : val(val), left(nullptr), right(nullptr), next(nullptr), parent(nullptr) {}
    
        TreeNode(int _val, TreeNode* _left, TreeNode* _right, TreeNode* _next)
                : val(_val), left(_left), right(_right), next(_next) {}
    };
struct node_metadata {
    int row;
    int column;
    TreeNode* ref;
};