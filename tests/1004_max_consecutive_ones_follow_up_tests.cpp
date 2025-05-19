#include <gtest/gtest.h>
#include "../1004_max_consecutive_ones_3/third_variant_1004_2d_matrix.hpp"
#include "../1004_max_consecutive_ones_3/fourth_variant_1004_decimal_pto.hpp"

TEST(MaxConsecutiveOnes3_2DMatrix_Variant, All_Workdays) {
    std::vector<std::vector<char>> days = {{'W', 'W', 'W'},
                                          {'W', 'W', 'W'},
                                          {'W', 'W', 'W'}};
    Variant_1004_2DMatrix s;
    EXPECT_EQ(0, s.getMaxVacations(days, 0));
    EXPECT_EQ(1, s.getMaxVacations(days, 1));
    EXPECT_EQ(2, s.getMaxVacations(days, 2));
    EXPECT_EQ(3, s.getMaxVacations(days, 3));
    EXPECT_EQ(4, s.getMaxVacations(days, 4));
    EXPECT_EQ(5, s.getMaxVacations(days, 5));
    EXPECT_EQ(6, s.getMaxVacations(days, 6));
    EXPECT_EQ(7, s.getMaxVacations(days, 7));
    EXPECT_EQ(8, s.getMaxVacations(days, 8));
    EXPECT_EQ(9, s.getMaxVacations(days, 9));
    EXPECT_EQ(9, s.getMaxVacations(days, 10));
    EXPECT_EQ(9, s.getMaxVacations(days, 9000));
}

TEST(MaxConsecutiveOnes3_2DMatrix_Variant, All_Holidays) {
    std::vector<std::vector<char>> days = {{'H', 'H', 'H'},
                                          {'H', 'H', 'H'},
                                          {'H', 'H', 'H'}};
    Variant_1004_2DMatrix s;
    EXPECT_EQ(9, s.getMaxVacations(days, 0));
    EXPECT_EQ(9, s.getMaxVacations(days, 1));
    EXPECT_EQ(9, s.getMaxVacations(days, 2));
    EXPECT_EQ(9, s.getMaxVacations(days, 3));
    EXPECT_EQ(9, s.getMaxVacations(days, 4));
    EXPECT_EQ(9, s.getMaxVacations(days, 5));
    EXPECT_EQ(9, s.getMaxVacations(days, 6));
    EXPECT_EQ(9, s.getMaxVacations(days, 7));
    EXPECT_EQ(9, s.getMaxVacations(days, 8));
    EXPECT_EQ(9, s.getMaxVacations(days, 9));
    EXPECT_EQ(9, s.getMaxVacations(days, 10));
    EXPECT_EQ(9, s.getMaxVacations(days, 9000));
}

TEST(MaxConsecutiveOnes3_2DMatrix_Variant, Mixed_Workdays_Holidays) {
    std::vector<std::vector<char>> days = {{'W', 'H', 'H'},
                                          {'W', 'W', 'H'},
                                          {'W', 'W', 'W'}};
    Variant_1004_2DMatrix s;
    EXPECT_EQ(3, s.getMaxVacations(days, 1));
    EXPECT_EQ(5, s.getMaxVacations(days, 2));
    EXPECT_EQ(6, s.getMaxVacations(days, 3));
    EXPECT_EQ(7, s.getMaxVacations(days, 4));
    EXPECT_EQ(8, s.getMaxVacations(days, 5));
    EXPECT_EQ(9, s.getMaxVacations(days, 6));
    EXPECT_EQ(9, s.getMaxVacations(days, 7));
    EXPECT_EQ(9, s.getMaxVacations(days, 8));
    EXPECT_EQ(9, s.getMaxVacations(days, 9));
    EXPECT_EQ(9, s.getMaxVacations(days, 9000));

    days = {{'W', 'H', 'W'},
            {'H', 'W', 'H'},
            {'W', 'H', 'W'}};
    EXPECT_EQ(3, s.getMaxVacations(days, 1));
    EXPECT_EQ(5, s.getMaxVacations(days, 2));
    EXPECT_EQ(7, s.getMaxVacations(days, 3));
    EXPECT_EQ(8, s.getMaxVacations(days, 4));
    EXPECT_EQ(9, s.getMaxVacations(days, 5));
    EXPECT_EQ(9, s.getMaxVacations(days, 6));
    EXPECT_EQ(9, s.getMaxVacations(days, 7));
    EXPECT_EQ(9, s.getMaxVacations(days, 8));
    EXPECT_EQ(9, s.getMaxVacations(days, 9));
}

TEST(MaxConsecutiveOnes3_2DMatrix_Variant, Different_Dimensions) {
    std::vector<std::vector<char>> days = {{'W', 'H', 'H', 'W', 'W'},
                                          {'H', 'W', 'W', 'W', 'W'}};
    Variant_1004_2DMatrix s;
    EXPECT_EQ(3, s.getMaxVacations(days, 1));
    EXPECT_EQ(5, s.getMaxVacations(days, 2));
    EXPECT_EQ(6, s.getMaxVacations(days, 3));
    EXPECT_EQ(7, s.getMaxVacations(days, 4));
    EXPECT_EQ(8, s.getMaxVacations(days, 5));
    EXPECT_EQ(9, s.getMaxVacations(days, 6));
    EXPECT_EQ(10, s.getMaxVacations(days, 7));
    EXPECT_EQ(10, s.getMaxVacations(days, 8));
    EXPECT_EQ(10, s.getMaxVacations(days, 9));
    EXPECT_EQ(10, s.getMaxVacations(days, 9000));

    days = {{'W'},
            {'H'},
            {'H'},
            {'W'},
            {'W'},
            {'H'},
            {'W'},
            {'W'},
            {'W'},
            {'W'}};
    EXPECT_EQ(3, s.getMaxVacations(days, 1));
    EXPECT_EQ(5, s.getMaxVacations(days, 2));
    EXPECT_EQ(6, s.getMaxVacations(days, 3));
    EXPECT_EQ(7, s.getMaxVacations(days, 4));
    EXPECT_EQ(8, s.getMaxVacations(days, 5));
    EXPECT_EQ(9, s.getMaxVacations(days, 6));
    EXPECT_EQ(10, s.getMaxVacations(days, 7));
    EXPECT_EQ(10, s.getMaxVacations(days, 8));
    EXPECT_EQ(10, s.getMaxVacations(days, 9));
    EXPECT_EQ(10, s.getMaxVacations(days, 9000));
}

/////////////////////////////////////////////////
// PTO as Decimal
/////////////////////////////////////////////////
TEST(MaxConsecutiveOnes3_DecimalPTO_Variant, OG_Problem) {
    std::vector<char> days = {'H', 'H', 'W', 'W'};
    Variant_1004_DecimalPTO s;
    EXPECT_EQ(2, s.getMaxVacations(days, 0.0));

    days = {'W', 'H', 'H', 'W', 'W', 'H', 'W'};
    EXPECT_EQ(5, s.getMaxVacations(days, 2.0));

    days = {'W', 'W', 'H', 'H', 'W', 'W', 'W'};
    EXPECT_EQ(2, s.getMaxVacations(days, 0.0));

    days = {'W', 'H', 'H', 'W', 'W', 'H', 'W'};
    EXPECT_EQ(7, s.getMaxVacations(days, 5.0));

    days = {'W', 'H', 'H', 'W', 'W', 'H', 'W'};
    EXPECT_EQ(7, s.getMaxVacations(days, 10.0));

    days = {'H', 'H', 'H', 'H', 'H', 'H', 'H'};
    EXPECT_EQ(7, s.getMaxVacations(days, 0.0));

    days = {'W', 'H', 'W', 'W', 'W', 'H', 'W', 'H'};
    EXPECT_EQ(3, s.getMaxVacations(days, 1.0));

    days = {'H', 'H', 'H', 'H', 'H', 'H'};
    EXPECT_EQ(6, s.getMaxVacations(days, 2.0));

    days = {'W', 'H', 'H', 'W', 'W', 'H', 'H', 'H', 'H', 'H'};
    EXPECT_EQ(9.0, s.getMaxVacations(days, 2.0));
}

TEST(MaxConsecutiveOnes3_DecimalPTO_Variant, Half_PTO_Days) {
    std::vector<char> days = {'W', 'H'};
    Variant_1004_DecimalPTO s;
    EXPECT_EQ(1.5, s.getMaxVacations(days, 0.5));

    days = {'H', 'W'};
    EXPECT_EQ(1.5, s.getMaxVacations(days, 0.5));

    days = {'H', 'H', 'W', 'W', 'W'};
    EXPECT_EQ(4.5, s.getMaxVacations(days, 2.5));

    days = {'H', 'H', 'W', 'W'};
    EXPECT_EQ(4, s.getMaxVacations(days, 2.5));

    days = {'H', 'W', 'H', 'W', 'H', 'W', 'H', 'W', 'H'};
    EXPECT_EQ(7.0, s.getMaxVacations(days, 3.0));

    days = {'H', 'H', 'H', 'W', 'W', 'W', 'H', 'H', 'H', 'H', 'W'};
    EXPECT_EQ(6.5, s.getMaxVacations(days, 2.5));

    days = {'W', 'W', 'W', 'W'};
    EXPECT_EQ(1.5, s.getMaxVacations(days, 1.5));

    days = {'H', 'W', 'H', 'H', 'W', 'H', 'H', 'W', 'H', 'H', 'H'};
    EXPECT_EQ(9.5, s.getMaxVacations(days, 2.5));
}

TEST(MaxConsecutiveOnes3_DecimalPTO_Variant, Other_Partial_PTOs) {
    std::vector<char> days = {'W', 'W', 'W', 'W', 'W', 'W', 'W'};
    Variant_1004_DecimalPTO s;
    EXPECT_EQ(3.2, s.getMaxVacations(days, 3.2));

    days = {'W', 'H', 'W', 'H', 'W', 'H', 'H', 'H'};
    EXPECT_EQ(5.1, s.getMaxVacations(days, 1.1));

    days = {'W', 'H', 'W'};
    EXPECT_EQ(3, s.getMaxVacations(days, 2.85));
    EXPECT_EQ(2.5, s.getMaxVacations(days, 1.5));
}

TEST(MaxConsecutiveOnes3_DecimalPTO_Variant, NoPTO_TakeNoDaysOff) {
    std::vector<char> days = {'W', 'W', 'W', 'W'};
    Variant_1004_DecimalPTO s;
    EXPECT_EQ(0.0, s.getMaxVacations(days, 0.0));

    days = {'H', 'H', 'H', 'H'};
    EXPECT_EQ(4.0, s.getMaxVacations(days, 0.0));
}

TEST(MaxConsecutiveOnes3_DecimalPTO_Variant, TooManyPTO_AllDaysOff) {
    std::vector<char> days = {'H', 'H', 'W', 'W'};
    Variant_1004_DecimalPTO s;
    EXPECT_EQ(4.0, s.getMaxVacations(days, 50.0));

    days = {'W', 'W', 'W', 'W', 'W', 'W', 'W'};
    EXPECT_EQ(7.0, s.getMaxVacations(days, 50.0));

    days = {'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'};
    EXPECT_EQ(8.0, s.getMaxVacations(days, 50.0));

    days = {'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'};
    EXPECT_EQ(8.0, s.getMaxVacations(days, 0.0));

    days = {};
    EXPECT_EQ(0.0, s.getMaxVacations(days, 0.0));

    days = {};
    EXPECT_EQ(0.0, s.getMaxVacations(days, 50.0));
}