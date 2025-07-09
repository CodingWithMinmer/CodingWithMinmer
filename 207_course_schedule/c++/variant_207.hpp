#pragma once

#include <vector>
#include <queue>

class Solution {
public:
    bool canFinish(std::vector<std::vector<int>>& graph) {
        int numCourses = graph.size();
        std::vector<int> indegrees(numCourses);
        for (auto& sequels : graph)
            for (auto sequel : sequels)
                indegrees[sequel]++;

        std::queue<int> q;
        for (int sequel = 0; sequel < numCourses; sequel++)
            if (indegrees[sequel] == 0)
                q.push(sequel);

        int visited = 0;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            visited++;

            for (auto& sequel : graph[node]) {
                indegrees[sequel]--;
                if (indegrees[sequel] == 0)
                    q.push(sequel);
            }
        }

        return visited == numCourses;
    }
};