#include <gtest/gtest.h>
#include "../../Unknowns/2_skip_list/c++/2_skip_list_variant.hpp"

class SkipListVariantBuilder {
    std::vector<SkipList_Variant::Node*> create_level(std::vector<int> vals) {
        std::vector<SkipList_Variant::Node*> l;
        for (int val : vals)
            l.push_back(new SkipList_Variant::Node(val));
        return l;
    }

    void wire_pointers_horizontally(std::vector<SkipList_Variant::Node*>& level) {
        for (int i = 1; i < level.size(); ++i) {
            level[i - 1]->next = level[i];
            level[i]->prev = level[i - 1];
        }
    }

    void wire_pointers_vertically(std::vector<SkipList_Variant::Node*>& top_nodes, std::vector<SkipList_Variant::Node*>& bottom_nodes) {
        std::unordered_map<int, SkipList_Variant::Node*> val_to_node;
        for (auto node : bottom_nodes)
            val_to_node[node->val] = node;

        for (auto top_node : top_nodes) {
            if (val_to_node.count(top_node->val)) {
                auto bottom_node = val_to_node[top_node->val];
                top_node->bottom = bottom_node;
                bottom_node->top = top_node;
            }
        }
    }
public:
    std::vector<std::vector<SkipList_Variant::Node*>> create() {
        auto level1 = create_level({10, 20, 30, 40, 50, 60, 70, 80, 90, 100});
        wire_pointers_horizontally(level1);

        auto level2 = create_level({10, 30, 50, 80, 100});
        wire_pointers_horizontally(level2);

        auto level3 = create_level({10, 50, 100});
        wire_pointers_horizontally(level3);

        auto level4 = create_level({10, 100});
        wire_pointers_horizontally(level4);

        wire_pointers_vertically(level4, level3);
        wire_pointers_vertically(level3, level2);
        wire_pointers_vertically(level2, level1);

        return {level4, level3, level2, level1};
    }
};

TEST(Unknown_SkipList_Variant, OG_Tests) {
    SkipListVariantBuilder builder;
    auto root = builder.create()[0][0];
    SkipList_Variant s;
    EXPECT_TRUE(s.search_closest(root, 70));
    EXPECT_TRUE(s.search_closest(root, 80));
    EXPECT_TRUE(s.search_closest(root, 60));
    EXPECT_TRUE(s.search_closest(root, 10));
    EXPECT_TRUE(s.search_closest(root, 20));
    EXPECT_TRUE(s.search_closest(root, 30));
    EXPECT_TRUE(s.search_closest(root, 50));
}

TEST(Unknown_SkipList_Variant, Search_Closest) {
    SkipListVariantBuilder builder;
    auto levels = builder.create();
    auto level4 = levels[0];
    auto root = level4[0];
    auto level3 = levels[1];
    auto level2 = levels[2];
    auto level1 = levels[3];
    SkipList_Variant s;
    EXPECT_EQ(s.search_closest(nullptr, 5), nullptr);
    EXPECT_EQ(s.search_closest(root, 5), level1[0]);
    EXPECT_EQ(s.search_closest(root, 10), level4[0]);

    EXPECT_EQ(s.search_closest(root, 70), level1[6]);
    EXPECT_EQ(s.search_closest(root, 15), level1[0]);
    EXPECT_EQ(s.search_closest(root, 22), level1[1]);
    EXPECT_EQ(s.search_closest(root, 35), level1[2]);
    EXPECT_EQ(s.search_closest(root, 46), level1[3]);
    EXPECT_EQ(s.search_closest(root, 57), level1[4]);
    EXPECT_EQ(s.search_closest(root, 61), level1[5]);
    EXPECT_EQ(s.search_closest(root, 85), level1[7]);
    EXPECT_EQ(s.search_closest(root, 99), level1[8]);
    EXPECT_EQ(s.search_closest(root, 101), level1[9]);
    EXPECT_EQ(s.search_closest(root, 9000), level1[9]);

    EXPECT_EQ(s.search_closest(root, 60), level1[5]);
    EXPECT_EQ(s.search_closest(root, 10), level4[0]);
    EXPECT_EQ(s.search_closest(root, 20), level1[1]);
    EXPECT_EQ(s.search_closest(root, 30), level2[1]);
    EXPECT_EQ(s.search_closest(root, 70), level1[6]);
    EXPECT_EQ(s.search_closest(root, 50), level3[1]);

    EXPECT_EQ(s.search_closest(root, 45), level1[3]);
    EXPECT_EQ(s.search_closest(root, 11), level1[0]);
    EXPECT_EQ(s.search_closest(root, 65), level1[5]);
    EXPECT_EQ(s.search_closest(root, 32), level1[2]);
    EXPECT_EQ(s.search_closest(root, 22), level1[1]);
    EXPECT_EQ(s.search_closest(root, 51), level1[4]);
    EXPECT_EQ(s.search_closest(root, 73), level1[6]);

    EXPECT_EQ(s.search_closest(root, 8), level1[0]);
    EXPECT_EQ(s.search_closest(root, 7), level1[0]);
    EXPECT_EQ(s.search_closest(root, 6), level1[0]);
    EXPECT_EQ(s.search_closest(root, 1), level1[0]);
    EXPECT_EQ(s.search_closest(root, -45), level1[0]);

    EXPECT_EQ(s.search_closest(root, 81), level1[7]);
    EXPECT_EQ(s.search_closest(root, 82), level1[7]);
    EXPECT_EQ(s.search_closest(root, 83), level1[7]);
    EXPECT_EQ(s.search_closest(root, 88), level1[7]);
    EXPECT_EQ(s.search_closest(root, 99), level1[8]);
    EXPECT_EQ(s.search_closest(root, 9000), level1[9]);
}
