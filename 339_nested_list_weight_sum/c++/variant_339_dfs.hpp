#pragma once 

#include <vector>
#include "object.hpp"

class SolutionDFS {
private:
    int dfs(std::vector<Object>& objs, int depth) {
        int sum = 0;
        for (auto obj : objs) {
            if (std::holds_alternative<int>(obj.value))
                sum += std::get<int>(obj.value) * depth;
            else {
                auto nested_objs = std::get<std::vector<Object>>(obj.value);
                sum += dfs(nested_objs, depth + 1);
            }
        }

        return sum;
    }
public:
    int depthSum(std::vector<Object>& objs) {
        int sum = 0;
        int depth = 1;
        return dfs(objs, 1);
        return sum;
    }
};