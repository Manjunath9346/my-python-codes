from collections import deque

class Solution:
    def shortestDistance(self, N, M, A, X, Y):
        # If start is blocked
        if A[0][0] == 0:
            return -1
        
        # Directions: up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # BFS queue: (row, col, distance)
        q = deque([(0, 0, 0)])
        visited = [[False]*M for _ in range(N)]
        visited[0][0] = True
        
        while q:
            i, j, dist = q.popleft()
            
            # Reached destination
            if i == X and j == Y:
                return dist
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and A[ni][nj] == 1:
                    visited[ni][nj] = True
                    q.append((ni, nj, dist + 1))
        
        return -1
