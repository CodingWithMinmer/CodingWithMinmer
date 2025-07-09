from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for sequel, prequel in prerequisites:
            graph[prequel].append(sequel)
            indegrees[sequel] += 1

        queue = deque()
        for sequel in range(numCourses):
            if indegrees[sequel] == 0:
                queue.append(sequel)

        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1

            for sequel in graph[node]:
                indegrees[sequel] -= 1
                if indegrees[sequel] == 0:
                    queue.append(sequel)

        return visited == numCourses