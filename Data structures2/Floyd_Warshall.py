class Solution:
    def floydWarshall(self, dist):
        V = len(dist)
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    # Avoid integer overflow if either dist[i][k] or dist[k][j] is 10^8
                    if dist[i][k] != 10**8 and dist[k][j] != 10**8:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
dist = [
    [0, 4, 10**8, 5, 10**8],
    [10**8, 0, 1, 10**8, 6],
    [2, 10**8, 0, 3, 10**8],
    [10**8, 10**8, 1, 0, 2],
    [1, 10**8, 10**8, 4, 0]
]
