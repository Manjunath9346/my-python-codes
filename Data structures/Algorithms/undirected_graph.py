class Solution:
    def isCycle(self, V, edges):
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * V

        def dfs(node, parent):
            visited[node] = True
            for nbr in graph[node]:
                if not visited[nbr]:
                    if dfs(nbr, node):
                        return True
                elif nbr != parent:
                    return True
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False


def main():
    V = int(input())           # Number of vertices
    E = int(input())           # Number of edges
    edges = []

    for _ in range(E):
        u, v = map(int, input().split())
        edges.append((u, v))

    obj = Solution()
    ans = obj.isCycle(V, edges)
    print("Yes" if ans else "No")


if __name__ == "__main__":
    main()
