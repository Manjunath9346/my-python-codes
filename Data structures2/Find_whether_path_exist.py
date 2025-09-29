class Solution:
    #Function to find whether a path exists from the source to destination.
    def is_Possible(self, grid):
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        
        # find source
        src_x = src_y = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    src_x, src_y = i, j
                    break
            if src_x != -1:
                break

        # directions: up, down, left, right
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        from collections import deque
        q = deque([(src_x, src_y)])
        visited[src_x][src_y] = True

        while q:
            x, y = q.popleft()
            if grid[x][y] == 2:   # reached destination
                return 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if grid[nx][ny] != 0:  # not a wall
                        visited[nx][ny] = True
                        q.append((nx, ny))

        return 0
sol = Solution()

# Example 1
grid1 = [
    [3,0,3,0,0],
    [3,0,0,0,3],
    [3,3,3,3,3],
    [0,2,3,0,0],
    [3,0,0,1,3]
]
print(sol.is_Possible(grid1))  # Expected: 0

# Example 2
grid2 = [
    [1,3],
    [3,2]
]
print(sol.is_Possible(grid2))  # Expected: 1

# Edge Case: Source == Destination
grid3 = [[2]]
print(sol.is_Possible(grid3))  # Expected: 1

# Edge Case: No path (walls block)
grid4 = [
    [1,0,0],
    [0,0,0],
    [0,0,2]
]
print(sol.is_Possible(grid4))  # Expected: 0

# Large Open Grid
grid5 = [[3]*5 for _ in range(5)]
grid5[0][0] = 1
grid5[4][4] = 2
print(sol.is_Possible(grid5))  # Expected: 1
