#include <gtest/gtest.h>
#include "../605_can_place_flowers/c++/variant_605_number_placed.hpp"

TEST(CanPlaceFlowers_Variant_NumbersPlaced, AllZeroes) {
    Solution_605_Variant s;
    std::vector<int> flowerbed = {0};
    EXPECT_EQ(1, s.placeFlowers(flowerbed));

    flowerbed = {0, 0};
    EXPECT_EQ(1, s.placeFlowers(flowerbed));

    flowerbed = {0, 0, 0};
    EXPECT_EQ(2, s.placeFlowers(flowerbed));

    flowerbed = {0, 0, 0, 0};
    EXPECT_EQ(2, s.placeFlowers(flowerbed));

    flowerbed = {0, 0, 0, 0, 0};
    EXPECT_EQ(3, s.placeFlowers(flowerbed));

    flowerbed = {0, 0, 0, 0, 0, 0};
    EXPECT_EQ(3, s.placeFlowers(flowerbed));
}

TEST(CanPlaceFlowers_Variant_NumbersPlaced, AsManyOnesAsPossible) {
    Solution_605_Variant s;
    std::vector<int> flowerbed = {1};
    EXPECT_EQ(0, s.placeFlowers(flowerbed));

    flowerbed = {0, 1};
    EXPECT_EQ(0, s.placeFlowers(flowerbed));

    flowerbed = {1, 0};
    EXPECT_EQ(0, s.placeFlowers(flowerbed));

    flowerbed = {1, 0, 1};
    EXPECT_EQ(0, s.placeFlowers(flowerbed));

    flowerbed = {0, 1, 0};
    EXPECT_EQ(0, s.placeFlowers(flowerbed));

    flowerbed = {1, 0, 1, 0};
    EXPECT_EQ(0, s.placeFlowers(flowerbed));

    flowerbed = {0, 1, 0, 1};
    EXPECT_EQ(0, s.placeFlowers(flowerbed));

    flowerbed = {1, 0, 1, 0, 1, 0};
    EXPECT_EQ(0, s.placeFlowers(flowerbed));

    flowerbed = {0, 1, 0, 1, 0, 1};
    EXPECT_EQ(0, s.placeFlowers(flowerbed));
}

TEST(CanPlaceFlowers_Variant_NumbersPlaced, Hybrid) {
    Solution_605_Variant s;
    std::vector<int> flowerbed = {1, 0, 0, 0, 0, 0};
    EXPECT_EQ(2, s.placeFlowers(flowerbed));

    flowerbed = {1, 0, 1, 0, 0, 0};
    EXPECT_EQ(1, s.placeFlowers(flowerbed));

    flowerbed = {0, 1, 0, 0, 0, 0, 0, 0, 0};
    EXPECT_EQ(3, s.placeFlowers(flowerbed));

    flowerbed = {0, 1, 0, 0, 1, 0, 0, 0, 0};
    EXPECT_EQ(2, s.placeFlowers(flowerbed));

    flowerbed = {0, 1, 0, 0, 1, 0, 0, 0, 1};
    EXPECT_EQ(1, s.placeFlowers(flowerbed));

    flowerbed = {1, 0, 0, 0, 0, 0, 0, 0, 1};
    EXPECT_EQ(3, s.placeFlowers(flowerbed));

    flowerbed = {1, 0, 0, 0, 1, 0, 0, 0, 1};
    EXPECT_EQ(2, s.placeFlowers(flowerbed));
}