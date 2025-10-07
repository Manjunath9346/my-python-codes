from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Build adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Initialize distance and parent arrays
        dist = [float('inf')] * (n + 1)
        parent = [i for i in range(n + 1)]
        
        dist[1] = 0
        pq = [(0, 1)]  # (distance, node)
        
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            
            for nei, wt in graph[node]:
                if d + wt < dist[nei]:
                    dist[nei] = d + wt
                    parent[nei] = node
                    heapq.heappush(pq, (dist[nei], nei))
        
        # If destination is unreachable
        if dist[n] == float('inf'):
            return [-1]
        
        # Reconstruct path
        path = []
        curr = n
        while parent[curr] != curr:
            path.append(curr)
            curr = parent[curr]
        path.append(1)
        path.reverse()
        
        # Return total distance + path
        return [dist[n]] + path
# Test 1
sol = Solution()
print(sol.shortestPath(5, 6, [[1,2,2],[2,5,5],[2,3,4],[1,4,1],[4,3,3],[3,5,1]]))
# Output: [5, 1, 4, 3, 5]

# Test 2
print(sol.shortestPath(2, 1, [[1, 2, 2]]))
# Output: [2, 1, 2]

# Test 3
print(sol.shortestPath(2, 0, []))
# Output: [-1]

# Test 4 (Extra)
print(sol.shortestPath(4, 4, [[1,2,1],[2,3,1],[3,4,1],[1,4,10]]))
# Output: [3, 1, 2, 3, 4]
