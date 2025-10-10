class Solution:
    
    # Function to find a Mother Vertex in the Graph.
    def findMotherVertex(self, V, adj):
        visited = [False] * V
        last_vertex = 0
        
        # Step 1: Find a candidate using DFS
        def dfs(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
        
        for i in range(V):
            if not visited[i]:
                dfs(i)
                last_vertex = i
        
        # Step 2: Verify candidate
        visited = [False] * V
        dfs(last_vertex)
        if all(visited):
            return last_vertex
        return -1
sol = Solution()

# Test 1
V = 4
adj = [[1,2],[3],[3],[]]
print(sol.findMotherVertex(V, adj))  
# Output: 0

# Test 2
V = 5
adj = [[1,2],[3],[3],[],[]]
print(sol.findMotherVertex(V, adj))  
# Output: -1

# Test 3
V = 7
adj = [[1,2],[3],[1],[4],[5],[6],[]]
print(sol.findMotherVertex(V, adj))  
# Output: 0
