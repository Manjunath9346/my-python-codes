class Solution:
    def graphColoring(self, v, edges, m):
        # Step 1: Build adjacency list
        graph = [[] for _ in range(v)]
        for u, w in edges:
            graph[u].append(w)
            graph[w].append(u)

        # Step 2: Initialize color assignment array
        color = [0] * v  # 0 means no color assigned

        # Step 3: Backtracking function
        def is_safe(node, c):
            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return False
            return True

        def solve(node):
            if node == v:
                return True
            for c in range(1, m + 1):
                if is_safe(node, c):
                    color[node] = c
                    if solve(node + 1):
                        return True
                    color[node] = 0  # backtrack
            return False

        return solve(0)
V = 4
edges = [[0, 1], [1, 3], [2, 3], [3, 0], [0, 2]]
m = 3

sol = Solution()
print(sol.graphColoring(V, edges, m))  # Output: True
