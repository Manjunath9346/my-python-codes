class Solution:

    def kosaraju(self, adj):
        n = len(adj)  # number of vertices
        visited = [False] * n
        stack = []

        # Step 1: DFS to store finishing times of nodes
        def dfs(v):
            visited[v] = True
            for nei in adj[v]:
                if not visited[nei]:
                    dfs(nei)
            stack.append(v)   # push after visiting all neighbors

        for i in range(n):
            if not visited[i]:
                dfs(i)

        # Step 2: Reverse the graph
        rev_adj = [[] for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                rev_adj[v].append(u)

        # Step 3: DFS on reversed graph using stack order
        visited = [False] * n
        def dfs_rev(v):
            visited[v] = True
            for nei in rev_adj[v]:
                if not visited[nei]:
                    dfs_rev(nei)

        # Step 4: Count SCCs
        scc_count = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                dfs_rev(node)
                scc_count += 1

        return scc_count
# Test Case 1
adj = [[2, 3], [0], [1], [4], []]
# SCCs: {0,1,2}, {3}, {4}
print(Solution().kosaraju(adj))  # Output: 3

# Test Case 2
adj = [[1], [2], [0]]
# All are connected → one SCC
print(Solution().kosaraju(adj))  # Output: 1

# Test Case 3
adj = [[1], []]
# SCCs: {0}, {1}
print(Solution().kosaraju(adj))  # Output: 2

# Test Case 4
adj = [[], []]
# No edges, each node is its own SCC
print(Solution().kosaraju(adj))  # Output: 2

# Test Case 5
adj = [[1], [2], [3], [4], [0]]
# Forms a cycle of all nodes
print(Solution().kosaraju(adj))  # Output: 1
