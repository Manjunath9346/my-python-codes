class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [10**8] * V
        dist[src] = 0

        # Relax all edges V-1 times
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != 10**8 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative weight cycles
        for u, v, w in edges:
            if dist[u] != 10**8 and dist[u] + w < dist[v]:
                return [-1]

        return dist
sol = Solution()

# Test Case 1
V = 5
edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
src = 0
print(sol.bellmanFord(V, edges, src))  # Output: [0, 5, 6, 6, 7]

# Test Case 2 (Negative weight cycle)
V = 4
edges = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]]
src = 0
print(sol.bellmanFord(V, edges, src))  # Output: [-1]

# Test Case 3
V = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2
print(sol.bellmanFord(V, edges, src))  # Output: [4, 3, 0]
