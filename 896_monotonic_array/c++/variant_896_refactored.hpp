#include <vector>
#include <iostream>

enum direction {
    unknown = -1,
    dec = 0,
    inc = 1,
    flat = 3
};
int countMonotonicSequences_improved(std::vector<int>& nums) {
    if (nums.size() <= 1) 
        return 0;

    int count = nums[0] != nums[1] ? 1 : 0;
    int dir = direction::unknown;
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] < nums[i - 1]) {
            if (dir == direction::inc || dir == direction::flat)
                count++;
            dir = direction::dec;
        } else if (nums[i] > nums[i - 1]) {
            if (dir == direction::dec || dir == direction::flat)
                count++;
            dir = direction::inc;
        } else {
            if (dir != direction::flat) {
                count++;
                dir = direction::flat;
            }
        }
    }

    return count;
}