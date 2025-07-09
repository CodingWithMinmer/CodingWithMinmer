#include <gtest/gtest.h>
#include "../708_insert_into_a_circular_sorted_list/c++/variant_708_return_new_node.hpp"

TEST(InsertSortedCircularLinkedList_Variant_ReturnNewNode, HappyCase) {
    auto head = new Node(5);
    head->next = new Node(10, new Node(10, new Node(15, new Node(20, head))));
    Solution708 s;
    auto node = s.insert(head, 19);
    EXPECT_EQ(19, node->val);
    EXPECT_EQ(20, node->next->val);
    EXPECT_EQ(5, node->next->next->val);
    EXPECT_EQ(10, node->next->next->next->val);
    EXPECT_EQ(10, node->next->next->next->next->val);
    EXPECT_EQ(15, node->next->next->next->next->next->val);
    EXPECT_EQ(19, node->next->next->next->next->next->next->val);

    head = new Node(5);
    head->next = new Node(10, new Node(10, new Node(15, new Node(20, head))));
    node = s.insert(head, 10);
    EXPECT_EQ(10, node->val);
    EXPECT_EQ(10, node->next->val);
    EXPECT_EQ(10, node->next->next->val);
    EXPECT_EQ(15, node->next->next->next->val);
    EXPECT_EQ(20, node->next->next->next->next->val);
    EXPECT_EQ(5, node->next->next->next->next->next->val);
    EXPECT_EQ(10, node->next->next->next->next->next->next->val);
}

TEST(InsertSortedCircularLinkedList_Variant_ReturnNewNode, OutOfRange) {
    auto head = new Node(666);
    head->next = new Node(9000, new Node(420, head));
    Solution708 s;
    auto node = s.insert(head, 9500);
    EXPECT_EQ(9500, node->val);
    EXPECT_EQ(420, node->next->val);
    EXPECT_EQ(666, node->next->next->val);
    EXPECT_EQ(9000, node->next->next->next->val);
    EXPECT_EQ(9500, node->next->next->next->next->val);

    head = new Node(666);
    head->next = new Node(9000, new Node(420, head));
    node = s.insert(head, 10);
    EXPECT_EQ(10, node->val);
    EXPECT_EQ(420, node->next->val);
    EXPECT_EQ(666, node->next->next->val);
    EXPECT_EQ(9000, node->next->next->next->val);
    EXPECT_EQ(10, node->next->next->next->next->val);
}

TEST(InsertSortedCircularLinkedList_Variant_ReturnNewNode, NullHead) {
    Solution708 s;
    auto head = s.insert(nullptr, 9000);
    EXPECT_EQ(9000, head->val);
    EXPECT_EQ(head, head->next);
}

TEST(InsertSortedCircularLinkedList_Variant_ReturnNewNode, TestAllDuplicates) {
    auto head = new Node(7);
    head->next = new Node(7, new Node(7, head));
    Solution708 s;
    auto node = s.insert(head, 1);
    EXPECT_EQ(1, node->val);
    EXPECT_EQ(7, node->next->val);
    EXPECT_EQ(7, node->next->next->val);
    EXPECT_EQ(7, node->next->next->next->val);
    EXPECT_EQ(1, node->next->next->next->next->val);
}