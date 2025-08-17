class Solution:
    def rotateMatrix(self, mat):
        n = len(mat)
        # Step 1: Transpose
        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        # Step 2: Reverse each column
        for j in range(n):
            for i in range(n//2):
                mat[i][j], mat[n-1-i][j] = mat[n-1-i][j], mat[i][j]
s = Solution()

mat1 = [[0,1,2],[3,4,5],[6,7,8]]
s.rotateMatrix(mat1)
print(mat1)  # [[2,5,8],[1,4,7],[0,3,6]]

mat2 = [[1,2],[3,4]]
s.rotateMatrix(mat2)
print(mat2)  # [[2,4],[1,3]]
