from collections import deque

class Solution:
    def canFinish(self, graph):
        numCourses = len(graph)
        indegrees = [0] * numCourses
        for sequels in graph:
            for sequel in sequels:
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
    
class TestCourseSchedule:
    def test_no_cycles(self):
        graph = [
            [1],      # 0 → 1
            [2],      # 1 → 2
            [],       # 2
            [1, 2]    # 3 → 1, 2
        ]
        s = Solution()
        assert s.canFinish(graph) == True

        graph = [
            [],
            [0],
            [1],
            [1],
            [],
            [4,6],
            []
        ]
        assert s.canFinish(graph) == True

    def test_with_cycle(self):
        graph = [
            [1],      # 0 → 1
            [2],      # 1 → 2
            [0]       # 2 → 0 (cycle)
        ]
        s = Solution()
        assert s.canFinish(graph) == False

        graph = [
            [],
            [0],
            [1],
            [1],
            [9],
            [4,6],
            [],
            [8],
            [9],
            [7]
        ]
        assert s.canFinish(graph) == False

    def test_disconnected_graph(self):
        graph = [
            [1],      # 0 → 1
            [],       # 1
            [3],      # 2 → 3
            []        # 3
        ]
        s = Solution()
        assert s.canFinish(graph) == True

    def test_self_loop(self):
        graph = [
            [0]       # 0 → 0 (self-loop).
        ]
        s = Solution()
        assert s.canFinish(graph) == False

    def test_empty_graph(self):
        s = Solution() # Please note numCourses can be 1 but there are no edges
        assert s.canFinish([]) == True