class Solution:
    def isBridge(self, V, edges, c, d):
        from collections import defaultdict
        graph = defaultdict(list)

        # Build adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        time = 0
        visited = [False] * V
        tin = [-1] * V  # discovery time
        low = [-1] * V  # lowest discovery time reachable

        def dfs(u, parent):
            nonlocal time
            visited[u] = True
            tin[u] = low[u] = time
            time += 1

            for v in graph[u]:
                if v == parent:
                    continue
                if not visited[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    # If low[v] > tin[u], (u, v) is a bridge
                    if low[v] > tin[u]:
                        if (u == c and v == d) or (u == d and v == c):
                            self.bridge = True
                else:
                    low[u] = min(low[u], tin[v])

        self.bridge = False
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)

        return 1 if self.bridge else 0
V = 4
edges = [[0, 1], [1, 2], [2, 3]]
c = 1
d = 2
V = 5
edges = [[0, 1], [0, 3], [1, 2], [2, 0], [3, 4]]
c = 0
d = 2
