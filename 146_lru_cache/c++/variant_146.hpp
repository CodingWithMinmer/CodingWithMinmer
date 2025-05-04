#pragma once
#include <unordered_map>

// VARIANT: What if you had to implement two more functions: the del(key) and last() functions?
class LRUCache_146_Variant {
    struct Node {
        int key;
        int value;
        Node* left;
        Node* right;

        Node(int key, int value) : key(key), value(value) {}
    };

    Node* head;
    Node* tail;
    std::unordered_map<int, Node*> key_to_node;

    void move_to_end(Node* curr) {
        auto before = tail->left;

        before->right = curr;
        curr->left = before;

        curr->right = tail;
        tail->left = curr;
    }

    void rewire_pointers(Node* curr) {
        auto before = curr->left;
        auto after = curr->right;
        before->right = after;
        after->left = before;
    }
public:
LRUCache_146_Variant() {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->right = tail;
        tail->left = head;
    }

    int get(int key) {
        if (!key_to_node.contains(key))
            return -1;

        Node* curr = key_to_node[key];
        int value = curr->value;

        rewire_pointers(curr);
        move_to_end(curr);

        return value;
    }

    void put(int key, int value) {
        if (key_to_node.contains(key)) {
            Node* curr = key_to_node[key];
            rewire_pointers(curr);
            key_to_node.erase(key);
        }

        Node* inserted = new Node(key, value);
        key_to_node[key] = inserted;
        move_to_end(inserted);
    }

    bool del(int key) {
        if (!key_to_node.contains(key))
            return false;

        Node* removed = key_to_node[key];
        rewire_pointers(removed);
        key_to_node.erase(key);
        return true;
    }

    int last() {
        if (tail->left == head)
            return -1;
        return tail->left->value;
    }
};