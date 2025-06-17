#include <gtest/gtest.h>
#include "../339_nested_list_weight_sum/c++/variant_339_dfs.hpp"
#include "../339_nested_list_weight_sum/c++/variant_339_bfs.hpp"

TEST(NestedWeightListSum_DFS, SingleElement) {
    Object obj1;
    obj1.value = {100};
    SolutionDFS s;
    std::vector<Object> objs = {obj1};
    EXPECT_EQ(100, s.depthSum(objs));
}

TEST(NestedWeightListSum_DFS, FlatList) {
    Object root;
    root.value = std::vector<Object>{ Object{.value = 1}, Object{.value = 2}, Object{.value = 3}, Object{.value = 4}, Object{.value = 5} };

    SolutionDFS s;
    EXPECT_EQ(15, s.depthSum(get<std::vector<Object>>(root.value)));
}

TEST(NestedWeightListSum_DFS, Nested) {
    Object obj4; obj4.value = std::vector<Object>{ Object{.value = 4} };
    Object obj3; obj3.value = std::vector<Object>{ Object{.value = 3}, obj4 };
    Object obj2; obj2.value = std::vector<Object>{ Object{.value = 2}, obj3 };
    Object obj1; obj1.value = std::vector<Object>{ Object{.value = 1}, obj2 };

    SolutionDFS s;
    EXPECT_EQ(30, s.depthSum(get<std::vector<Object>>(obj1.value)));
}

TEST(NestedWeightListSum_DFS, Complex) {
    Object obj3; obj3.value = std::vector<Object>{ Object{.value = 9} };
    Object obj2; obj2.value = std::vector<Object>{ Object{.value = 5}, obj3, Object{.value = 3} };
    Object root; root.value = std::vector<Object>{ Object{.value = 8}, Object{.value = 4}, obj2, Object{.value = 6} };

    SolutionDFS s;
    EXPECT_EQ(61, s.depthSum(get<std::vector<Object>>(root.value)));

    Object obj3b; obj3b.value = std::vector<Object>{ Object{.value = 9} };
    Object obj2b; obj2b.value = std::vector<Object>{ obj3b };
    Object root2; root2.value = std::vector<Object>{ Object{.value = 4}, Object{.value = 2}, obj2b, Object{.value = -3} };
    EXPECT_EQ(30, s.depthSum(get<std::vector<Object>>(root2.value)));
}

TEST(NestedWeightListSum_DFS, Negatives) {
    Object obj3; obj3.value = std::vector<Object>{ Object{.value = -9} };
    Object obj2; obj2.value = std::vector<Object>{ Object{.value = 5}, obj3, Object{.value = 3} };
    Object root; root.value = std::vector<Object>{ Object{.value = 8}, Object{.value = 4}, obj2, Object{.value = -6} };

    SolutionDFS s;
    EXPECT_EQ(-5, s.depthSum(get<std::vector<Object>>(root.value)));
}

TEST(NestedWeightListSum_DFS, AllZeroes) {
    Object obj3; obj3.value = std::vector<Object>{ Object{.value = 0} };
    Object obj2; obj2.value = std::vector<Object>{ Object{.value = 0}, obj3, Object{.value = 0} };
    Object root; root.value = std::vector<Object>{ Object{.value = 0}, Object{.value = 0}, obj2, Object{.value = 0} };

    SolutionDFS s;
    EXPECT_EQ(0, s.depthSum(get<std::vector<Object>>(root.value)));
}
///////////////////////////////////////////////////
TEST(NestedWeightListSum_BFS, SingleElement) {
    Object obj1;
    obj1.value = {100};
    SolutionBFS s;
    std::vector<Object> objs = {obj1};
    EXPECT_EQ(100, s.depthSum(objs));
}

TEST(NestedWeightListSum_BFS, FlatList) {
    Object root;
    root.value = std::vector<Object>{ Object{.value = 1}, Object{.value = 2}, Object{.value = 3}, Object{.value = 4}, Object{.value = 5} };

    SolutionBFS s;
    EXPECT_EQ(15, s.depthSum(get<std::vector<Object>>(root.value)));
}

TEST(NestedWeightListSum_BFS, Nested) {
    Object obj4; obj4.value = std::vector<Object>{ Object{.value = 4} };
    Object obj3; obj3.value = std::vector<Object>{ Object{.value = 3}, obj4 };
    Object obj2; obj2.value = std::vector<Object>{ Object{.value = 2}, obj3 };
    Object obj1; obj1.value = std::vector<Object>{ Object{.value = 1}, obj2 };

    SolutionBFS s;
    EXPECT_EQ(30, s.depthSum(get<std::vector<Object>>(obj1.value)));
}

TEST(NestedWeightListSum_BFS, Complex) {
    Object obj3; obj3.value = std::vector<Object>{ Object{.value = 9} };
    Object obj2; obj2.value = std::vector<Object>{ Object{.value = 5}, obj3, Object{.value = 3} };
    Object root; root.value = std::vector<Object>{ Object{.value = 8}, Object{.value = 4}, obj2, Object{.value = 6} };

    SolutionBFS s;
    EXPECT_EQ(61, s.depthSum(get<std::vector<Object>>(root.value)));

    Object obj3b; obj3b.value = std::vector<Object>{ Object{.value = 9} };
    Object obj2b; obj2b.value = std::vector<Object>{ obj3b };
    Object root2; root2.value = std::vector<Object>{ Object{.value = 4}, Object{.value = 2}, obj2b, Object{.value = -3} };
    EXPECT_EQ(30, s.depthSum(get<std::vector<Object>>(root2.value)));
}

TEST(NestedWeightListSum_BFS, Negatives) {
    Object obj3; obj3.value = std::vector<Object>{ Object{.value = -9} };
    Object obj2; obj2.value = std::vector<Object>{ Object{.value = 5}, obj3, Object{.value = 3} };
    Object root; root.value = std::vector<Object>{ Object{.value = 8}, Object{.value = 4}, obj2, Object{.value = -6} };

    SolutionBFS s;
    EXPECT_EQ(-5, s.depthSum(get<std::vector<Object>>(root.value)));
}

TEST(NestedWeightListSum_BFS, AllZeroes) {
    Object obj3; obj3.value = std::vector<Object>{ Object{.value = 0} };
    Object obj2; obj2.value = std::vector<Object>{ Object{.value = 0}, obj3, Object{.value = 0} };
    Object root; root.value = std::vector<Object>{ Object{.value = 0}, Object{.value = 0}, obj2, Object{.value = 0} };

    SolutionBFS s;
    EXPECT_EQ(0, s.depthSum(get<std::vector<Object>>(root.value)));
}