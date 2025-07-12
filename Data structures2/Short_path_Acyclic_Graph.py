from typing import List
from collections import defaultdict, deque

class Solution:

    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list
        adj = defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))

        # Step 2: Perform topological sort using DFS
        visited = [False] * V
        stack = []

        def topo_sort(node):
            visited[node] = True
            for nei, _ in adj[node]:
                if not visited[nei]:
                    topo_sort(nei)
            stack.append(node)

        for i in range(V):
            if not visited[i]:
                topo_sort(i)

        # Step 3: Initialize distances
        dist = [float('inf')] * V
        dist[0] = 0  # Distance to source is 0

        # Step 4: Process nodes in topological order
        while stack:
            u = stack.pop()
            if dist[u] != float('inf'):
                for v, wt in adj[u]:
                    if dist[v] > dist[u] + wt:
                        dist[v] = dist[u] + wt

        # Step 5: Replace unreachable with -1
        return [d if d != float('inf') else -1 for d in dist]
sol = Solution()

# Test Case 1
V = 4
E = 2
edges = [[0, 1, 2], [0, 2, 1]]
print(sol.shortestPath(V, E, edges))
# Output: [0, 2, 1, -1]

# Test Case 2
V = 6
E = 7
edges = [[0, 1, 2], [0, 4, 1], [4, 5, 4], [4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]]
print(sol.shortestPath(V, E, edges))
# Output: [0, 2, 3, 6, 1, 5]

# Test Case 3 (Disconnected node)
V = 5
E = 3
edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3]]
print(sol.shortestPath(V, E, edges))
# Output: [0, 1, 3, 6, -1]
