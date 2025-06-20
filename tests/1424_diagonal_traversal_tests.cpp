#include <gtest/gtest.h>
#include "../1424_diagonal_traverse_2/first_variant_1424_anti_diagonal.hpp"
#include "../1424_diagonal_traverse_2/second_variant_1424_print_anti_diagonal.hpp"

TEST(DiagonalTraverse2_FirstVariant_AntiDiagonal, FullMatrix) {
    std::vector<std::vector<int>> nums = {
        {1, 3, 6},
        {2, 5, 8},
        {4, 7, 9}
    };
    std::vector<std::vector<int>> expected = {{1}, {3, 2}, {6, 5, 4}, {8, 7}, {9}};
    EXPECT_EQ(expected, findAntiDiagonalOrder_1424_first_variant(nums));

    nums = {{12, 7, 21, 31, 11},
        {45, -2, 14, 27, 19},
        {-3, 15, 36, 71, 26},
        {4, -13, 55, 34, 15}};
    expected = {
        {12},
        {7, 45},
        {21, -2, -3},
        {31, 14, 15, 4},
        {11, 27, 36, -13},
        {19, 71, 55},
        {26, 34},
        {15}
    };
    EXPECT_EQ(expected, findAntiDiagonalOrder_1424_first_variant(nums));
}

TEST(DiagonalTraverse2_FirstVariant_AntiDiagonal, HalfMatrix) {
    std::vector<std::vector<int>> nums = {
        {1, 3, 6},
        {2, 5},
        {4}
    };
    std::vector<std::vector<int>> expected = {{1}, {3, 2}, {6, 5, 4}};
    EXPECT_EQ(expected, findAntiDiagonalOrder_1424_first_variant(nums));

    nums = {{12, 7, 21, 31},
            {45, -2, 14, 27, 19},
            {-3, 36},
            {4, -13, 55, 34}};
    expected = {
        {12},
        {7, 45},
        {21, -2, -3},
        {31, 14, 36, 4},
        {27, -13},
        {19, 55},
        {34}
    };
    EXPECT_EQ(expected, findAntiDiagonalOrder_1424_first_variant(nums));

    nums = {{12, 7, 21, 31},
            {45},
            {-3, 36},
            {4, -13}};
    expected = {
    {12},
    {7, 45},
    {21, -3},
    {31, 36, 4},
    {-13},
    };
    EXPECT_EQ(expected, findAntiDiagonalOrder_1424_first_variant(nums));
}

TEST(DiagonalTraverse2_FirstVariant_AntiDiagonal, SingleColumn) {
    std::vector<std::vector<int>> nums = {
        {1},
        {2},
        {4},
        {90},
        {123}
    };
    std::vector<std::vector<int>> expected = {{1}, {2}, {4}, {90}, {123}};
    EXPECT_EQ(expected, findAntiDiagonalOrder_1424_first_variant(nums));
}

TEST(DiagonalTraverse2_FirstVariant_PrintAntiDiagonal, SingleRow) {
    std::vector<std::vector<int>> nums = {
        {1, 2, 3, 4, 5, 6}
    };
    std::vector<std::vector<int>> expected = {{1}, {2}, {3}, {4}, {5}, {6}};
    EXPECT_EQ(expected, findAntiDiagonalOrder_1424_first_variant(nums));
}
////////////////////////////////////////////////////////////////////////////////////////////////////////
// VARIANT: print out the anti-diagonal order

TEST(DiagonalTraverse2_FirstVariant_PrintAntiDiagonal, HalfMatrix) {
    std::vector<std::vector<int>> nums = {
        {1, 3, 6},
        {2, 5},
        {4}
    };
    
    std::vector<int> expected = {4, 2, 5, 1, 3, 6};
    
    EXPECT_EQ(expected,  findAntiDiagonalOrder_1424_first_variant_2(nums));
}

TEST(DiagonalTraverse_FirstVariant_PrintAntiDiagonal, FullMatrix) {
    std::vector<std::vector<int>> nums = {
        {1, 3, 6},
        {2, 5, 8},
        {4, 7, 9}
    };
    std::vector<int> expected = {4, 7, 2, 9, 5, 1, 8, 3, 6};

    EXPECT_EQ(expected, findAntiDiagonalOrder_1424_first_variant_2(nums));
}

//////////////////////////////////////////////////////////////////////////////////////////
TEST(DiagonalTraverse_SecondVariant_PrintAntiDiagonal, FullMatrix) {
    std::vector<std::vector<int>> nums = {
        {1, 3, 6},
        {2, 5, 8},
        {4, 7, 9}
    };
    findAntiDiagonalOrder_1424_second_variant(nums);

    nums = {{12, 7, 21, 31, 11},
            {45, -2, 14, 27, 19},
            {-3, 15, 36, 71, 26},
            {4, -13, 55, 34, 15}};
    findAntiDiagonalOrder_1424_second_variant(nums);
}
TEST(DiagonalTraverse2_SecondVariant_PrintAntiDiagonal, SingleColumn) {
    std::vector<std::vector<int>> nums = {
        {1},
        {2},
        {4},
        {90},
        {123}
    };
    findAntiDiagonalOrder_1424_second_variant(nums);
}
TEST(DiagonalTraverse2_SecondVariant_PrintAntiDiagonal, SingleRow) {
    std::vector<std::vector<int>> nums = {
        {1, 2, 3, 4, 5, 6}
    };
    findAntiDiagonalOrder_1424_second_variant(nums);
}



