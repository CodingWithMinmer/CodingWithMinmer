#include <gtest/gtest.h>
#include "../827_making_a_large_island/c++/variant_827_borders_land.hpp"

TEST(MakingLargeIsland_Variant, NoLand_MakesLargestOfMatrix) {
    std::vector<std::vector<int>> grid = {
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0},
    };
    Solution827Variant s;
    EXPECT_EQ(20, s.largestIsland(grid));

    grid = {{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};
    EXPECT_EQ(16, s.largestIsland(grid));

    grid = {
        {0},
        {0},
        {0},
        {0},
        {0}};
    EXPECT_EQ(5, s.largestIsland(grid));

    grid = {{0}};
    EXPECT_EQ(1, s.largestIsland(grid));
}

TEST(MakingLargeIsland_Variant, AllLand_MakesZeroAreaIsland) {
    std::vector<std::vector<int>> grid = {
        {1, 1, 1, 1, 1},
        {1, 1, 1, 1, 1},
        {1, 1, 1, 1, 1},
        {1, 1, 1, 1, 1},
    };
    Solution827Variant s;
    EXPECT_EQ(0, s.largestIsland(grid));

    grid = {{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}};
    EXPECT_EQ(0, s.largestIsland(grid));

    grid = {
        {1},
        {1},
        {1},
        {1},
        {1}};
    EXPECT_EQ(0, s.largestIsland(grid));

    grid = {{1}};
    EXPECT_EQ(0, s.largestIsland(grid));
}

TEST(MakingLargeIsland_Variant, HybridLandWater_StillCannotCreateIsland) {
    std::vector<std::vector<int>> grid = {
        {0, 1, 0, 1, 0},
        {0, 0, 0, 0, 0},
        {1, 1, 1, 1, 1},
        {0, 0, 0, 0, 0},
    };
    Solution827Variant s;
    EXPECT_EQ(0, s.largestIsland(grid));

    grid = {{0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1}};
    EXPECT_EQ(0, s.largestIsland(grid));

    grid = {
        {1},
        {0},
        {1},
        {0},
        {1}};
    EXPECT_EQ(0, s.largestIsland(grid));

    grid = {
        {0, 0, 0, 1, 1},
        {1, 1, 0, 1, 1},
        {0, 1, 0, 1, 1},
        {0, 1, 0, 0, 0},
    };
    EXPECT_EQ(0, s.largestIsland(grid));
}

TEST(MakingLargeIsland_Variant, Hyrbid_CreatesIsland) {
    std::vector<std::vector<int>> grid = {
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0},
        {0, 0, 1, 1, 1},
        {0, 0, 1, 1, 1},
    };
    Solution827Variant s;
    EXPECT_EQ(9, s.largestIsland(grid));

    grid = {
        {0, 0, 0, 1, 1},
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0},
        {0, 0, 0, 1, 1},
    };
    EXPECT_EQ(10, s.largestIsland(grid));

    grid = {
        {1, 0, 0, 0, 1},
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0},
        {1, 0, 0, 0, 1},
    };
    EXPECT_EQ(8, s.largestIsland(grid));

    grid = {{1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};
    EXPECT_EQ(10, s.largestIsland(grid));

    grid = {
        {0},
        {0},
        {0},
        {1},
        {1}};
    EXPECT_EQ(2, s.largestIsland(grid));
}