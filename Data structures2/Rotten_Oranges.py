from collections import deque

class Solution:
    def orangesRotting(self, mat):
        n = len(mat)
        m = len(mat[0])
        q = deque()
        time = 0
        fresh = 0

        # Step 1: Initialize the queue with all rotten oranges
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append(((i, j), 0))  # ((row, col), time)
                elif mat[i][j] == 1:
                    fresh += 1

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: BFS
        while q:
            (x, y), t = q.popleft()
            time = max(time, t)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1:
                    mat[nx][ny] = 2  # rot the orange
                    fresh -= 1
                    q.append(((nx, ny), t + 1))

        return time if fresh == 0 else -1
sol = Solution()

# Test Case 1
mat1 = [
    [0, 1, 2],
    [0, 1, 2],
    [2, 1, 1]
]
print(sol.orangesRotting(mat1))  
# Output: 1

# Test Case 2
mat2 = [[2, 2, 0, 1]]
print(sol.orangesRotting(mat2))  
# Output: -1

# Test Case 3
mat3 = [
    [2, 2, 2],
    [0, 2, 0]
]
print(sol.orangesRotting(mat3))  
# Output: 0

# Test Case 4
mat4 = [
    [1, 1, 1],
    [1, 2, 1],
    [1, 1, 1]
]
print(sol.orangesRotting(mat4))  
# Output: 2
