from collections import defaultdict, deque

class Solution:
    def safeNodes(self, V, edges):
        graph = defaultdict(list)
        rev_graph = defaultdict(list)
        indegree = [0] * V

        # Build reverse graph and indegree count
        for u, v in edges:
            graph[u].append(v)
            rev_graph[v].append(u)
            indegree[u] += 1

        q = deque()
        safe = [0] * V

        # Start from terminal nodes (nodes with no outgoing edges)
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        # Reverse BFS (topological sort approach)
        while q:
            node = q.popleft()
            safe[node] = 1
            for prev in rev_graph[node]:
                indegree[prev] -= 1
                if indegree[prev] == 0:
                    q.append(prev)

        # Return all safe nodes in sorted order
        return [i for i in range(V) if safe[i] == 1]


# Test Case 1
print(Solution().safeNodes(5, [[1, 0], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]))
# Output: [0, 1, 2, 3, 4]

# Test Case 2
print(Solution().safeNodes(4, [[1, 2], [2, 3], [3, 2]]))
# Output: [0]

# Test Case 3
print(Solution().safeNodes(3, [[0, 1], [1, 2]]))
# Output: [0, 1, 2]

# Test Case 4
print(Solution().safeNodes(3, [[0, 1], [1, 0], [1, 2]]))
# Output: [2]

# Test Case 5
print(Solution().safeNodes(6, [[0, 1], [1, 2], [2, 3], [3, 1], [4, 5]]))
# Output: [4, 5]
