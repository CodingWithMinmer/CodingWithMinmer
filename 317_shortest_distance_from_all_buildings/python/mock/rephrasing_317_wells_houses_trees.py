from collections import deque

class WellPlacement:
    def shortestDistance(self, grid):
        matrix = [[[0,0] for _ in range(len(grid[0]))] for _ in range(len(grid))]

        houses = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'H':
                    self.bfs([i,j], grid, matrix, houses)
                    houses += 1

        result = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j][1] == houses:
                    result = min(result, matrix[i][j][0])

        return result if result != float('inf') else -1

    def bfs(self, src, grid, matrix, houses):
        q = deque()
        q.append((src, 0))

        while q:
            (curr, distance) = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                i, j = curr[0] + dr, curr[1] + dc
                if 0 <= i < len(grid) and \
                   0 <= j < len(grid[0]) and \
                   matrix[i][j][1] == houses and \
                   grid[i][j] == ' ':
                    matrix[i][j][0] += distance + 1
                    matrix[i][j][1] = houses + 1
                    q.append(([i, j], distance + 1))