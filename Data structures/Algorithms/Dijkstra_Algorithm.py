import heapq
from collections import defaultdict

class Solution:
    def dijkstra(self, V, edges, src):
        # Build adjacency list: u -> [(v, w), ...]
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # Since the graph is undirected

        # Distance array
        dist = [float('inf')] * V
        dist[src] = 0

        # Min-heap to store (distance, node)
        heap = [(0, src)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, weight in adj[u]:
                if dist[v] > d + weight:
                    dist[v] = d + weight
                    heapq.heappush(heap, (dist[v], v))

        return dist
# Test Case 1
V = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2
print(Solution().dijkstra(V, edges, src))  # Output: [4, 3, 0]

# Test Case 2
V = 5
edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]
src = 0
print(Solution().dijkstra(V, edges, src))  # Output: [0, 4, 8, 10, 10]
