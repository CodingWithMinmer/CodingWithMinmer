#pragma once

#include <cassert>
#include <vector>

// VARIANT: What if the sizes - m and n - weren't given? Instead, we're guaranteed
// that one list is double in size of the other. Merge them like you would in the original problem.
void merge_vectors_88(std::vector<int>& list_a, std::vector<int>& list_b) {
    int a = list_a.size() / 2 - 1;
    int b = list_b.size() - 1;
    int i = list_a.size() - 1;
    while (b >= 0) {
        if (a >= 0 && list_a[a] >= list_b[b]) {
            list_a[i] = list_a[a];
            a--;
        }
        else {
            list_a[i] = list_b[b];
            b--;
        }
        i--;
    }
}

void merge_vectors_88() {
    std::vector<int> list_a = {1, 3, 0, 0};
    std::vector<int> list_b = {4, 10};
    std::vector<int> expected = {1, 3, 4, 10};
    merge_vectors_88(list_a, list_b);
    assert(expected == list_a);

    list_a = {5, 6, 7, 8, 0, 0, 0, 0};
    list_b = {1, 2, 3, 4};
    expected = {1, 2, 3, 4, 5, 6, 7, 8};
    merge_vectors_88(list_a, list_b);
    assert(expected == list_a);

    list_a = {0};
    list_b = {99}; // Not quite 2N size but algo works!
    expected = {99};
    merge_vectors_88(list_a, list_b);
    assert(expected == list_a);

    list_a = {1, 10, 0, 0};
    list_b = {2, 11};
    expected = {1, 2, 10, 11};
    merge_vectors_88(list_a, list_b);
    assert(expected == list_a);
}