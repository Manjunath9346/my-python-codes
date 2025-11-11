class Solution:
	def isNegativeWeightCycle(self, n, edges):
		# Step 1: Initialize distances
		dist = [0] * n  # all 0 works since we check for any possible negative cycle
		
		# Step 2: Relax all edges (n - 1) times
		for _ in range(n - 1):
			for u, v, w in edges:
				if dist[u] + w < dist[v]:
					dist[v] = dist[u] + w
		
		# Step 3: Check for negative weight cycle
		for u, v, w in edges:
			if dist[u] + w < dist[v]:
				return 1  # Negative cycle detected
		
		return 0  # No negative cycle
sol = Solution()

print(sol.isNegativeWeightCycle(3, [[0,1,-1],[1,2,-2],[2,0,-3]]))  #  Output: 1 (contains negative cycle)
print(sol.isNegativeWeightCycle(3, [[0,1,-1],[1,2,-2],[2,0,3]]))   #  Output: 0 (no cycle)
print(sol.isNegativeWeightCycle(4, [[0,1,1],[1,2,2],[2,3,3]]))     #  Output: 0
print(sol.isNegativeWeightCycle(4, [[0,1,1],[1,2,-1],[2,0,-1]]))   #  Output: 1
