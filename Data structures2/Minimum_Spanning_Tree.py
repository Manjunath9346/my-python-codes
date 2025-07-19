from typing import List
import heapq

class Solution:
    def spanningTree(self, V: int, adj: List[List[List[int]]]) -> int:
        visited = [False] * V
        min_heap = [(0, 0)]  # (weight, vertex)
        total_weight = 0

        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if visited[node]:
                continue
            visited[node] = True
            total_weight += weight

            for neighbor in adj[node]:
                next_node, wt = neighbor
                if not visited[next_node]:
                    heapq.heappush(min_heap, (wt, next_node))

        return total_weight
# Helper to convert edges to adjacency list
def build_adj(V, edges):
    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append([v, w])
        adj[v].append([u, w])
    return adj

sol = Solution()

# Test Case 1
V1 = 3
edges1 = [(0, 1, 5), (1, 2, 3), (0, 2, 1)]
adj1 = build_adj(V1, edges1)
print(sol.spanningTree(V1, adj1))  # Output: 4

# Test Case 2
V2 = 2
edges2 = [(0, 1, 5)]
adj2 = build_adj(V2, edges2)
print(sol.spanningTree(V2, adj2))  # Output: 5

# Test Case 3
V3 = 4
edges3 = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
adj3 = build_adj(V3, edges3)
print(sol.spanningTree(V3, adj3))  # Output: 19
