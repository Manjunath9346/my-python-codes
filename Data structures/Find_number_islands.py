class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        
        # All 8 directions
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        def dfs(x, y):
            visited[x][y] = True
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (0 <= new_x < n) and (0 <= new_y < m):
                    if not visited[new_x][new_y] and grid[new_x][new_y] == 'L':
                        dfs(new_x, new_y)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and not visited[i][j]:
                    dfs(i, j)
                    count += 1

        return count
# Test Case 1
grid1 = [
    ['L', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'L'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'W', 'W', 'W', 'W'],
    ['L', 'W', 'L', 'L', 'W']
]
print(Solution().numIslands(grid1))  # Output: 4

# Test Case 2
grid2 = [
    ['W', 'L', 'L', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'W', 'L', 'W']
]
print(Solution().numIslands(grid2))  # Output: 2
