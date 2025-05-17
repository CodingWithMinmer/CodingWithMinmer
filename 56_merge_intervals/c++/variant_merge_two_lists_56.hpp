#pragma once

#include <cassert>
#include <vector>

// VARIANT: What if you had to merge two interval lists instead of one?
void try_merge(std::vector<std::vector<int>>& result,
                std::vector<int>& curr_interval) {
    if (result.empty() || curr_interval[0] > result.back()[1])
        result.push_back(curr_interval);
    else
        result.back()[1] = std::max(curr_interval[1], result.back()[1]);
}
std::vector<std::vector<int>> merge_2_interval_lists_56_variant(
        std::vector<std::vector<int>>& A,
        std::vector<std::vector<int>>& B) {
    std::vector<std::vector<int>> result;
    int i = 0, j = 0;
    while (i < A.size() && j < B.size()) {
        std::vector<int> curr_interval;
        if (A[i][0] <= B[j][0])
            curr_interval = A[i++];
        else
            curr_interval = B[j++];

        try_merge(result, curr_interval);
    }

    if (i < A.size())
        while (i < A.size())
            try_merge(result, A[i++]);
    else
        while (j < B.size())
            try_merge(result, B[j++]);

    return result;
}

void merge_2_interval_lists_56_variant() {
    std::vector<std::vector<int>> A = {{3, 11}, {14, 15}, {18, 22}, {23, 24}, {25, 26}};
    std::vector<std::vector<int>> B = {{2, 8}, {13, 20}};
    std::vector<std::vector<int>> expected = {{2, 11}, {13, 22}, {23, 24}, {25, 26}};
    assert(expected == merge_2_interval_lists_56_variant(A, B));

    A = {};
    B = {{2, 8}, {13, 20}};
    expected = {{2, 8}, {13, 20}};
    assert(expected == merge_2_interval_lists_56_variant(A, B));

    A = {{1, 5}, {10, 15}, {20, 25}};
    B = {{5, 10}, {15, 20}};
    expected = {{1, 25}};
    assert(expected == merge_2_interval_lists_56_variant(A, B));

    A = {{1, 5}, {11, 15}, {21, 25}};
    B = {{6, 10}, {16, 20}};
    expected = {{1, 5}, {6, 10}, {11, 15}, {16, 20}, {21, 25}};
    assert(expected == merge_2_interval_lists_56_variant(A, B));

    A = {{1, 5}};
    B = {{1, 5}};
    expected = {{1, 5}};
    assert(expected == merge_2_interval_lists_56_variant(A, B));

    A = {{1, 5}, {10, 15}, {20, 25}};
    B = {{2, 3}, {4, 5}, {12, 13}, {20, 27}};
    expected = {{1, 5}, {10, 15}, {20, 27}};
    assert(expected == merge_2_interval_lists_56_variant(A, B));
}