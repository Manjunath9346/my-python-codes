from collections import deque

class Solution:
    def shortestPath(self, adj, src):
        n = len(adj)
        dist = [-1] * n  # Initialize all distances as -1
        dist[src] = 0

        q = deque([src])
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)

        return dist
adj = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]]
src = 0
print(Solution().shortestPath(adj, src))
# Output: [0, 1, 2, 1, 2, 3, 3, 4, 4]
adj = [[3], [3], [], [0, 1]]
src = 3
print(Solution().shortestPath(adj, src))
# Output: [1, 1, -1, 0]
