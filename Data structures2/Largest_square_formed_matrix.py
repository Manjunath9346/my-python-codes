from typing import List

class Solution:
    def maxSquare(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        dp = [[0]*m for _ in range(n)]
        max_side = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if i == 0 or j == 0:   # first row or column
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    max_side = max(max_side, dp[i][j])
        
        return max_side
sol = Solution()
print(sol.maxSquare([[0,1,1,0,1],
                     [1,1,0,1,0],
                     [0,1,1,1,0],
                     [1,1,1,1,0],
                     [1,1,1,1,1],
                     [0,0,0,0,0]]))  # Output: 3

print(sol.maxSquare([[1,1],
                     [1,1]]))  # Output: 2

print(sol.maxSquare([[0,0],
                     [0,0]]))  # Output: 0
