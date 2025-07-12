class Solution:
    def maxGold(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n = len(mat)
        m = len(mat[0])
        
        # Create a DP table with same dimensions
        dp = [[0] * m for _ in range(n)]
        
        # Fill the rightmost column first
        for i in range(n):
            dp[i][m - 1] = mat[i][m - 1]
        
        # Fill the DP table from right to left
        for j in range(m - 2, -1, -1):
            for i in range(n):
                # Possible moves
                right = dp[i][j + 1]
                right_up = dp[i - 1][j + 1] if i > 0 else 0
                right_down = dp[i + 1][j + 1] if i < n - 1 else 0
                
                dp[i][j] = mat[i][j] + max(right, right_up, right_down)
        
        # Find the maximum in the first column
        return max(dp[i][0] for i in range(n))
sol = Solution()

# Test Case 1
mat1 = [
    [1, 3, 3],
    [2, 1, 4],
    [0, 6, 4]
]
print(sol.maxGold(mat1))  
# Output: 12

# Test Case 2
mat2 = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]
]
print(sol.maxGold(mat2))  
# Output: 16

# Test Case 3
mat3 = [
    [1, 3, 3],
    [2, 1, 4],
    [0, 7, 5]
]
print(sol.maxGold(mat3))  
# Output: 14

# Test Case 4 (Edge)
print(sol.maxGold([[1]]))  
# Output: 1
