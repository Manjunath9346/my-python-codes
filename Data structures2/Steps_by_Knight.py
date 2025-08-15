from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos, targetPos, n):
        if knightPos == targetPos: return 0
        moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        visited = [[False]*n for _ in range(n)]
        q = deque([(knightPos[0]-1, knightPos[1]-1, 0)])  # convert 1-based to 0-based
        visited[knightPos[0]-1][knightPos[1]-1] = True
        while q:
            x, y, steps = q.popleft()
            for dx, dy in moves:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                    if [nx+1, ny+1] == targetPos:  # back to 1-based for comparison
                        return steps+1
                    visited[nx][ny] = True
                    q.append((nx, ny, steps+1))
        return -1  # should never reach here if target is valid

s = Solution()

# Test case 1
print(s.minStepToReachTarget([3, 3], [1, 2], 3))  # Output: 1

# Test case 2
print(s.minStepToReachTarget([4, 5], [1, 1], 6))  # Output: 3

# Test case 3
print(s.minStepToReachTarget([1, 1], [1, 1], 8))  # Output: 0
