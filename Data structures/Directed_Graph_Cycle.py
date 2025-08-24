class Solution:
    def isCycle(self, V, edges):
        # Build adjacency list
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
        
        visited = [False] * V
        recStack = [False] * V
        
        # DFS function to detect cycle
        def dfs(node):
            visited[node] = True
            recStack[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recStack[neighbor]:
                    return True
            recStack[node] = False
            return False
        
        # Check for cycles starting from all vertices
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        return False

# Test cases
sol = Solution()

# Test case 1
V1 = 4
edges1 = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]
print(sol.isCycle(V1, edges1))  # Output: True

# Test case 2
V2 = 4
edges2 = [[0, 1], [0, 2], [1, 2], [2, 3]]
print(sol.isCycle(V2, edges2))  # Output: False
