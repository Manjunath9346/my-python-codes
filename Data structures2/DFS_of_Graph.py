class Solution:
    def dfs(self, adj):
        V = len(adj)
        visited = [False] * V
        result = []

        def dfs_util(node):
            visited[node] = True
            result.append(node)

            for nei in adj[node]:
                if not visited[nei]:
                    dfs_util(nei)

        dfs_util(0)   # start DFS from vertex 0
        return result
obj = Solution()

print(obj.dfs([[2, 3, 1], [0], [0, 4], [0], [2]]))
# Expected: [0, 2, 4, 3, 1]

print(obj.dfs([[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]))
# Expected: [0, 1, 2, 3, 4]
