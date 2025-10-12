from typing import List
from collections import deque

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()

        # Step 1: Add all boundary land cells to queue
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n-1 or j == m-1) and grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0  # Mark visited / remove land

        # Step 2: BFS to remove all land connected to boundaries
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    q.append((nr, nc))

        # Step 3: Count remaining land cells
        return sum(sum(row) for row in grid)
obj = Solution()
print(obj.numberOfEnclaves([[0,0,0,0],
                            [1,0,1,0],
                            [0,1,1,0],
                            [0,0,0,0]]))   # ➤ 3

print(obj.numberOfEnclaves([[0,0,0,1],
                            [0,1,1,0],
                            [0,1,1,0],
                            [0,0,0,1],
                            [0,1,1,0]]))   # ➤ 4

print(obj.numberOfEnclaves([[1,1,1],
                            [1,0,1],
                            [1,1,1]]))     # ➤ 0 (All touch boundary)

print(obj.numberOfEnclaves([[0,1,0,1,0],
                            [1,1,0,1,1],
                            [0,1,1,1,0],
                            [0,0,0,0,0]])) # ➤ 1
