#include <gtest/gtest.h>
#include "../670_maximum_swap/variant_670.hpp"

TEST(MaximumSwap_Variant_BuildSecondLargest, EmptyReturnsEmptyVector) {
    std::vector<int> num = {};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());
}

TEST(MaximumSwap_Variant_BuildSecondLargest, OneDigitReturnsEmptyVector) {
    std::vector<int> num = {1};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());

    num = {2};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());

    num = {3};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());

    num = {4};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());

    num = {5};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());

    num = {6};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());

    num = {7};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());

    num = {8};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());

    num = {9};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());

    num = {0};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());
}

TEST(MaximumSwap_Variant_BuildSecondLargest, DistinctDigitsAndOneSwap) {
    std::vector<int> num = {2, 7, 3, 6};
    std::vector<int> expected = {7, 6, 2, 3};
    EXPECT_EQ(expected, get_second_largest_number_670(num));

    num = {2, 3, 4, 1, 8};
    expected = {8, 4, 3, 1, 2};
    EXPECT_EQ(expected, get_second_largest_number_670(num)); // https://www.1point3acres.com/bbs/thread-1046619-1-1.html
}

TEST(MaximumSwap_Variant_BuildSecondLargest, AllDuplicateDigitsCannotBuildSecondLargest) {
    std::vector<int> num = {5, 5, 5, 5, 5, 5, 5, 5, 5, 5};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());

    num = {2, 2};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());

    num = {0, 0, 0, 0, 0, 0};
    EXPECT_TRUE(get_second_largest_number_670(num).empty());
}

TEST(MaximumSwap_Variant_BuildSecondLargest, DuplicateDigitsAndLoopedSwap) {
    std::vector<int> num = {1, 2, 1, 1, 1};
    std::vector<int> expected = {1, 2, 1, 1, 1};
    EXPECT_EQ(expected, get_second_largest_number_670(num));

    num = {5, 9, 7, 6, 6, 3, 9, 6, 6};
    expected = {9, 9, 7, 6, 6, 6, 6, 3, 5};
    EXPECT_EQ(expected, get_second_largest_number_670(num));
    
    // Add 2 more 3's
    num = {5, 9, 7, 6, 6, 3, 9, 6, 6, 3, 3};
    expected = {9, 9, 7, 6, 6, 6, 6, 3, 5, 3, 3};
    EXPECT_EQ(expected, get_second_largest_number_670(num));

    num = {4, 4, 4, 4, 9, 9, 9, 9, 9};
    expected = {9, 9, 9, 9, 4, 9, 4, 4, 4};
    EXPECT_EQ(expected, get_second_largest_number_670(num));

    num = {9, 9, 7, 6, 6, 6, 6, 5, 3, 3, 3};
    expected = {9, 9, 7, 6, 6, 6, 6, 3, 5, 3, 3};
    EXPECT_EQ(expected, get_second_largest_number_670(num));
}

TEST(MaximumSwap_Variant_BuildSecondLargest, Zeroes) {
    std::vector<int> num = {0, 0, 0, 0, 0, 6, 0}; // All zeroes but one
    std::vector<int> expected = {0, 6, 0, 0, 0, 0, 0};
    EXPECT_EQ(expected, get_second_largest_number_670(num));

    num = {0, 0, 1, 2, 3, 3}; // Some zero duplicates
    expected = {3, 3, 2, 0, 1, 0};
    EXPECT_EQ(expected, get_second_largest_number_670(num));

    num = {0, 0, 8, 4, 9, 9, 6, 7};
    expected = {9, 9, 8, 7, 6, 0, 4, 0};
    EXPECT_EQ(expected, get_second_largest_number_670(num));
}
