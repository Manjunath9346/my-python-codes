class Solution:
    def numProvinces(self, adj, V):
        def dfs(node, visited):
            visited[node] = True
            for neighbor in range(V):
                if adj[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor, visited)

        visited = [False] * V
        count = 0
        for i in range(V):
            if not visited[i]:
                dfs(i, visited)
                count += 1
        return count
adj = [[1, 0, 1],
       [0, 1, 0],
       [1, 0, 1]]
V = 3
# Output: 2
adj = [[1, 1],
       [1, 1]]
V = 2
# Output: 1
