import sys
from typing import List
sys.setrecursionlimit(10**8)

class Solution:
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]
        distinct_islands = set()
        
        def dfs(r, c, base_r, base_c, shape):
            visited[r][c] = True
            shape.append((r - base_r, c - base_c))  # relative position
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == 1:
                    dfs(nr, nc, base_r, base_c, shape)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    shape = []
                    dfs(i, j, i, j, shape)
                    distinct_islands.add(tuple(shape))
        
        return len(distinct_islands)

# Test Cases
sol = Solution()
grid1 = [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 1, 1]]
print(sol.countDistinctIslands(grid1))  # Output: 1

grid2 = [[1, 1, 0, 1, 1],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 1, 1]]
print(sol.countDistinctIslands(grid2))  # Output: 3

grid3 = [[1,0],[0,1]]
print(sol.countDistinctIslands(grid3))  # Output: 2

grid4 = [[1,1,1],[1,0,1],[1,1,1]]
print(sol.countDistinctIslands(grid4))  # Output: 1
