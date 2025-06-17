#include <gtest/gtest.h>
#include "../../Unknowns/3_digitsums/c++/3_digitsums.hpp"
#include "../../Unknowns/3_digitsums/c++/3_digitsums_followup.hpp"

TEST(Unknown_Digitsums, SingleDigits_NoMath) {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    Kth_Smallest_DigitSums s;
    std::vector<int> expected = {1};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 1));

    expected = {2, 1};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 2));

    expected = {3, 2, 1};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 3));

    expected = {4, 3, 2, 1};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 4));

    expected = {5, 4, 3, 2, 1};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 5));
}

TEST(Unknown_Digitsums, MultiDigitNumbers_PreservesOGNumber) {
    std::vector<int> nums = {9, 52, 11111111, 99, 123};
    Kth_Smallest_DigitSums s;
    std::vector<int> expected = {123};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 1));

    expected = {52, 123};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 2));

    expected = {11111111, 52, 123};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 3));

    expected = {9, 11111111, 52, 123};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 4));

    expected = {99, 9, 11111111, 52, 123};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 5));

    nums = {6, 36, 22222, 101, 80};
    expected = {80, 6, 101};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 3));
}

TEST(Unknown_Digitsums, Tiebreaker) {
    std::vector<int> nums = {9, 222, 402, 99, 123};
    Kth_Smallest_DigitSums_Followup s;
    std::vector<int> expected = {222};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 1));

    expected = {222, 402};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 2));

    expected = {222, 402, 123};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 3));

    expected = {222, 402, 123, 9};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 4));

    expected = {222, 402, 123, 9, 99};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 5));

    nums = {111, 84, 21, 12, 3, 56, 2001, 10000};
    expected = {10000, 111, 21};
    EXPECT_EQ(expected, s.kthSmallestDigitSums(nums, 3));
}