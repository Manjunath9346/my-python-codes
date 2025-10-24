from typing import List
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        # Step 2: Dijkstra’s setup
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]  # (distance, node)
        
        while pq:
            curr_dist, node = heapq.heappop(pq)
            
            # Skip if we already found a shorter path
            if curr_dist > dist[node]:
                continue
            
            for nei, time in graph[node]:
                new_dist = curr_dist + time
                
                # Found shorter distance
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_dist, nei))
                
                # Found another shortest path
                elif new_dist == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        return ways[n - 1] % MOD
sol = Solution()

print(sol.countPaths(7, [
    [0,6,7],[0,1,2],[1,2,3],[1,3,3],
    [6,3,3],[3,5,1],[6,5,1],[2,5,1],
    [0,4,5],[4,6,2]
]))  #  Output: 4

print(sol.countPaths(6, [
    [0,5,8],[0,2,2],[0,1,1],[1,3,3],
    [1,2,3],[2,5,6],[3,4,2],[4,5,2]
]))  #  Output: 3
