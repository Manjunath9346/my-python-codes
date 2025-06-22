from collections import deque, defaultdict

class Solution:
    
    def topoSort(self, V, edges):
        # Create adjacency list and in-degree array
        adj = defaultdict(list)
        indegree = [0] * V
        
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        # Queue for nodes with in-degree 0
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        topo_order = []
        
        while q:
            node = q.popleft()
            topo_order.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return topo_order if len(topo_order) == V else []
V = 4
edges = [[0, 1], [1, 2], [2, 3]]
# Possible Output: [0, 1, 2, 3]
V = 4
edges = [[3, 0], [1, 0], [2, 0]]
# Possible Outputs: [1, 2, 3, 0], [2, 3, 1, 0], etc.
