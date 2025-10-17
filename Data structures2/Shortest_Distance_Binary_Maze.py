from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        n, m = len(grid), len(grid[0])
        sr, sc = source
        dr, dc = destination
        
        # If source or destination is blocked
        if grid[sr][sc] == 0 or grid[dr][dc] == 0:
            return -1
        
        # If source == destination
        if sr == dr and sc == dc:
            return 0
        
        # Directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Distance matrix initialized to infinity
        dist = [[float('inf')] * m for _ in range(n)]
        dist[sr][sc] = 0
        
        # BFS queue: stores (row, col, distance)
        q = deque([(sr, sc, 0)])
        
        while q:
            r, c, d = q.popleft()
            
            for drn in directions:
                nr, nc = r + drn[0], c + drn[1]
                
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and dist[nr][nc] > d + 1:
                    dist[nr][nc] = d + 1
                    if nr == dr and nc == dc:
                        return dist[nr][nc]  # Found destination early
                    q.append((nr, nc, d + 1))
        
        # If destination not reachable
        return -1
grid = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 0, 1]
]
source = [0, 1]
destination = [2, 2]

print(Solution().shortestPath(grid, source, destination))
# Output ➤ 3
