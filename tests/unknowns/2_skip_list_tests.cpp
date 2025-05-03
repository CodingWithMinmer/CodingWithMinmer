#include <gtest/gtest.h>
#include "../../Unknowns/2_skip_list/c++/2_skip_list.hpp"

class SkipListBuilder {
    std::vector<SkipList::Node*> create_level(std::vector<int> vals) {
        std::vector<SkipList::Node*> l;
        for (int val : vals)
            l.push_back(new SkipList::Node(val));
        return l;
    }

    void wire_pointers_horizontally(std::vector<SkipList::Node*>& level) {
        for (int i = 1; i < level.size(); ++i) {
            level[i - 1]->next = level[i];
            level[i]->prev = level[i - 1];
        }
    }

    void wire_pointers_vertically(std::vector<SkipList::Node*>& top_nodes, std::vector<SkipList::Node*>& bottom_nodes) {
        std::unordered_map<int, SkipList::Node*> val_to_node;
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
    std::vector<std::vector<SkipList::Node*>> create() {
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

TEST(Unknown_SkipList, Basic) {
    SkipListBuilder builder;
    auto root = builder.create()[0][0];
    SkipList s;
    EXPECT_TRUE(s.search(root, 70));
    EXPECT_TRUE(s.search(root, 80));
    EXPECT_TRUE(s.search(root, 60));
    EXPECT_TRUE(s.search(root, 10));
    EXPECT_TRUE(s.search(root, 20));
    EXPECT_TRUE(s.search(root, 30));
    EXPECT_TRUE(s.search(root, 50));

    // In between SkipList::Nodes, not found
    EXPECT_FALSE(s.search(root, 45));
    EXPECT_FALSE(s.search(root, 11));
    EXPECT_FALSE(s.search(root, 65));
    EXPECT_FALSE(s.search(root, 32));
    EXPECT_FALSE(s.search(root, 22));
    EXPECT_FALSE(s.search(root, 51));
    EXPECT_FALSE(s.search(root, 73));

    // Lower values than root
    EXPECT_FALSE(s.search(root, 8));
    EXPECT_FALSE(s.search(root, 7));
    EXPECT_FALSE(s.search(root, 6));
    EXPECT_FALSE(s.search(root, 1));
    EXPECT_FALSE(s.search(root, -45));

    // Higher values than highest SkipList::Node
    EXPECT_FALSE(s.search(root, 81));
    EXPECT_FALSE(s.search(root, 82));
    EXPECT_FALSE(s.search(root, 83));
    EXPECT_FALSE(s.search(root, 88));
    EXPECT_FALSE(s.search(root, 99));
    EXPECT_FALSE(s.search(root, 9000));
}