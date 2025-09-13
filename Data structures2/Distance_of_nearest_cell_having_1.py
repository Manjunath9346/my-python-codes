from collections import deque

class Solution:
    # Function to find distance of nearest 1 in the grid for each cell.
    def nearest(self, grid):
        n, m = len(grid), len(grid[0])
        q = deque()
        dist = [[-1] * m for _ in range(n)]

        # Step 1: Initialize queue with all cells having 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        # Step 2: BFS from all 1's
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        return dist
grid1 = [[0,1,1,0], [1,1,0,0], [0,0,1,1]]
print(Solution().nearest(grid1))
# Output: [[1,0,0,1], [0,0,1,1], [1,1,0,0]]

grid2 = [[1,0,1], [1,1,0], [1,0,0]]
print(Solution().nearest(grid2))
# Output: [[0,1,0], [0,0,1], [0,1,2]]
