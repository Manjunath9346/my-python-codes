from collections import deque, defaultdict

class Solution:
    def isBipartite(self, V, edges):
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        color = [-1] * V  # -1 means unvisited

        for i in range(V):
            if color[i] == -1:
                if not self.bfs_check(i, adj, color):
                    return False
        return True

    def bfs_check(self, start, adj, color):
        queue = deque()
        queue.append(start)
        color[start] = 0  # Start coloring with 0

        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]  # Alternate color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
# Test 1 - Bipartite
V1 = 3
edges1 = [[0, 1], [1, 2]]
print(Solution().isBipartite(V1, edges1))  # Output: True

# Test 2 - Not Bipartite
V2 = 4
edges2 = [[0, 3], [1, 2], [3, 2], [0, 2]]
print(Solution().isBipartite(V2, edges2))  # Output: False

# Test 3 - Disconnected Graph (All components bipartite)
V3 = 5
edges3 = [[0, 1], [2, 3]]
print(Solution().isBipartite(V3, edges3))  # Output: True

# Test 4 - Self Loop
V4 = 2
edges4 = [[0, 0], [0, 1]]
print(Solution().isBipartite(V4, edges4))  # Output: False

# Test 5 - Complete Bipartite
V5 = 6
edges5 = [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]]
print(Solution().isBipartite(V5, edges5))  # Output: True
