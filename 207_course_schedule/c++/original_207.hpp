#pragma once

#include <vector>
#include <queue>

class Solution {
public:
    bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
        std::vector<int> indegrees(numCourses);
        std::vector<std::vector<int>> graph(numCourses);
        for (auto prerequisite : prerequisites) {
            auto sequel = prerequisite[0];
            auto prequel = prerequisite[1];

            graph[prequel].push_back(sequel);
            indegrees[sequel]++;
        }

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