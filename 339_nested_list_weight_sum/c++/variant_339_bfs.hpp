#pragma once 

#include <vector>
#include <queue>
#include "object.hpp"

class SolutionBFS {
public:
    int depthSum(std::vector<Object>& objs) {
        std::queue<Object> queue;
        for (auto obj : objs)
            queue.emplace(obj);
        
        int level = 1;
        int sum = 0;
        while (!queue.empty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                auto obj = queue.front();
                queue.pop();

                if (std::holds_alternative<int>(obj.value))
                    sum += std::get<int>(obj.value) * level;
                else {
                    auto nested_objs = std::get<std::vector<Object>>(obj.value);
                    for (auto nested_obj : nested_objs)
                        queue.emplace(nested_obj);
                }
            }
            level++;
        }

        return sum;
    }
};