class Solution:

    def findMaxArea(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        # All 8 possible directions
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0),  (1, 1)]

        def dfs(i, j):
            # Mark the cell visited and initialize area
            visited[i][j] = True
            area = 1
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and grid[ni][nj] == 1:
                    area += dfs(ni, nj)
            return area

        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
sol = Solution()

print(sol.findMaxArea([[1,1,1,0],
                       [0,0,1,0],
                       [0,0,0,1]]))
# ✅ Output: 5

print(sol.findMaxArea([[0,1]]))
# ✅ Output: 1

print(sol.findMaxArea([[1,0,1],
                       [1,1,0],
                       [0,1,1]]))
# ✅ Output: 6

print(sol.findMaxArea([[0,0,0],
                       [0,0,0],
                       [0,0,0]]))
# ✅ Output: 0
