from collections import deque

class Solution:
    def isPossible(self, N, P, prerequisites):
        adj = [[] for _ in range(N)]
        indegree = [0] * N
        
        # Build graph
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        # Queue for nodes with 0 indegree
        q = deque([i for i in range(N) if indegree[i] == 0])
        count = 0
        
        while q:
            node = q.popleft()
            count += 1
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        return count == N
print(Solution().isPossible(4, 3, [[1,0],[2,1],[3,2]]))  #  True (Yes)
print(Solution().isPossible(2, 2, [[1,0],[0,1]]))        #  False (No)
print(Solution().isPossible(3, 2, [[1,0],[2,1]]))        #  True (Yes)
print(Solution().isPossible(3, 3, [[0,1],[1,2],[2,0]]))  #  False (No)
