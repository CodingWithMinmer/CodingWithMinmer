#pragma once

#include <vector>

// VARIANT: What if you had to optimize your algorithm using binary search?
class SparseVectorVariant {
public:
    std::vector<std::pair<int, int>> index_to_num;
    int binary_search(std::vector<std::pair<int, int>>& index_to_num, int target_index) {
        int left = 0;
        int right = index_to_num.size() - 1;
        while (left <= right) {
            int mid = (right - left)/2 + left;
            if (index_to_num[mid].first == target_index)
                return index_to_num[mid].second;
            if (index_to_num[mid].first < target_index)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return 0;
    }
    SparseVectorVariant(std::vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++)
            if (nums[i] != 0)
                index_to_num.push_back(std::pair{i, nums[i]});
    }
    int dotProduct(SparseVectorVariant& vec) {
        int sum = 0;
        if (index_to_num.size() < vec.index_to_num.size())
            for (auto [index, value] : index_to_num)
                sum += value * binary_search(vec.index_to_num, index);
        else
            for (auto [index, value] : vec.index_to_num)
                sum += value * binary_search(index_to_num, index);

        return sum;
    }
};

void dotProductVariant() {
    std::vector<int> nums = {0, 3, 0 ,0, 0, 0, 9};
    SparseVectorVariant our_sparse(nums);
    std::vector<int> other = {1, 2, 3, 4, 0, 7, 0, 0, 0, 0, 0};
    SparseVectorVariant other_sparse(other);
    assert(6 == our_sparse.dotProduct(other_sparse));

    nums = {0, 0, 0 ,0, 0, 0, 0};
    SparseVectorVariant our_sparse1(nums);
    other = {1, 2, 3, 4, 0, 7, 0, 0, 0, 0, 0};
    SparseVectorVariant other_sparse1(other);
    assert(0 == our_sparse1.dotProduct(other_sparse1));

    nums = {5, 0, 6, 0, 7, 0, 9, 0, 1};
    SparseVectorVariant our_sparse2(nums);
    other = {0, 0, 3, 0, 8, 1, 2, 0, 10};
    SparseVectorVariant other_sparse2(other);
    assert(102 == our_sparse2.dotProduct(other_sparse2));

    nums = {5, 0, 6, 0, 7, 0, 9, 0, 1};
    SparseVectorVariant our_sparse3(nums);
    other = {0, 0, 3, 0, 8, 1, 2, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    SparseVectorVariant other_sparse3(other);
    assert(102 == our_sparse3.dotProduct(other_sparse3));

    nums = {0, 0, 3, 0, 8, 1, 2, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    SparseVectorVariant our_sparse4(nums);
    other = {5, 0, 6, 0, 7, 0, 9, 0, 1};
    SparseVectorVariant other_sparse4(other);
    assert(102 == our_sparse4.dotProduct(other_sparse4));

    nums = {11};
    SparseVectorVariant our_sparse5(nums);
    other = {10};
    SparseVectorVariant other_sparse5(other);
    assert(110 == our_sparse5.dotProduct(other_sparse5));

    nums = {0, 1, 2, 0, 3, 4, 0};
    SparseVectorVariant our_sparse6(nums);
    other = {1, 0, 5, 0, 0, 3, 23, 24, 25, 26, 27, 28};
    SparseVectorVariant other_sparse6(other);
    assert(22 == our_sparse6.dotProduct(other_sparse6));
}