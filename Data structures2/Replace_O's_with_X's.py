# User function Template for python3

class Solution:
    def fill(self, mat):
        n, m = len(mat), len(mat[0])
        
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != 'O':
                return
            mat[i][j] = '#'   # Mark as visited (safe O)
            # Explore 4 directions
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # Step 1: Mark 'O's connected to boundaries
        for i in range(n):
            if mat[i][0] == 'O': dfs(i, 0)
            if mat[i][m-1] == 'O': dfs(i, m-1)
        for j in range(m):
            if mat[0][j] == 'O': dfs(0, j)
            if mat[n-1][j] == 'O': dfs(n-1, j)
        
        # Step 2: Flip surrounded 'O' to 'X', restore safe ones
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O':
                    mat[i][j] = 'X'   # Surrounded, flip
                elif mat[i][j] == '#':
                    mat[i][j] = 'O'   # Restore safe O
        
        return mat


# Example usage:
sol = Solution()
mat1 = [['X', 'X', 'X', 'X'], 
        ['X', 'O', 'X', 'X'], 
        ['X', 'O', 'O', 'X'], 
        ['X', 'O', 'X', 'X'], 
        ['X', 'X', 'O', 'O']]
print(sol.fill(mat1))
# Output:
# [['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'X', 'O', 'O']]
