#pragma once
#include <unordered_map>

class LRUCache_146 {
    struct Node {
        int key;
        int value;
        Node* left;
        Node* right;
    
        Node(int key, int value) : key(key), value(value) {}
    };

    Node* head;
    Node* tail;
    int capacity;
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
LRUCache_146(int capacity) : capacity(capacity) {
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

        if (key_to_node.size() > capacity) {
            Node* curr = head->right;
            rewire_pointers(curr);
            key_to_node.erase(curr->key);
        }
    }
};