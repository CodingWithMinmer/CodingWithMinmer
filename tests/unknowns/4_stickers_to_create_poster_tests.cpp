#include <gtest/gtest.h>
#include "../../Unknowns/4_stickers/c++/stickers_to_create_poster.hpp"

TEST(Unknown_StickersToCreatePoster, NeedOneSticker) {
    StickersToCreatePosters s;
    std::string sticker = "a";
    std::string poster = "a";
    EXPECT_EQ(1, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "aa";
    poster = "aa";
    EXPECT_EQ(1, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "ab";
    poster = "ab";
    EXPECT_EQ(1, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "abcdefghijklmnopqrstuvwxyz";
    poster = "abcdefghijklmnopqrstuvwxyz";
    EXPECT_EQ(1, s.minimum_stickers_for_poster(sticker, poster));
}

TEST(Unknown_StickersToCreatePoster, MoreThanEnoughStickers_HasLeftovers) {
    StickersToCreatePosters s;
    std::string sticker = "aa";
    std::string poster = "a";
    EXPECT_EQ(1, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "aaa";
    poster = "a";
    EXPECT_EQ(1, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "aabb";
    poster = "ab";
    EXPECT_EQ(1, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "aaabbb";
    poster = "aabb";
    EXPECT_EQ(1, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "aabbcc";
    poster = "abbcc";
    EXPECT_EQ(1, s.minimum_stickers_for_poster(sticker, poster));
}

TEST(Unknown_StickersToCreatePoster, InsufficientStickers_ReturnsNegativeOne) {
    StickersToCreatePosters s;
    std::string sticker = "z";
    std::string poster = "a";
    EXPECT_EQ(-1, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "za";
    poster = "ab";
    EXPECT_EQ(-1, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "bca";
    poster = "abcd";
    EXPECT_EQ(-1, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "bcdda";
    poster = "abcdcxccaa";
    EXPECT_EQ(-1, s.minimum_stickers_for_poster(sticker, poster));
}

TEST(Unknown_StickersToCreatePoster, LeftoverStickers_DoesNotMatter) {
    StickersToCreatePosters s;
    std::string sticker = "zab";
    std::string poster = "zzz";
    EXPECT_EQ(3, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "ffffrrooggg";
    poster = "ffroogf";
    EXPECT_EQ(1, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "xyza";
    poster = "xxyyyyzza";
    EXPECT_EQ(4, s.minimum_stickers_for_poster(sticker, poster));
}

TEST(Unknown_StickersToCreatePoster, FractionalStickersNeeded_RoundsUp) {
    StickersToCreatePosters s;
    std::string sticker = "aabb";
    std::string poster = "aaabbb";
    EXPECT_EQ(2, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "xxyz";
    poster = "xyxx";
    EXPECT_EQ(2, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "xyyyza";
    poster = "xxyyyyzzyyyyayy";
    EXPECT_EQ(4, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "aaa";
    poster = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    EXPECT_EQ(10, s.minimum_stickers_for_poster(sticker, poster));
    sticker = "aaaxyz";
    poster = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    EXPECT_EQ(10, s.minimum_stickers_for_poster(sticker, poster));
    sticker = "aaaxyyyzzz";
    poster = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    EXPECT_EQ(10, s.minimum_stickers_for_poster(sticker, poster));

    sticker = "xxoo";
    poster = "xxxxxxooo";
    EXPECT_EQ(3, s.minimum_stickers_for_poster(sticker, poster));
}