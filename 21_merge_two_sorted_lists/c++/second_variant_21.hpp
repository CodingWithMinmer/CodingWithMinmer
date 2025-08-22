#pragma once

#include <vector>
#include <cassert>

// VARIANT: What if you had to merge 3 sorted integer lists into a resulting list without duplicates?
std::vector<int> merge_3_sorted_lists_second_variant_21(std::vector<int>& listA,
                                std::vector<int>& listB,
                                std::vector<int>& listC) {
    std::vector<int> result;
    int a = 0, b = 0, c = 0;
    while (a < listA.size() || b < listB.size() || c < listC.size()) {
        int a_val = a < listA.size() ? listA[a] : INT_MAX;
        int b_val = b < listB.size() ? listB[b] : INT_MAX;
        int c_val = c < listC.size() ? listC[c] : INT_MAX;

        int min_val = std::min({a_val, b_val, c_val});
        if (result.empty() || result.back() != min_val) {
            result.push_back(min_val);
        }

        if (a_val == min_val)
            a++;
        else if (b_val == min_val)
            b++;
        else if (c_val == min_val)
            c++;
    }

    return result;
}

void merge_3_sorted_lists_second_variant_21() {
    std::vector<int> a = {1, 1, 1, 3, 4, 5};
    std::vector<int> b = {3, 3, 4, 5, 6};
    std::vector<int> c = {1, 1, 3, 3, 8, 8, 8, 10};
    std::vector<int> expected = {1, 3, 4, 5, 6, 8, 10};
    assert(expected == merge_3_sorted_lists_second_variant_21(a, b, c));

    a = {};
    b = {3, 3, 4, 5, 6};
    c = {1, 1, 3, 3, 8, 8, 8, 10};
    expected = {1, 3, 4, 5, 6, 8, 10};
    assert(expected == merge_3_sorted_lists_second_variant_21(a, b, c));

    a = {};
    b = {};
    c = {};
    expected = {};
    assert(expected == merge_3_sorted_lists_second_variant_21(a, b, c));

    a = {1};
    b = {2};
    c = {3, 4, 5, 6, 7};
    expected = {1, 2, 3, 4, 5, 6, 7};
    assert(expected == merge_3_sorted_lists_second_variant_21(a, b, c));

    a = {1, 2, 3};
    b = {1, 2, 3};
    c = {1, 2, 3};
    expected = {1, 2, 3};
    assert(expected == merge_3_sorted_lists_second_variant_21(a, b, c));

    a = {2, 2};
    b = {2};
    c = {0};
    expected = {0, 2};
    assert(expected == merge_3_sorted_lists_second_variant_21(a, b, c));
}