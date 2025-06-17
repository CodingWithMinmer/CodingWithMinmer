#include <gtest/gtest.h>
#include "../896_monotonic_array/c++/variant_896_unrefactored.hpp"
#include "../896_monotonic_array/c++/variant_896_refactored.hpp"

TEST(MonotonicArray_896_Variant, UnchangingTerrain) {
    std::vector<int> nums1 = {5, 5, 5, 5, 5};
    EXPECT_EQ(1, countMonotonicSequences(nums1));
    EXPECT_EQ(1, countMonotonicSequences_improved(nums1));

    nums1 = {1000};
    EXPECT_EQ(0, countMonotonicSequences(nums1));
    EXPECT_EQ(0, countMonotonicSequences_improved(nums1));
}

TEST(MonotonicArray_896_Variant, StrictlyIncreasing) {
    std::vector<int> nums1{1, 3, 5, 10};
    EXPECT_EQ(1, countMonotonicSequences(nums1));

    nums1 = {1, 9};
    EXPECT_EQ(1, countMonotonicSequences(nums1));

    nums1 = {10, 16, 20, 25, 50, 69, 420};
    EXPECT_EQ(1, countMonotonicSequences(nums1));

    nums1 = {0, 9};
    EXPECT_EQ(1, countMonotonicSequences(nums1));
}

TEST(MonotonicArray_896_Variant, StrictlyDecreasing) {
    std::vector<int> nums1 = {10, 5, 3, 1};
    EXPECT_EQ(1, countMonotonicSequences(nums1));

    nums1 = {9, 4, 3, 2, 1};
    EXPECT_EQ(1, countMonotonicSequences(nums1));

    nums1 = {100, 1};
    EXPECT_EQ(1, countMonotonicSequences(nums1));
}

TEST(MonotonicArray_896_Variant, Unchanging_StrictlyIncreasing) {
    std::vector<int> nums1{6, 6, 6, 9, 10, 11, 12}; // Unchanging to Strictly increasing
    EXPECT_EQ(2, countMonotonicSequences(nums1));

    nums1 = {10, 11, 12, 12, 12, 12}; // Strictly increasing to Unchanging
    EXPECT_EQ(2, countMonotonicSequences(nums1));
}

TEST(MonotonicArray_896_Variant, Unchanging_StrictlyDecreasing) {
    std::vector<int> nums1{6, 6, 6, 5, 4, 3, 2, 1}; // Unchanging to Strictly decreasing
    EXPECT_EQ(2, countMonotonicSequences(nums1));

    nums1 = {5, 4, 3, 2, 2, 2, 2, 2}; // Strictly decreasing to Unchanging
    EXPECT_EQ(2, countMonotonicSequences(nums1));
}

TEST(MonotonicArray_896_Variant, OnlyStrictly_Increasing_Decreasing) {
    std::vector<int> nums1{4, 5, 6, 5, 4, 5, 6, 7, 8, 3, 1, 10};
    EXPECT_EQ(5, countMonotonicSequences(nums1));

    nums1 = {10, 9, 5, 7, 10, 2, 10, 2, 10, 15, 16};
    EXPECT_EQ(6, countMonotonicSequences(nums1));

    nums1 = {1, 2, 1, 2, 1, 2, 1, 2};
    EXPECT_EQ(7, countMonotonicSequences(nums1));
}

TEST(MonotonicArray_896_Variant, Hybrid) {
    // Unchanging to Dec to Unchanging to Increasing to Unchanging
    std::vector<int> nums1{6, 6, 6, 5, 4, 3, 2, 1, 1, 22, 22};
    EXPECT_EQ(5, countMonotonicSequences(nums1));

    nums1 = {1, 2, 3, 4, 4, 4, 3, 2, 1};
    EXPECT_EQ(3, countMonotonicSequences(nums1));

    nums1 = {1, 1, 2, 2, 1, 1, 3, 3, 5, 5, 1, 5, 1, 5, 5, 5, 1};
    EXPECT_EQ(15, countMonotonicSequences(nums1));

    nums1 = {10, 9, 8, 8, 8, 8, 6, 4, 4, 4, 4, 4, 4, 1, 2, 1, 2, 2};
    EXPECT_EQ(9, countMonotonicSequences(nums1));

    nums1 = {1, 2, 3, 2, 1, 1};
    EXPECT_EQ(3, countMonotonicSequences(nums1));
}