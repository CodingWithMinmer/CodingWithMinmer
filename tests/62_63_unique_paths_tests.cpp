#include <gtest/gtest.h>
#include "../62_unique_path/mock/c++/mock_62_variant.hpp"
#include "../62_unique_path/mock/c++/mock_63_variant.hpp"

TEST(UniquePaths_62_Variant, GetPaths) {
    Solution62Variant_ReturnPaths s;
    std::vector<std::string> result = s.get_unique_paths(3);
    std::vector<std::string> expected = {"RRDD", "RDRD", "RDDR", "DRRD", "DRDR", "DDRR"};
    EXPECT_EQ(expected, result);
}

TEST(UniquePaths_63_Variant, GetPaths_Obstacles) {
    Solution63Variant_Obstacles s;
    std::vector<std::vector<int>> grid = {
        {0, 0, 0, 0},
        {0, 1, 0, 0},
        {1, 0, 0, 1},
        {0, 0, 0, 0},
    };
    std::vector<std::string> result = s.get_unique_paths_with_obstacles(grid);
    std::vector<std::string> expected = {"RRDDDR"};
    EXPECT_EQ(expected, result);

    grid = {
        {0, 0, 0},
        {0, 1, 0},
        {0, 0, 0}
    };
    result = s.get_unique_paths_with_obstacles(grid);
    expected = {"RRDD", "DDRR"};
    EXPECT_EQ(expected, result);
}