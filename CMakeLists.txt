cmake_minimum_required(VERSION 3.28)
project(CodingWithMinmer)

set(CMAKE_CXX_STANDARD 20)

add_executable(CodingWithMinmer main.cpp
        1249_minimum_remove_to_make_valid_parentheses/mock_interview_1249.hpp
        1249_minimum_remove_to_make_valid_parentheses/original_1249.hpp
        1249_minimum_remove_to_make_valid_parentheses/first_variant_in_place_1249.hpp
        71_simplify_path/first_variant_cwd_cd_71.hpp
        71_simplify_path/original_71.hpp
        938_range_of_sum_bst/second_variant_many_invocations_938.hpp
        utils/Node.hpp
        938_range_of_sum_bst/first_variant_average_938.hpp
        938_range_of_sum_bst/original_938.hpp
        283_move_zeroes/variant_zeroes_to_front_283.hpp
        283_move_zeroes/variant_zeroes_to_front_283.hpp
        283_move_zeroes/original_283.hpp
        199_binary_tree_right_side_view/original_199.hpp
        1650_lowest_common_ancestor_3/original_1650.hpp
        528_random_pick_weight/original_528.hpp
        88_merged_sorted_array/original_88.hpp
        680_valid_palindrome_2/original_680.hpp
        215_kth_largest_element/original_215.hpp
        215_kth_largest_element/second_variant_kth_smallest_215.hpp
        1762_buildings_with_an_ocean_view/original_1762.hpp
        1762_buildings_with_an_ocean_view/first_variant_view_count_1762.hpp
        1762_buildings_with_an_ocean_view/second_variant_ocean_view_both_sides_1762.hpp
        125_valid_palindrome/original_125.hpp
        125_valid_palindrome/variant_125.hpp
        56_merge_intervals/original_56.hpp
        56_merge_intervals/variant_merge_two_lists_56.hpp
        162_find_peak_element/variant_find_valley_element_162.hpp
        162_find_peak_element/original_162.hpp
        1047_remove_all_adjacent_duplicates_in_string/variant_remove_all_1047.hpp
        121_best_time_to_buy_and_sell_stock/variant_121.hpp
        121_best_time_to_buy_and_sell_stock/original_121.hpp
)

add_subdirectory(tests)
