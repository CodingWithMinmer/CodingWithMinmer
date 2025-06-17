#include <vector>

int countMonotonicSequences(std::vector<int>& nums) {
    int dir = -1;
    int count = 0;
    bool is_flat = false;
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] < nums[i - 1]) {
            if (dir == 1 || dir == -1)
                count++;

            if (is_flat && dir == 0) {
                is_flat = false;
                count += 2;
            }
            if (is_flat) {
                is_flat = false;
                count++;
            }

            dir = 0;
        }
        else if (nums[i] > nums[i - 1]) {
            if (dir == 0 || dir == -1)
                count++;
                
            if (is_flat && dir == 1) {
                is_flat = false;
                count += 2;
            }
            if (is_flat) {
                is_flat = false;
                count++;
            }

            dir = 1;
        }
        else
            is_flat = true;
    }

    if (is_flat)
        count++;

    return count;
}