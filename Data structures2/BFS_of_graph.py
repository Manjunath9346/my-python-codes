from collections import deque

class Solution:
    def bfs(self, adj):
        V = len(adj)                # number of vertices
        visited = [False] * V
        queue = deque()
        bfs_order = []

        queue.append(0)
        visited[0] = True

        while queue:
            node = queue.popleft()
            bfs_order.append(node)

            # traverse neighbors in the given order
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    queue.append(nei)

        return bfs_order
obj = Solution()

print(obj.bfs([[2, 3, 1], [0], [0, 4], [0], [2]]))
# Expected: [0, 2, 3, 1, 4]

print(obj.bfs([[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]))
# Expected: [0, 1, 2, 3, 4]
