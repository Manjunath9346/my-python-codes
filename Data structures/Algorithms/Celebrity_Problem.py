class Solution:
    def celebrity(self, mat):
        n = len(mat)
        stack = [i for i in range(n)]
        
        # Find a potential celebrity
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            
            if mat[a][b] == 1:
                # a knows b, so a cannot be a celebrity
                stack.append(b)
            else:
                # a doesn't know b, so b cannot be a celebrity
                stack.append(a)
        
        if not stack:
            return -1
        
        candidate = stack.pop()
        
        # Verify candidate
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        
        return candidate
mat = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
sol = Solution()
print(sol.celebrity(mat))  # Output: 1
