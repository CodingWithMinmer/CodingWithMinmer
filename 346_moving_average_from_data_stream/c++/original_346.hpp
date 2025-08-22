#pragma once

#include <queue>

class MovingAverage_346 {
    std::queue<int> queue;
    int window_sum = 0;
    int size;
public:
    MovingAverage_346(int size) : size(size) {}

    double next(int val) {
        window_sum += val;
        queue.emplace(val);

        if (queue.size() > size) {
            int excluded_num = queue.front();
            queue.pop();
            window_sum -= excluded_num;
        }

        return window_sum * 1.0 / queue.size();
    }
};