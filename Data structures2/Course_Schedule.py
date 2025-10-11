from collections import deque, defaultdict

class Solution:
    def findOrder(self, n, prerequisites):
        # Step 1: Build adjacency list and in-degree array
        adj = defaultdict(list)
        indegree = [0] * n
        
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        # Step 2: Initialize queue with all tasks having no prerequisites
        q = deque([i for i in range(n) if indegree[i] == 0])
        order = []
        
        # Step 3: Process queue (Kahn’s Algorithm)
        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        # Step 4: Check if valid topological ordering exists
        if len(order) == n:
            return order
        else:
            return []  # cycle detected → impossible
# Test 1
print(Solution().findOrder(2, [[1, 0]]))
# Possible output: [0, 1]

# Test 2
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
# Possible output: [0, 1, 2, 3] or [0, 2, 1, 3]

# Test 3
print(Solution().findOrder(3, [[0, 1], [1, 2], [2, 0]]))
# Output: []  (Cycle exists → not possible)
